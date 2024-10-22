from src.shared.helpers.external_interfaces.http_codes import OK, InternalServerError
from .get_all_projects_viewmodel import GetAllProjectsViewmodel
from .get_all_projects_usecase import GetAllProjectsUsecase
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO


class GetAllProjectsController:
    def __init__(self, usecase: GetAllProjectsUsecase):
        self.usecase = usecase
    
    def __call__(self, request: IRequest) -> IResponse:
        try:

            start_date = request.data.get('start_date')
            if start_date is not None:
                if type(start_date) is not int:
                    raise WrongTypeParameter(fieldName='start_date', fieldTypeExpected='int', fieldTypeReceived=type(start_date))
            
            end_date = request.data.get('end_date')
            if end_date is not None:
                if type(end_date) is not int:
                    raise WrongTypeParameter(fieldName='end_date', fieldTypeExpected='int', fieldTypeReceived=type(end_date))
            
            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')

            requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user'))

            projects = self.usecase(user_id=requester_user.user_id, start_date=start_date, end_date=end_date)
            viewmodel = GetAllProjectsViewmodel(projects)
            return OK(viewmodel.to_dict())
    
        
        except Exception as err:
            return InternalServerError(body=err.args[0])