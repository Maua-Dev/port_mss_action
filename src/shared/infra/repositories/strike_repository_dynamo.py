
from src.shared.domain.entities.member import Member
from src.shared.domain.entities.strike import Strike
from src.shared.domain.repositories.strike_repository_interface import IStrikeRepository
from src.shared.environments import Environments
from src.shared.infra.external.dynamo.datasources.dynamo_datasource import DynamoDatasource


class StrikeRepositoryDynamo(IStrikeRepository):
    @staticmethod
    def strike_partition_key_format(strike_id: str) -> str:
        return f'{strike_id}'
    
    @staticmethod
    def strike_sort_key_format(action_id: str) -> str:
        return f'action#{action_id}'
    
    @staticmethod
    def owner_partition_key_format(owner_user: Member) -> str:
        return f'{owner_user}'
    
    @staticmethod
    def owner_sort_key_format(owner_user_id: str) -> str:
        return f'owner#{owner_user_id}'
    
    @staticmethod
    def target_partition_key_format(target_user: Member) -> str:
        return f'{target_user}'
    
    @staticmethod
    def target_sort_key_format(target_user_id: str) -> str:
        return f'target#{target_user_id}'

    @staticmethod
    def applier_partition_key_format(applier_user: Member) -> str:
        return f'{applier_user}'
    
    @staticmethod
    def target_sort_key_format(applier_user_id: str) -> str:
        return f'applier#{applier_user_id}'
    
    def __init__(self):
        self.dynamo= DynamoDatasource(
            endpoint_url=Environments.get_envs().endpoint_url,
            dynamo_table_name=Environments.get_envs().dynamo_table_name_member,
            region=Environments.get_envs().region,
            partition_key=Environments.get_envs().dynamo_partition_key,
            sort_key=Environments.get_envs().dynamo_gsi_1_sort_key
        )

    def create_strike(self, strike: Strike) -> Strike:
        item= StikeDynamoDTO
