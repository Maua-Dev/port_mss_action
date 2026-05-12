from src.shared.helpers.errors.usecase_errors import UnconfirmedUserError, DataIngestionError
from src.shared.helpers.errors.usecase_errors import DuplicatedItem
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.controller_errors import WrongTypeParameter
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.external_interfaces.external_interface import IResponse
from .bedrock_ingestion_usecase import BedrockIngestionUseCase
from src.shared.helpers.external_interfaces.http_codes import OK, NotFound, BadRequest, InternalServerError, Conflict, ServiceUnavailable

class BedrockIngestionController:

    def __init__(self, usecase: BedrockIngestionUseCase):
        self.BedrockIngestionUseCase = usecase

    def __call__(self, request: dict) -> IResponse:
        try:
            detail= request.get("detail")

            bucket_name= detail.get("bucket", {}).get("name")

            object_key= detail.get("object", {}).get("key")

            if not bucket_name or not object_key:
                raise MissingParameters('bucket name ou object key')

            result= self.BedrockIngestionUseCase(
                bucket_name, 
                object_key
            )

            viewmodel= {
                'data': result,
                'message': 'Bedrock ingestion started successfully'
            }
            

            response= OK(viewmodel)

            return response

        except NoItemsFound as err:
            return NotFound(body=err.message)

        except MissingParameters as err:
            return BadRequest(body=err.message)

        except WrongTypeParameter as err:
            return BadRequest(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)

        except (DuplicatedItem, UnconfirmedUserError) as err:
            return Conflict(body=err.message)

        except DataIngestionError as err:
            return ServiceUnavailable(body=err.message)

        except Exception as err:
            return InternalServerError(body=str(err))