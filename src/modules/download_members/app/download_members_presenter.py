import boto3
from .download_members_extractor import DownloadMembersExtractor
from .download_members_transformer import DownloadMembersTransformer
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock


repo_member = MemberRepositoryMock()
extractor = DownloadMembersExtractor(repo=repo_member)
transformer = DownloadMembersTransformer(extractor=extractor)

def lambda_handler(event,context):
    file_content = transformer()
    
    return {
        'statusCode': 200,
        'body': file_content.getvalue(),
        'headers': {
            'Content-Type': 'text/csv',
            'Content-Disposition': 'attachment; filename=membros.csv'
        },
    }