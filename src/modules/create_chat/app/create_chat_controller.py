from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.usecase_errors import BedrockIntegrationError, ForbiddenAction
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, InternalServerError, Forbidden, ServiceUnavailable
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO
from .create_chat_usecase import CreateChatUsecase
from .create_chat_viewmodel import CreateChatViewmodel

class CreateChatController:
    def __init__(self, usecase: CreateChatUsecase):
        self.usecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')

            requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user'))

            if type(requester_user.user_id) is not str:
                raise WrongTypeParameter(fieldName='user_id', fieldTypeExpected='str', fieldTypeReceived=type(requester_user.user_id))

            question = request.data.get('question')

            if question is None:
                raise MissingParameters('question')

            if type(question) is not str:
                raise WrongTypeParameter(fieldName='question', fieldTypeExpected='str', fieldTypeReceived=type(question))

            answer = self.usecase(question=question)

            viewmodel = CreateChatViewmodel(answer=answer)

            return OK(viewmodel.to_dict())

        except MissingParameters as err:
            return BadRequest(body=err.message)

        except WrongTypeParameter as err:
            return BadRequest(body=err.message)

        except BedrockIntegrationError as err:
            return ServiceUnavailable(body=err.message)

        except ForbiddenAction as err:
            return Forbidden(body=err.message)

        except Exception as err:
            return InternalServerError(body=str(err))
