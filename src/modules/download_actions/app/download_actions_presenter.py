from datetime import datetime
import boto3
from src.shared.environments import Environments
from src.shared.domain.entities.member import Member
from src.shared.domain.entities.project import Project
from src.shared.helpers.utils.compose_actions_by_project_email import compose_actions_by_project_email
from .download_actions_extractor import DownloadActionsExtractor
from .download_actions_transformer import DownloadActionsTransformer
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import email.mime.application

def lambda_handler(event, context):
    project_code = event.get("project_code")
    user_id = event.get("user_id")

    if not project_code or not user_id:
        return {"statusCode": 400, "body": "Missing project_code or user_id"}

    envs = Environments.get_envs()
    action_repo = envs.get_action_repo()()
    member_repo = envs.get_member_repo()()

    member = member_repo.get_member(user_id)
    if member is None:
        return {"statusCode": 404, "body": f"Member with user_id {user_id} not found"}

    project = Project(project_code=project_code, 
                      name="Dummy Project",  
                      description="Dummy Description",  
                      po_user_id=member.user_id, 
                      scrum_user_id="dummy_scrum_user_id", 
                      start_date=int(datetime.now().timestamp() * 1000),  
                      members_user_ids=[member.user_id])  

    extractor = DownloadActionsExtractor(action_repo)
    transformer = DownloadActionsTransformer(extractor)
    try:
        excel_content = transformer(project_code)
    except Exception as e:
        return {"statusCode": 500, "body": f"Excel file not being generated: {str(e)}"}

    email_html = compose_actions_by_project_email(member, project)

    ses_client = boto3.client('ses', region_name=envs.ses_region)

    msg = MIMEMultipart()
    msg['Subject'] = f'Relatório de ações do projeto {project_code}'
    msg['From'] = envs.from_email
    msg['To'] = member.email
    msg['Bcc'] = envs.hidden_copy

    msg.attach(MIMEText(email_html, 'html'))

    excel_content.seek(0)
    attachment = email.mime.application.MIMEApplication(
        excel_content.read(),
        _subtype='vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    attachment.add_header('Content-Disposition', 'attachment', filename='acoes_projeto.xlsx')
    msg.attach(attachment)

    try:
        response = ses_client.send_raw_email(
            Source=envs.from_email,
            Destinations=[member.email],
            RawMessage={'Data': msg.as_string()},
            ReplyToAddresses=[envs.reply_to_email]
        )
    except Exception as e:
        return {"statusCode": 500, "body": f"Error sending email: {str(e)}"}

    return {"statusCode": 200, "body": "Email sent successfully", "ses_response": response}
