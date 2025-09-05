from src.auth_resend.app.auth_resend_usecase import AuthResendUsecase
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, InternalServerError
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse

class AuthResendController:
    def __init__(self, usecase: "AuthResendUsecase"):
        self.usecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            body = request.body or request.data.get("body") or {}
            email = body.get("email")
            if not email:
                raise MissingParameters("email")

            result = self.usecase(email=email)
            return OK(result)

        except MissingParameters as e:
            return BadRequest({"error": "MissingParameters", "message": str(e)})
        except Exception as e:
            return InternalServerError({"error": "InternalServerError", "message": str(e)})
