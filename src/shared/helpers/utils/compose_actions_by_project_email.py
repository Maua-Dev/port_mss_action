
def compose_actions_by_project_email(self) -> str:
    message = f"""
        <!DOCTYPE html>
        <html lang="pt-br">
        <head>
            <meta charset="UTF-8">
            <title>Relatório de Ações po Projeto</title>
        </head>
        <body style="font-family: Arial, sans-serif; margin: 0; padding: 20px; background-color: #f4f4f9;">
            <div style="max-width: 600px; margin: auto; background-color: #ffffff; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);">
                <h2 style="color: #333333;">Olá, Vitin!</h2>
                <p style="color: #555555;">Segue arquivo com todas as ações de cada projeto da Dev Community Mauá.</p>
                <a href="cid:relatorio_acoes.xlsx" style="display: inline-block; background-color: #4CAF50; color: #ffffff; padding: 10px 20px; text-decoration: none; border-radius: 4px;">Baixar Relatório</a>
                <p style="color: #555555;">Para que você pare de perguntar: "E aí, grupo? Como estamos de projeto? (seguido de @ para cada membro de cada área)"</p>
                <hr>
                <p style="color: #555555;">Com carinho,<br>Equipe do Portal Interno (#ehobeckas😎)</p>
            </div>
        </body>
        </html>
        """
    return message