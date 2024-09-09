import os
from typing import List, Optional
from src.shared.domain.repositories.member_repository_interface import IMemberRepository
from src.shared.domain.entities.member import Member
from src.shared.infra.dto.member_dynamo_dto import MemberDynamoDTO
from src.shared.environments import Environments
from src.shared.infra.external.dynamo.datasources.dynamo_datasource import DynamoDatasource
from boto3.dynamodb.conditions import Key
from src.shared.domain.enums.active_enum import ACTIVE
from src.shared.domain.enums.course_enum import COURSE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.enums.stack_enum import STACK
from src.shared.helpers.utils.compose_member_active_email import compose_member_active_email
import boto3


class MemberRepositoryDynamo(IMemberRepository):
    @staticmethod
    def member_partition_key_format(member: Member) -> str:
        return f'member'
    
    @staticmethod
    def member_sort_key_format(user_id: str) -> str:
        return f'member#{user_id}'
    
    def __init__(self):
        self.dynamo = DynamoDatasource(
            endpoint_url=Environments.get_envs().endpoint_url,
            dynamo_table_name=Environments.get_envs().dynamo_table_name_member,
            region=Environments.get_envs().region,
            partition_key=Environments.get_envs().dynamo_partition_key,
            sort_key=Environments.get_envs().dynamo_sort_key,
        )
        
    def create_member(self, member: Member) -> Member:
        item = MemberDynamoDTO.from_entity(member).to_dynamo()
        resp = self.dynamo.put_item(item=item, partition_key=self.member_partition_key_format(member), sort_key=self.member_sort_key_format(member.user_id), is_decimal=True)
        
        return member
    
    def get_all_members(self) -> List[Member]:
        query_string = Key(self.dynamo.partition_key).eq("member")
        resp = self.dynamo.query(key_condition_expression=query_string, Select='ALL_ATTRIBUTES')

        members = []
        for item in resp.get("Items"):
            if item.get("entity") == "member":
                members.append(MemberDynamoDTO.from_dynamo(item).to_entity())

        return members

    def get_member(self, user_id: str) -> Member:
        member = self.dynamo.get_item(partition_key=self.member_partition_key_format(user_id), sort_key=self.member_sort_key_format(user_id))

        if "Item" not in member:
            return None

        member_dto = MemberDynamoDTO.from_dynamo(member['Item'])
        return member_dto.to_entity()
    
    def batch_get_member(self, user_ids: List[str]) -> List[Member]:
        keys = [{self.dynamo.partition_key: self.member_partition_key_format(user_id), self.dynamo.sort_key: self.member_sort_key_format(user_id)} for user_id in user_ids]

        resp = self.dynamo.batch_get_items(keys=keys)

        members = []
        for item in resp.get("Responses", { }).get(self.dynamo.dynamo_table.name,[]):
            if item.get("entity") == "member":
                members.append(MemberDynamoDTO.from_dynamo(item).to_entity())
        
        return members

    def delete_member(self, user_id: str) -> Optional[Member]:
        delete_member = self.dynamo.delete_item(partition_key=self.member_partition_key_format(user_id), sort_key=self.member_sort_key_format(user_id))
        
        if "Attributes" not in delete_member:
            return None
        
        return MemberDynamoDTO.from_dynamo(delete_member["Attributes"]).to_entity()
    
    def update_member(self, user_id: str, new_name: Optional[str] = None, new_email_dev: Optional[str] = None, new_role: Optional[str] = None, new_stack: Optional[str] = None, new_year: Optional[int] = None, new_cellphone: Optional[str] = None, new_course: Optional[str] = None, new_active: Optional[str] = None, new_deactivated_date: Optional[int] = None) -> Member:
        member_to_update = self.get_member(user_id=user_id)
        
        if member_to_update is None:
            return None
        
        if new_name is not None:
            member_to_update.name = new_name
        if new_email_dev is not None:
            member_to_update.email_dev = new_email_dev
        if new_role is not None:
            member_to_update.role = new_role
        if new_stack is not None:
            member_to_update.stack = new_stack
        if new_year is not None:
            member_to_update.year = new_year
        if new_cellphone is not None:
            member_to_update.cellphone = new_cellphone
        if new_course is not None:
            member_to_update.course = new_course
        if new_active is not None:
            member_to_update.active = new_active
        if new_deactivated_date is not None:
            member_to_update.deactivated_date = new_deactivated_date
        update_dict ={
            "name": member_to_update.name,
            "email_dev": member_to_update.email_dev,
            "role": member_to_update.role.value,
            "stack": member_to_update.stack.value,
            "year": member_to_update.year,
            "cellphone": member_to_update.cellphone,
            "course": member_to_update.course.value,
            "active": member_to_update.active.value,
            "deactivated_date": member_to_update.deactivated_date if new_deactivated_date is not None else None
        }
        
        resp = self.dynamo.update_item(partition_key=self.member_partition_key_format(member_to_update), sort_key=self.member_sort_key_format(user_id), update_dict=update_dict)
        
        if "Attributes" not in resp:
            return None
        
        return MemberDynamoDTO.from_dynamo(resp["Attributes"]).to_entity()
    
    def send_active_member_email(self, member: Member) -> bool:
        try:
            client_ses = boto3.client('ses', region_name=Environments.get_envs().ses_region)

            member_active_composed_html = compose_member_active_email(member)

            response = client_ses.send_email(
                Destination={
                    'ToAddresses': [
                        member.email,
                    ],
                    'BccAddresses':
                        [
                            Environments.get_envs().hidden_copy
                        ]
                },
                Message={
                    'Body': {
                        'Html': {
                            'Charset': "UTF-8",
                            'Data': member_active_composed_html,
                        },
                    },
                    'Subject': {
                        'Charset': "UTF-8",
                        'Data': "Portal Interno - Conta Ativa",
                    },
                },
                ReplyToAddresses=[
                    Environments.get_envs().reply_to_email,
                ],
                Source=Environments.get_envs().from_email,
            )

            return True

        except Exception as err:
            print(err)
            return False