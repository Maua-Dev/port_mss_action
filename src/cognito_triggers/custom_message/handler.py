import os
import urllib.parse

def _build_confirm_link(event):
    base = os.environ.get("CONFIRMATION_URL_BASE", "")
    code = event["request"]["codeParameter"] 
    username = urllib.parse.quote(event.get("userName", ""))
    client_id = event.get("callerContext", {}).get("clientId", "")
    region = event.get("region", "")
    query = urllib.parse.urlencode({
        "code": code,
        "username": username,
        "client_id": client_id,
        "region": region
    }, safe="{}")  # mantém {####}
    return f"{base}?{query}"

def handler(event, _context):
    trigger = event.get("triggerSource", "")
    link = _build_confirm_link(event)

    subject = "Confirme seu e-mail - Portal Interno"
    body_html = f"""
    <html>
      <body style="font-family: Arial, sans-serif">
        <h2>Bem-vindo(a)!</h2>
        <p>Para ativar sua conta, confirme seu e-mail clicando no botão abaixo:</p>
        <p><a href="{link}" style="background:#2563eb;color:#fff;padding:12px 18px;border-radius:8px;text-decoration:none;">Confirmar E-mail</a></p>
        <p>Ou use este código: <b>{event["request"]["codeParameter"]}</b></p>
        <hr/>
        <small>Se você não solicitou, ignore este e-mail.</small>
      </body>
    </html>
    """

    event["response"]["emailSubject"]  = subject
    event["response"]["emailMessage"]  = body_html
    event["response"]["smsMessage"]    = f"Seu código de confirmação: {event['request']['codeParameter']}"

    return event
