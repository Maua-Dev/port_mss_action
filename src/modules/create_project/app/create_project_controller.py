from .create_project_usecase import CreateProjectUsecase
from .create_project_viewmodel import CreateProjectViewmodel
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import DuplicatedItem
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import BadRequest, Created, InternalServerError


class CreateProjectController:

    def __init__(self, usecase: CreateProjectUsecase):
        self.usecase = usecase
        
    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('code') is None:
                raise MissingParameters('code')
            if request.data.get('name') is None:
                raise MissingParameters('name')
            if request.data.get('description') is None:
                raise MissingParameters('description')
            if request.data.get('po_RA') is None:
                raise MissingParameters('po_RA')
            if request.data.get('scrum_RA') is None:
                raise MissingParameters('scrum_RA')
            if request.data.get('start_date') is None:
                raise MissingParameters('start_date')
            if request.data.get('photos') is not None:
                if type(request.data.get('photos')) is not list:
                    raise EntityError('photos')
                for value in request.data.get('photos'):
                    if type(value) is not str:
                        raise EntityError('photos')
            
            project = self.usecase(
                code=request.data.get('code'),
                name=request.data.get('name'),
                description=request.data.get('description'),
                po_RA=request.data.get('po_RA'),
                scrum_RA=request.data.get('scrum_RA'),
                start_date=request.data.get('start_date'),
                photos=request.data.get('photos')
            )
            
            return Created(CreateProjectViewmodel(project).to_dict())
        
        except MissingParameters as err:
            return BadRequest(body=err.message)

        except DuplicatedItem as err:
            return BadRequest(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)
        
        except Exception as err:
            return InternalServerError(body=err.args[0])