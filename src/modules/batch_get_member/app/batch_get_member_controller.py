from src.modules.batch_get_member.app.batch_get_member_usecase import BatchGetMemberUsecase
from src.modules.batch_get_member.app.batch_get_member_viewmodel import BatchGetMemberViewmodel
from src.shared.domain.entities.member import Member
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, InternalServerError, NotFound


class BatchGetMemberController:
    def __init__(self, usecase: BatchGetMemberUsecase):
        self.usecase = usecase
        
    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('ras') is None:
                raise MissingParameters('ras')
            
            for ra in request.data.get('ras'):
                if type(ra) != str:
                    raise WrongTypeParameter(fieldName='ra', fieldTypeExpected='str', fieldTypeReceived=type(ra))
                if not Member.validate_ra(ra):
                    raise EntityError('ra')
            
            members = self.usecase(ras=request.data.get('ras'))
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
        
        except Exception as err:
            return InternalServerError(body=err.args[0])