from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, UnregisteredUser, UserIsNotFromAdmin, UserNotAllowed
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, Forbidden, InternalServerError, NotFound
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO
from src.shared.domain.entities.member import Member

from .get_hours_chart_usecase import GetHoursChartUsecase
from .get_hours_chart_viewmodel import GetHoursChartViewmodel


class GetHoursChartController:
    def __init__(self, usecase: GetHoursChartUsecase):
        self.usecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')

            requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user'))

            if type(requester_user.user_id) is not str:
                raise WrongTypeParameter(fieldName='user_id', fieldTypeExpected='str', fieldTypeReceived=type(requester_user.user_id))
            if not Member.validate_user_id(requester_user.user_id):
                raise EntityError('user_id')

            if request.data.get('start_date') is not None:
                raw_start_date = request.data.get('start_date')
                if type(raw_start_date) is str and raw_start_date.isdigit():
                    raw_start_date = int(raw_start_date)
                if type(raw_start_date) is not int:
                    raise WrongTypeParameter(fieldName='start_date', fieldTypeExpected='int', fieldTypeReceived=type(request.data.get('start_date')))
                if not 1000000000000 < raw_start_date < 10000000000000:
                    raise EntityError('start_date')
                start_date = raw_start_date
            else:
                start_date = None

            if request.data.get('end_date') is not None:
                raw_end_date = request.data.get('end_date')
                if type(raw_end_date) is str and raw_end_date.isdigit():
                    raw_end_date = int(raw_end_date)
                if type(raw_end_date) is not int:
                    raise WrongTypeParameter(fieldName='end_date', fieldTypeExpected='int', fieldTypeReceived=type(request.data.get('end_date')))
                if not 1000000000000 < raw_end_date < 10000000000000:
                    raise EntityError('end_date')
                end_date = raw_end_date
            else:
                end_date = None

            if start_date is not None and end_date is not None:
                if start_date > end_date:
                    raise EntityError('start_date')

            projects, hours_by_project, hours_by_project_and_stack = self.usecase(user_id=requester_user.user_id, start_date=start_date, end_date=end_date)

            viewmodel = GetHoursChartViewmodel(projects=projects, hours_by_project=hours_by_project, hours_by_project_and_stack=hours_by_project_and_stack)
            return OK(viewmodel.to_dict())

        except MissingParameters as err:
            return BadRequest(body=err.message)

        except WrongTypeParameter as err:
            return BadRequest(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)

        except UnregisteredUser as err:
            return NotFound(body=err.message)

        except UserNotAllowed as err:
            return BadRequest(body=err.message)

        except UserIsNotFromAdmin as err:
            return Forbidden(body=err.message)

        except ForbiddenAction as err:
            return Forbidden(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])