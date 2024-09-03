from src.shared.domain.entities.member import Member
from src.shared.domain.entities.action import Action

def compose_deleted_user_email(Member: Member, Action: Action):
    name = Member.name
    action = Action.title
    message = """
    
        <!DOCTYPE html>
    <html xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">

    <head>
        <!--[if gte mso 9]>
            <xml>
            <o:OfficeDocumentSettings>
            <o:AllowPNG/>
            <o:PixelsPerInch>96</o:PixelsPerInch>
            </o:OfficeDocumentSettings>
            </xml><![endif]-->

        <style type="text/css">
            @media only screen and (min-width: 620px) {
                    {
                        {
                            {
                            .u-row {
                                    {
                                        {
                                            {
                                            width: 600px !important;
                                        }
                                    }
                                }
                            }

                            .u-row .u-col {
                                    {

                                        {
                                            {
                                            vertical-align: top;
                                        }
                                    }
                                }
                            }

                            .u-row .u-col-50 {
                                    {

                                        {
                                            {
                                            width: 300px !important;
                                        }
                                    }
                                }
                            }

                            .u-row .u-col-100 {
                                    {

                                        {
                                            {
                                            width: 600px !important;
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }

            @media (max-width: 620px) {
                    {
                        {
                            {
                            .u-row-container {
                                    {
                                        {
                                            {
                                            max-width: 100% !important;
                                            padding-left: 0px !important;
                                            padding-right: 0px !important;
                                        }
                                    }
                                }
                            }

                            .u-row .u-col {
                                    {

                                        {
                                            {
                                            min-width: 320px !important;
                                            max-width: 100% !important;
                                            display: block !important;
                                        }
                                    }
                                }
                            }

                            .u-row {
                                    {

                                        {
                                            {
                                            width: 100% !important;
                                        }
                                    }
                                }
                            }

                            .u-col {
                                    {

                                        {
                                            {
                                            width: 100% !important;
                                        }
                                    }
                                }
                            }

                            .u-col>div {
                                    {

                                        {
                                            {
                                            margin: 0 auto;
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }

            body {
                    {

                        {
                            {
                            margin: 0;
                            padding: 0;
                        }
                    }
                }
            }

            table,
            tr,
            td {
                    {

                        {
                            {
                            vertical-align: top;
                            border-collapse: collapse;
                        }
                    }
                }
            }

            p {
                    {

                        {
                            {
                            margin: 0;
                        }
                    }
                }
            }

            .ie-container table,
            .mso-container table {
                    {

                        {
                            {
                            table-layout: fixed;
                        }
                    }
                }
            }

            * {
                    {

                        {
                            {
                            line-height: inherit;
                        }
                    }
                }
            }

            a[x-apple-data-detectors=\'true\'] {
                    {

                        {
                            {
                            color: inherit !important;
                            text-decoration: none !important;
                        }
                    }
                }
            }

            table,
            td {
                    {

                        {
                            {
                            color: #000000;
                        }
                    }
                }
            }

            #u_body a {
                    {

                        {
                            {
                            color: #223166;
                            text-decoration: underline;
                        }
                    }
                }
            }

            @media (max-width: 480px) {
                    {
                        {
                            {
                            #u_content_heading_6 .v-container-padding-padding {
                                    {
                                        {
                                            {
                                            padding: 20px 10px 40px !important;
                                        }
                                    }
                                }
                            }

                            #u_content_heading_6 .v-font-size {
                                    {

                                        {
                                            {
                                            font-size: 20px !important;
                                        }
                                    }
                                }
                            }

                            #u_content_text_deprecated_7 .v-container-padding-padding {
                                    {

                                        {
                                            {
                                            padding: 30px 10px 10px !important;
                                        }
                                    }
                                }
                            }

                            #u_content_text_deprecated_8 .v-container-padding-padding {
                                    {

                                        {
                                            {
                                            padding: 10px 10px 30px !important;
                                        }
                                    }
                                }
                            }

                            #u_content_text_deprecated_9 .v-container-padding-padding {
                                    {

                                        {
                                            {
                                            padding: 10px 10px 20px !important;
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        </style>
        <title></title>
    </head>

    <body class="clean-body u_body"
        style="margin: 0;padding: 0;-webkit-text-size-adjust: 100%;background-color: #f8f8fc;color: #000000">
        <table id="u_body"
            style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;min-width: 320px;Margin: 0 auto;background-color: #f8f8fc;width:100%"
            cellpadding="0" cellspacing="0">
            <tbody>
                <tr style="vertical-align: top">
                    <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">
                        <div class="u-row-container" style="padding: 0px;background-color: transparent">
                            <div class="u-row"
                                style="Margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;">
                                <div
                                    style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">
                                    <div class="u-col u-col-50"
                                        style="max-width: 320px;min-width: 300px;display: table-cell;vertical-align: top;">
                                        <div
                                            style="background-color: #223166;height: 100%;width: 100% !important;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
                                            <div
                                                style="box-sizing: border-box; height: 100%; padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
                                                <table style="font-family:'Open Sans',sans-serif;" role="presentation"
                                                    cellpadding="0" cellspacing="0" width="100%" border="0">
                                                    <tbody>
                                                        <tr>
                                                            <td class="v-container-padding-padding"
                                                                style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:'Open Sans',sans-serif;"
                                                                align="left">
                                                                <table width="100%" cellpadding="0" cellspacing="0"
                                                                    border="0">
                                                                    <tr>
                                                                        <td style="padding-right: 0px;padding-left: 0px;"
                                                                            align="center">
                                                                            <a href="https://d22wxe17x1tv7t.cloudfront.net/portalinterno.png"
                                                                                target="_blank"><img align="center"
                                                                                    border="0"
                                                                                    src="https://d22wxe17x1tv7t.cloudfront.net/portalinterno.png"
                                                                                    alt="Logo Portal Interno" title="Portal Interno"
                                                                                    style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: inline-block !important;border: none;height: auto;float: none;width: 65%;max-width: 280px;"
                                                                                    width="280"></a>
                                                                        </td>
                                                                    </tr>
                                                                </table>
                                                            </td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="u-col u-col-50"
                                        style="max-width: 320px;min-width: 300px;display: table-cell;vertical-align: top;">
                                        <div
                                            style="background-color: #223166;height: 100%;width: 100% !important;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
                                            <div
                                                style="box-sizing: border-box; height: 100%; padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
                                                <table style="font-family:'Open Sans',sans-serif;" role="presentation"
                                                    cellpadding="0" cellspacing="0" width="100%" border="0">
                                                    <tbody>
                                                        <tr>
                                                            <td class="v-container-padding-padding"
                                                                style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:'Open Sans',sans-serif;"
                                                                align="left">
                                                                <table width="100%" cellpadding="0" cellspacing="0"
                                                                    border="0">
                                                                    <tr>
                                                                        <td style="padding-right: 0px;padding-left: 0px;"
                                                                            align="center"><img align="center" border="0"
                                                                                src="https://d3ebnpochj0915.cloudfront.net/logo_maua_branco.png"
                                                                                alt="Logo Maua" title="Logo Maua"
                                                                                style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: inline-block !important;border: none;height: auto;float: none;width: 100%;max-width: 280px;"
                                                                                width="280"></td>
                                                                    </tr>
                                                                </table>
                                                            </td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="u-row-container" style="padding: 0px;background-color: transparent">
                            <div class="u-row"
                                style="Margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;">
                                <div
                                    style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">
                                    <div class="u-col u-col-100"
                                        style="max-width: 320px;min-width: 600px;display: table-cell;vertical-align: top;">
                                        <div
                                            style="background-color: #223166;height: 100%;width: 100% !important;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
                                            <div
                                                style="box-sizing: border-box; height: 100%; padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
                                                <table id="u_content_heading_6" style="font-family:'Open Sans',sans-serif;"
                                                    role="presentation" cellpadding="0" cellspacing="0" width="100%"
                                                    border="0">
                                                    <tbody>
                                                        <tr>
                                                            <td class="v-container-padding-padding"
                                                                style="overflow-wrap:break-word;word-break:break-word;padding:25px 10px 50px;font-family:'Open Sans',sans-serif;"
                                                                align="left">
                                                                <h1 class="v-font-size"
                                                                    style="margin: 0px; color: #ffffff; line-height: 140%; text-align: center; word-wrap: break-word; font-size: 22px;">
                                                                    <strong>Criação da conta</strong></h1>
                                                            </td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="u-row-container" style="padding: 0px;background-color: transparent">
                            <div class="u-row"
                                style="Margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;">
                                <div
                                    style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">
                                    <div class="u-col u-col-100"
                                        style="max-width: 320px;min-width: 600px;display: table-cell;vertical-align: top;">
                                        <div
                                            style="background-color: #ffffff;height: 100%;width: 100% !important;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
                                            <div
                                                style="box-sizing: border-box; height: 100%; padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
                                                <table id="u_content_text_deprecated_7"
                                                    style="font-family:'Open Sans',sans-serif;" role="presentation"
                                                    cellpadding="0" cellspacing="0" width="100%" border="0">
                                                    <tbody>
                                                        <tr>
                                                            <td class="v-container-padding-padding"
                                                                style="overflow-wrap:break-word;word-break:break-word;padding:50px 50px 0px;font-family:'Open Sans',sans-serif;"
                                                                align="left">
                                                                <div class="v-font-size"
                                                                    style="font-size: 15px; line-height: 140%; text-align: justify; word-wrap: break-word;">
                                                                    <p style="line-height: 140%; font-size: 14px;"><span
                                                                            style="font-family: 'Open Sans', sans-serif; font-size: 16px; line-height: 21px;"><strong>Olá,
                                                                                {name}</strong></span></p>
                                                                    <p style="line-height: 140%;">&nbsp;</p>
                                                                    <p style="line-height: 140%;">Estamos te enviando esse
                                                                        email para avisar que a sua ação {action}
                                                                        está sendo anulada,
                                                                        qualquer dúvida entre em contato conosco!</p>
                                                                    <p style="line-height: 140%;">&nbsp;</p>
                                                                </div>
                                                            </td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                                <table id="u_content_text_deprecated_8"
                                                    style="font-family:'Open Sans',sans-serif;" role="presentation"
                                                    cellpadding="0" cellspacing="0" width="100%" border="0">
                                                    <tbody>
                                                        <tr>
                                                            <td class="v-container-padding-padding"
                                                                style="overflow-wrap:break-word;word-break:break-word;padding:15px 10px 50px 50px;font-family:'Open Sans',sans-serif;"
                                                                align="left">
                                                                <div class="v-font-size"
                                                                    style="line-height: 160%; text-align: left; word-wrap: break-word;">
                                                                    <p style="font-size: 14px; line-height: 160%;">
                                                                        Atenciosamente,</p>
                                                                    <p style="font-size: 14px; line-height: 160%;">&nbsp;
                                                                    </p>
                                                                    <p style="font-size: 14px; line-height: 160%;">
                                                                        <strong>Equipe Portal Interno ;)</strong></p>
                                                                </div>
                                                            </td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="u-row-container" style="padding: 0px;background-color: transparent">
                            <div class="u-row"
                                style="Margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;">
                                <div
                                    style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">
                                    <div class="u-col u-col-100"
                                        style="max-width: 320px;min-width: 600px;display: table-cell;vertical-align: top;">
                                        <div
                                            style="height: 100%;width: 100% !important;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
                                            <div
                                                style="box-sizing: border-box; height: 100%; padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
                                                <table id="u_content_text_deprecated_9"
                                                    style="font-family:'Open Sans',sans-serif;" role="presentation"
                                                    cellpadding="0" cellspacing="0" width="100%" border="0">
                                                    <tbody>
                                                        <tr>
                                                            <td class="v-container-padding-padding"
                                                                style="overflow-wrap:break-word;word-break:break-word;padding:10px 100px 20px;font-family:'Open Sans',sans-serif;"
                                                                align="left">
                                                                <div class="v-font-size"
                                                                    style="line-height: 170%; text-align: center; word-wrap: break-word;">
                                                                    <p style="line-height: 170%;">Dev Community</p>
                                                                </div>
                                                            </td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                                <table style="font-family:'Open Sans',sans-serif;" role="presentation"
                                                    cellpadding="0" cellspacing="0" width="100%" border="0">
                                                    <tbody>
                                                        <tr>
                                                            <td class="v-container-padding-padding"
                                                                style="overflow-wrap:break-word;word-break:break-word;padding:0px;font-family:'Open Sans',sans-serif;"
                                                                align="left">
                                                                <table height="0px" align="center" border="0"
                                                                    cellpadding="0" cellspacing="0" width="100%"
                                                                    style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;border-top: 1px solid #BBBBBB;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
                                                                    <tbody>
                                                                        <tr style="vertical-align: top">
                                                                            <td
                                                                                style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;font-size: 0px;line-height: 0px;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
                                                                                <span>&nbsp;</span></td>
                                                                        </tr>
                                                                    </tbody>
                                                                </table>
                                                            </td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </td>
                </tr>
            </tbody>
        </table>
    </body>

    </html>

"""

    message = message.format(name=name, action=action)

    return message