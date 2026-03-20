from .create_strike_viewmodel import CreateStrikeViewmodel
from .create_strike_usecase import CreateStrikeUsecase
from src.shared.domain.entities.strike import Strike
from src.shared.domain.enums.strike_category import STRIKE_CATEGORY
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import DuplicatedItem, UnregisteredUser
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import BadRequest, Created, InternalServerError
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO


class CreateStrikeController:
    def __init__(self, usecase: CreateStrikeUsecase):
        self.usecase = usecase
        
    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')
            
            requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user'))
            
            if request.data.get('owner_user_id') is None:
                raise MissingParameters('owner_user_id')
            
            if request.data.get('target_user_id') is None:
                raise MissingParameters('target_user_id')
            
            if request.data.get('occurred_date') is None:
                raise MissingParameters('occurred_date')
            
            if request.data.get('category') is None:
                raise MissingParameters('category')
            
            if type(request.data.get('owner_user_id')) != str:
                raise WrongTypeParameter(
                    fieldName="owner_user_id",
                    fieldTypeExpected="str",
                    fieldTypeReceived=request.data.get('owner_user_id').__class__.__name__
                )
                
            
            if type(request.data.get('target_user_id')) != str:
                raise WrongTypeParameter(
                    fieldName="target_user_id",
                    fieldTypeExpected="str",
                    fieldTypeReceived=request.data.get('target_user_id').__class__.__name__
                )
            
            category_tag_str= request.data.get('category')

            if  category_tag_str not in [category.value for category in STRIKE_CATEGORY]:
                raise EntityError('category')
            
            category_type_tag= STRIKE_CATEGORY[category_tag_str]
            
            if request.data.get('description') is not None:
                if type(request.data.get('description')) != str:
                    raise WrongTypeParameter(
                        fieldName="description",
                        fieldTypeExpected="str",
                        fieldTypeReceived=request.data.get('description').__class__.__name__
                    )
                
            
                description= request.data.get('description')
            else:
                description= None

            strike= self.usecase(
                owner_user_id= request.data.get('owner_user_id'),
                target_user_id= request.data.get('target_user_id'),
                applier_user_id= requester_user.user_id,
                occurred_date= request.data.get('occurred_date'),
                category= category_type_tag,
                description= description
            )

            viewmodel= CreateStrikeViewmodel(strike=strike[0], case_number=strike[1])
        
            return Created(viewmodel.to_dict())
        
        except WrongTypeParameter as err:
            return BadRequest(body=err.message)
        
        except MissingParameters as err:
            return BadRequest(body=err.message)

        except DuplicatedItem as err:
            return BadRequest(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)
        
        except UnregisteredUser as err:
            return BadRequest(body=err.message)
        
        except Exception as err:
            return InternalServerError(body=err.args[0])
        
