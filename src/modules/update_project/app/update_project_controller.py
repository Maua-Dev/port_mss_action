from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, NotFound, BadRequest, InternalServerError
from .update_project_viewmodel import UpdateProjectViewmodel
from .update_project_usecase import UpdateProjectUsecase

class UpdateProjectController:
    def __init__(self, usecase: UpdateProjectUsecase) -> None:
        self.UpdateProjectUsecase = usecase


    def __call__(self, request: IRequest) -> IResponse:
        try:
            if not request.data.get('code'):
                raise MissingParameters('code')
            
            if request.data.get('new_name') is None:
                raise MissingParameters('new_name')
            
            if request.data.get('new_description') is None:
                raise MissingParameters('new_description')
            
            if request.data.get('new_po_RA') is None:
                raise MissingParameters('new_po_RA')
            
            if request.data.get('new_scrum_RA') is None:
                raise MissingParameters('new_scrum_RA')
            
            if request.data.get('new_photos') is None:
                raise MissingParameters('new_photos')
            

            update_project = self.UpdateProjectUsecase(
                code = request.data.get('code'),
                new_name = request.data.get('new_name'),
                new_description = request.data.get('new_description'),
                new_po_RA = request.data.get('new_po_RA'),
                new_scrum_RA = request.data.get('new_scrum_RA'),
                new_photos = request.data.get('new_photos')
            )

            viewmodel = UpdateProjectViewmodel(update_project)

            response = OK(viewmodel.to_dict())

            return response

        except NoItemsFound as err:
            return NotFound(body=err.message)
        
        except MissingParameters as err:
            return BadRequest(body=err.message)
        
        except EntityError as err:
            return BadRequest(body=err.message)
        
        except Exception as err:
            return InternalServerError(body=err.message)


