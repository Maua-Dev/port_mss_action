from src.modules.auth_sign_in.app.auth_sign_in_usecase import AuthSignInUsecase
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, Unauthorized, InternalServerError
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse

class AuthSignInController:
    def __init__(self, usecase: "AuthSignInUsecase"):
        self.usecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            body = request.body or request.data.get("body") or {}
            email = body.get("email")
            password = body.get("password")
            if not email or not password:
                raise MissingParameters("email, password")

            result = self.usecase(email=email, password=password)
            if result.get("error") == "UserNotConfirmed":
                return Unauthorized(result)
            if result.get("error") == "NotAuthorized":
                return Unauthorized(result)

            return OK(result)

        except MissingParameters as e:
            return BadRequest({"error": "MissingParameters", "message": str(e)})
        except Exception as e:
            return InternalServerError({"error": "InternalServerError", "message": str(e)})
