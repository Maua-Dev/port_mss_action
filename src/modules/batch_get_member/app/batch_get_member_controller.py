from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO
from .batch_get_member_usecase import BatchGetMemberUsecase
from .batch_get_member_viewmodel import BatchGetMemberViewmodel
from src.shared.domain.entities.member import Member
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound, UnregisteredUser
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, Forbidden, InternalServerError, NotFound


class BatchGetMemberController:
    def __init__(self, usecase: BatchGetMemberUsecase):
        self.usecase = usecase
        
    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')
            
            user_id = request.data.get('user_ids')
            
            requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user'))
            
            for user_id in request.data.get('user_ids'):
                if user_id is None:
                    raise MissingParameters('user_id')
                if type(user_id) != str:
                    raise WrongTypeParameter(fieldName='user_id', fieldTypeExpected='str', fieldTypeReceived=type(user_id))
                if not Member.validate_user_id(user_id):
                    raise EntityError('user_id')
        
            members = self.usecase(user_id=requester_user.user_id, user_ids=request.data.get('user_ids'))
            viewmodel = BatchGetMemberViewmodel(members=members)

            return OK(viewmodel.to_dict())
            
        except NoItemsFound as err:
            return NotFound(body=err.message)
        
        except MissingParameters as err:
            return BadRequest(body=err.message)
        
        except EntityError as err:
            return BadRequest(body=err.message)
        
        except WrongTypeParameter as err:
            return BadRequest(body=err.message)
        
        except UnregisteredUser as err:
            return Forbidden(body=err.message)
        
        except Exception as err:
            return InternalServerError(body=err.args[0])