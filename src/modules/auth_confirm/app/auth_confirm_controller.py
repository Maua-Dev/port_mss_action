from src.modules.auth_confirm.app.auth_confirm_usecase import AuthConfirmUsecase
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, InternalServerError
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse

class AuthConfirmController:
    def __init__(self, usecase: "AuthConfirmUsecase"):
        self.usecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            body = request.body or request.data.get("body") or {}
            email = body.get("email")
            code = body.get("code")
            if not email or not code:
                raise MissingParameters("email, code")

            result = self.usecase(email=email, code=code)
            return OK(result)

        except MissingParameters as e:
            return BadRequest({"error": "MissingParameters", "message": str(e)})

        except Exception as e:
            return InternalServerError({"error": "InternalServerError", "message": str(e)})
