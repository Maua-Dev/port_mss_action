from .delete_member_usecase import DeleteMemberUseCase
from .delete_member_viewmodel import DeleteMemberViewModel
from src.shared.domain.entities.member import Member
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, InternalServerError, NotFound


class DeleteMemberController:
    
    def __init__(self, usecase:  DeleteMemberUseCase):
        self.usecase = usecase
        
    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('ra') is None:
                raise MissingParameters('ra')
            if not Member.validate_ra(request.data.get('ra')):
                raise EntityError('ra')
            
            member = self.usecase(ra=request.data.get('ra'))
            viewmodel = DeleteMemberViewModel(member)
            
            return OK(viewmodel.to_dict())
        
        except MissingParameters as err:
            return BadRequest(body=err.message)
        
        except NoItemsFound as err:
            return NotFound(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)
        
        except Exception as err:
            return InternalServerError(body=err.args[0])