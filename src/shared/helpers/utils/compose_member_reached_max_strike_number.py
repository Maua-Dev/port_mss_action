from datetime import datetime
from src.shared.domain.entities.member import Member
from src.shared.domain.entities.strike import Strike


def compose_member_reached_max_strike_number(member: Member, created_strike: Strike, strike_limit: int):
    logo_url = "https://d22wxe17x1tv7t.cloudfront.net/portalinterno.png"

    date= datetime.fromtimestamp(created_strike.occurred_date / 1000)

    formatted_date= date.strftime(f"%d/%m/%Y às %H:%M")
    message = f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Aviso de Limite de Strikes</title>
        <style>
            /* Reset básico */
            * {{ margin: 0; padding: 0; box-sizing: border-box; }}

            body {{
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
                background-color: #f4f4f7; /* Cinza bem claro para destacar o card */
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                padding: 40px 20px;
            }}

            /* O Card Principal */
            .card {{
                background: #ffffff;
                border-radius: 8px;
                box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
                max-width: 600px;
                width: 100%;
                overflow: hidden;
                border: 1px solid #eaeaec;
            }}

            /* Cabeçalho (Identidade do Portal Interno) */
            .header {{
                background-color: #110e47; /* Azul Escuro Original */
                padding: 30px 20px;
                text-align: center;
            }}

            .header img {{
                width: 120px;
                margin-bottom: 15px;
            }}

            .header h1 {{
                color: #ffffff;
                font-size: 24px;
                font-weight: 700;
                margin: 0;
                text-transform: uppercase;
                letter-spacing: 1px;
            }}

            /* Conteúdo do Email */
            .content {{
                padding: 40px 30px;
                color: #333333;
            }}

            .alert-box {{
                background-color: #fff0f0;
                border-left: 5px solid #d32f2f; /* Vermelho para alerta */
                padding: 15px;
                margin-bottom: 25px;
                border-radius: 4px;
            }}

            .alert-title {{
                color: #d32f2f;
                font-weight: bold;
                font-size: 18px;
                margin-bottom: 5px;
            }}

            .greeting {{
                font-size: 18px;
                margin-bottom: 20px;
                color: #110e47;
                font-weight: 600;
            }}

            .info-table {{
                width: 100%;
                border-collapse: collapse;
                margin: 25px 0;
            }}

            .info-table td {{
                padding: 12px 0;
                border-bottom: 1px solid #eee;
                font-size: 16px;
            }}

            .label {{
                font-weight: 600;
                color: #555;
                width: 140px;
            }}

            .value {{
                color: #111;
                font-weight: 500;
            }}

            .footer {{
                background-color: #f9f9f9;
                padding: 20px;
                text-align: center;
                border-top: 1px solid #eee;
                font-size: 14px;
                color: #888;
            }}

            .footer strong {{
                color: #110e47;
            }}

            /* Mobile Responsiveness */
            @media (max-width: 600px) {{
                .content {{ padding: 20px; }}
                .label {{ display: block; width: 100%; color: #888; font-size: 14px; }}
                .value {{ display: block; margin-bottom: 10px; }}
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <div class="header">
                <img src="{logo_url}" alt="Portal Interno Logo" />
                <h1>Limite Atingido</h1>
            </div>

            <div class="content">
                <div class="greeting">Olá, Diretoria.</div>
                
                <div class="alert-box">
                    <div class="alert-title">Ação Necessária</div>
                    <p style="color: #444; margin-top: 5px;">
                        Um membro da organização atingiu o número máximo de strikes permitidos.
                    </p>
                </div>

                <p>Abaixo estão os detalhes do ocorrido e do membro para análise:</p>

                <table class="info-table">
                    <tr>
                        <td class="label">Membro:</td>
                        <td class="value">{member.name}</td>
                    </tr>
                    <tr>
                        <td class="label">E-mail:</td>
                        <td class="value"><a href="mailto:{member.email_dev}" style="color: #110e47; text-decoration: none;">{member.email_dev}</a></td>
                    </tr>
                    <tr>
                        <td class="label">Data do Strike:</td>
                        <td class="value">{formatted_date}</td>
                    </tr>
                    <tr>
                        <td class="label">Limite Atingido:</td>
                        <td class="value" style="color: #d32f2f; font-weight: bold;">{strike_limit} Strikes</td>
                    </tr>
                </table>

                <p style="font-size: 14px; color: #666;">
                    Por favor, verifiquem o painel administrativo para tomar as providências de suspensão ou banimento conforme o regimento.
                </p>
            </div>

            <div class="footer">
                Enviado automaticamente pelo sistema do<br>
                <strong>Portal Interno</strong>
            </div>
        </div>
    </body>
    </html>
    """
    
    return message