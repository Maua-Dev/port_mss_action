from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, InternalServerError, NotFound
from .get_all_members_viewmodel import GetAllMembersViewmodel
from .get_all_members_usecase import GetAllMembersUsecase
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
class GetAllMembersController:
    def __init__(self, usecase: GetAllMembersUsecase):
        self.usecase = usecase
        self.memberrepo = MemberRepositoryMock()
        self.actionrepo = ActionRepositoryMock()
    def __call__(self, request: IRequest) -> IResponse:
        try:

            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')
            requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user'))

            start_date = request.data.get('start_date')
            if start_date is None:
                raise MissingParameters('start_date')
            if type(start_date) is not int:
                raise WrongTypeParameter(fieldName='start_date', fieldTypeExpected='int', fieldTypeReceived=type(start_date))
            
            end_date = request.data.get('end_date')
            if end_date is None:
                raise MissingParameters('end_date')
            if type(end_date) is not int:
                raise WrongTypeParameter(fieldName='end_date', fieldTypeExpected='int', fieldTypeReceived=type(end_date))
            
            members = self.usecase(requester_user.user_id, start_date, end_date)
            
            viewmodel = GetAllMembersViewmodel(members)
            return OK(viewmodel.to_dict())
          
        except MissingParameters as err:
            return BadRequest(body=err.message)
        
        except EntityError as err:
            return BadRequest(body=err.message)
        
        except NoItemsFound as err:
            return NotFound(body=err.message)
        
        except Exception as err:
            return InternalServerError(body=err.args[0])