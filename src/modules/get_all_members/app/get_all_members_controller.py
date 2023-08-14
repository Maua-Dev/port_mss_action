from src.shared.helpers.external_interfaces.http_codes import OK, InternalServerError
from .get_all_members_viewmodel import GetAllMembersViewmodel
from .get_all_members_usecase import GetAllMembersUsecase
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse

class GetAllMembersController:
    def __init__(self, usecase: GetAllMembersUsecase):
        self.usecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            members = self.usecase()
            viewmodel = GetAllMembersViewmodel(members)
            return OK(viewmodel.to_dict())
        
        except Exception as err:
            return InternalServerError(body=err.args[0])