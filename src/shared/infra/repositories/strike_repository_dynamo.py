from typing import List, Optional
from src.shared.domain.entities.strike import Strike
from src.shared.domain.repositories.strike_repository_interface import IStrikeRepository
from src.shared.environments import Environments
from src.shared.infra.dto.strike_dynamo_dto import StrikeDynamoDTO
from src.shared.infra.external.dynamo.datasources.dynamo_datasource import DynamoDatasource


class StrikeRepositoryDynamo(IStrikeRepository):
    @staticmethod
    def strike_partition_key_format(strike_id: str) -> str:
        return f'strike#{strike_id}'
    
    @staticmethod
    def gsi_strike_partition_key_format(target_id: str) -> str:
        return f'target#{target_id}'
    
    @staticmethod
    def gsi_strike_sort_key_format(occurred_date: int) -> int:
        return occurred_date
    
    def __init__(self):
        self.dynamo = DynamoDatasource(
            endpoint_url=Environments.get_envs().endpoint_url,
            dynamo_table_name=Environments.get_envs().dynamo_table_name_strike,
            region=Environments.get_envs().region,
            partition_key=Environments.get_envs().dynamo_partition_key,
            sort_key=Environments.get_envs().dynamo_sort_key,
            gsi_partition_key=Environments.get_envs().dynamo_gsi_strike_partition_key
        )

    def create_strike(self, strike: Strike) -> Strike:
        item = StrikeDynamoDTO.from_entity(strike).to_dynamo()

        item['GSI-TARGET-PK'] = self.gsi_strike_partition_key_format(strike.target_user_id)
        item['GSI-TARGET-SK'] = self.gsi_strike_sort_key_format(occurred_date=strike.occurred_date)

        resp = self.dynamo.put_item(
            item=item, 
            partition_key=self.strike_partition_key_format(strike.strike_id),
            sort_key=strike.applier_user_id  # Assumindo que SK é o applier_user_id
        )
        
        return strike

    def get_all(self) -> List[Strike]:
        # Implementar scan se necessário
        pass
    
    def find_by_id(self, strike_id: str) -> Optional[Strike]:
        response = self.dynamo.query(
            key_condition_expression='PK = :pk',
            ExpressionAttributeValues={':pk': self.strike_partition_key_format(strike_id)},
            Limit=1
        )
        
        items = response.get('Items', [])
        if not items:
            return None
        
        strike_dto = StrikeDynamoDTO.from_dynamo(items[0])
        return strike_dto.to_entity()

    def delete_strike(self, strike_id: str) -> Optional[Strike]:
        pass

    def get_strike_by_target_id(self, target_user_id: str) -> Optional[List[Strike]]:
        response = self.dynamo.query(
            key_condition_expression='#gsi_pk = :target_id',
            ExpressionAttributeNames={'#gsi_pk': 'GSI-TARGET-PK'},
            ExpressionAttributeValues={':target_id': self.gsi_strike_partition_key_format(target_user_id)},
            IndexName='GSI-TARGET'  
        )
        
        items = response.get('Items', [])
        if not items:
            return None
        
        strikes = [StrikeDynamoDTO.from_dynamo(item).to_entity() for item in items]
        return strikes