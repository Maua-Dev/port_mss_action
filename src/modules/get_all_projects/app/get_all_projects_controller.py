from src.shared.helpers.external_interfaces.http_codes import OK, InternalServerError
from .get_all_projects_viewmodel import GetAllProjectsViewmodel
from .get_all_projects_usecase import GetAllProjectsUsecase
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse


class GetAllProjectsController:
    def __init__(self, usecase: GetAllProjectsUsecase):
        self.usecase = usecase
    
    def __call__(self, request: IRequest) -> IResponse:
        try:
            projects = self.usecase()
            viewmodel = GetAllProjectsViewmodel(projects)
            return OK(viewmodel.to_dict())
        
        except Exception as err:
            return InternalServerError(body=err.args[0])