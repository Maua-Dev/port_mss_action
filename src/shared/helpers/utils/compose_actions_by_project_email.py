from src.shared.domain.entities.member import Member
from src.shared.domain.entities.project import Project

def compose_actions_by_project_email( member: Member, project: Project) -> str:
    member_name = member.name
    project_name = project.name
    message = """
        <!DOCTYPE html>
        <html lang="pt-br" charset="UTF-8">
        <head>
        </head>
        <body style="margin: 0; padding: 0; display: flex; align-items: center; justify-content: center; min-height: 100vh; background-color: white; font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">
        <table class="main" style="width: 50vw; max-width: 600px; background-color: white; border-radius: 10px; box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.25); overflow: hidden;">
            <tr>
            <td>
                <table class="TittleBox" style="width: 100%; background-color: #110e47; border-radius: 10px 10px 0 0;">
                <tr>
                    <td style="text-align: center; padding: 20px;">
                    <img alt="PI Logo" src="https://d22wxe17x1tv7t.cloudfront.net/portalinterno.png" style="width: 60%;"/>
                    <h1 style="color: #ffffff; margin-top: 10px;"><strong>Ação Invalidada!</strong></h1>
                    </td>
                </tr>
                </table>
                <table class="ContentBox" style="width: 100%; background-color: #282470;  border-top: 1px solid #ffffff; border-radius: 0 0 10px 10px;">
                <tr>
                    <td style="text-align: center; padding: 20px;">
                    <div class="TextsBox" style="word-wrap: break-word;">
                        <h2 style="color: #ffffff;">Olá, {member_name}<p>Segue relatório com todas as ações do projeto: {project_name}.
                            Para mais informações, por favor, entre em contato com a equipe de suporte.</p></h2>
                    </div>
                    </td>
                </tr>
                </table>
                <table class="BottomBox" style="width: 100%; background-color: #110e47; border-top: 1px solid #ffffff; border-radius: 0 0 10px 10px;">
                <tr>
                    <td style="text-align: center; padding: 20px;">
                    <div class="TextsBox" style="color: #ffffff; word-wrap: break-word;">
                        <h2>Atenciosamente,</h2>
                        <h2><strong>Equipe do Portal Interno</strong>&#127744;</h2>
                    </div>
                    </td>
                </tr>
                </table>
            </td>
            </tr>
        </table>
        </body>
        </html>
        """
    message = message.format(member_name=member_name, project_name=project_name)
    return message