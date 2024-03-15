from src.shared.domain.entities.project import Project
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
            code = request.data.get('code')
            new_name = request.data.get('new_name')
            new_description = request.data.get('new_description')
            new_po_user_id = request.data.get('new_po_user_id')
            new_scrum_user_id = request.data.get('new_scrum_user_id')
            new_photos = request.data.get('new_photos')

            if code is None:
                raise MissingParameters('code')
            
            if not Project.validate_project_code(code):
                raise EntityError("code")
                    
            if new_name is not None and type(new_name) != str:
                raise EntityError("name")
            
            if new_description is not None and type(new_description) != str:
                raise EntityError("description")
            
            if new_po_user_id is not None and not Project.validate_RA(new_po_user_id):
                raise EntityError("po_user_id")
            
            if new_scrum_user_id is not None and not Project.validate_RA(new_scrum_user_id):
                raise EntityError("scrum_user_id")
            
            if new_photos is not None and type(new_photos) != list:
                raise EntityError("photos")
            
            if new_photos != None:
                if not all(type(photo) == str for photo in new_photos):
                    raise EntityError("photos")
            
            update_project = self.UpdateProjectUsecase(
                code=code,
                new_name=new_name,
                new_description=new_description,
                new_po_user_id=new_po_user_id,
                new_scrum_user_id=new_scrum_user_id,
                new_photos=new_photos
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


