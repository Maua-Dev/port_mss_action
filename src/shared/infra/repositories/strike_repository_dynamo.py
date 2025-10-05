
from typing import List, Optional
from src.shared.domain.entities.member import Member
from src.shared.domain.entities.strike import Strike
from src.shared.domain.repositories.strike_repository_interface import IStrikeRepository
from src.shared.environments import Environments
from src.shared.infra.dto.strike_dynamo_dto import StrikeDynamoDTO
from src.shared.infra.external.dynamo.datasources.dynamo_datasource import DynamoDatasource


class StrikeRepositoryDynamo(IStrikeRepository):
    @staticmethod
    def strike_partition_key_format(target_user_id: str) -> str:
        return f'target#{target_user_id}'
    
    @staticmethod
    def strike_sort_key_format(occurred_date: int, strike_id: str) -> int:
        return f'{occurred_date}#strike{strike_id}'
    
    @staticmethod
    def gsi_strike_partition_key_format(strike_id: str) -> str:
        return f'{strike_id}'
    
    def __init__(self):
        self.dynamo= DynamoDatasource(
            endpoint_url=Environments.get_envs().endpoint_url,
            dynamo_table_name=Environments.get_envs().dynamo_table_name_strike,
            region=Environments.get_envs().region,
            partition_key=Environments.get_envs().dynamo_partition_key,
            sort_key=Environments.get_envs().dynamo_sort_key,
            gsi_partition_key= Environments.get_envs().dynamo_gsi_strike_partition_key
        )

    def create_strike(self, strike: Strike) -> Strike:
        item= StrikeDynamoDTO.from_entity(strike).to_dynamo()

        # aqui entendo que com essa GSI posso fazer querryes por somente pelo strike_id (caso nao saiba o target_user_id), nao basta ele como SK
        item['GSI-STRIKE-PK']= self.gsi_strike_partition_key_format(strike.strike_id)

        resp= self.dynamo.put_item(item=item, partition_key=self.strike_partition_key_format(strike.target_user_id), sort_key=self.strike_sort_key_format(strike.occurred_date, strike.strike_id))
        
        return strike

    def get_all(self) -> list[Strike]:
        pass
    
    def find_by_id(self, strike_id: str) -> Optional[Strike]:
        pass

    def delete_strike(self, strike_id: str) -> Optional[Strike]:
        pass

    def get_strike_by_target_id(self, target_user_id: str) -> Optional[List[Strike]]:
        pass