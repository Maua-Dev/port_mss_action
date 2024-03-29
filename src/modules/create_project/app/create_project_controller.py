from .create_project_usecase import CreateProjectUsecase
from .create_project_viewmodel import CreateProjectViewmodel
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import DuplicatedItem
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import BadRequest, Created, InternalServerError
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO


class CreateProjectController:

    def __init__(self, usecase: CreateProjectUsecase):
        self.usecase = usecase
        
    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')
            
            requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user'))

            if request.data.get('code') is None:
                raise MissingParameters('code')
            if request.data.get('name') is None:
                raise MissingParameters('name')
            if request.data.get('description') is None:
                raise MissingParameters('description')
            if request.data.get('po_user_id') is None:
                raise MissingParameters('po_user_id')
            if request.data.get('scrum_user_id') is None:
                raise MissingParameters('scrum_user_id')
            if request.data.get('start_date') is None:
                raise MissingParameters('start_date')
            if request.data.get('members_user_ids') is None:
                raise MissingParameters('members_user_ids')
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
                po_user_id=request.data.get('po_user_id'),
                scrum_user_id=request.data.get('scrum_user_id'),
                start_date=request.data.get('start_date'),
                members_user_ids=request.data.get('members_user_ids'),
                photos=request.data.get('photos'),
                user_id=requester_user.user_id
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