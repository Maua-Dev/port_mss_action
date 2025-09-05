from src.modules.auth_sign_up.app.auth_sign_up_usecase import AuthSignUpUsecase
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.external_interfaces.http_codes import Created, BadRequest, InternalServerError
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse

class AuthSignUpController:
    def __init__(self, usecase: "AuthSignUpUsecase"):
        self.usecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            body = request.body or request.data.get("body") or {}
            email = body.get("email")
            password = body.get("password")
            name = body.get("name")

            if not email or not password:
                raise MissingParameters("email, password")

            result = self.usecase(email=email, password=password, name=name)
            return Created(result)

        except MissingParameters as e:
            return BadRequest({"error": "MissingParameters", "message": str(e)})

        except Exception as e:
            return InternalServerError({"error": "InternalServerError", "message": str(e)})
