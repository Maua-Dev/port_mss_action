from decimal import Decimal
from typing import List, Optional
from src.shared.domain.entities.action import Action
from src.shared.domain.entities.associated_action import AssociatedAction
from src.shared.domain.entities.member import Member
from src.shared.domain.entities.project import Project
from src.shared.domain.repositories.action_repository_interface import IActionRepository
from src.shared.environments import Environments
from src.shared.infra.dto.action_dynamo_dto import ActionDynamoDTO
from src.shared.infra.dto.associated_action_dynamo_dto import AssociatedActionDynamoDTO
from src.shared.infra.dto.member_dynamo_dto import MemberDynamoDTO
from src.shared.infra.dto.project_dynamo_dto import ProjectDynamoDTO
from src.shared.infra.external.dynamo.datasources.dynamo_datasource import DynamoDatasource
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.domain.enums.action_type_enum import ACTION_TYPE
from src.shared.domain.enums.stack_enum import STACK
from boto3.dynamodb.conditions import Key

class ActionRepositoryDynamo(IActionRepository):
    @staticmethod
    def action_partition_key_format(action_id: str) -> str:
        return f'{action_id}'
    
    @staticmethod
    def action_sort_key_format(action_id: str) -> str:
        return f'action#{action_id}'
    
    @staticmethod
    def project_partition_key_format(project: Project) -> str:
        return f'project'
    
    @staticmethod
    def project_sort_key_format(code: str) -> str:
        return f'project#{code}'
    
    @staticmethod
    def member_partition_key_format(member: Member) -> str:
        return f'member'
    
    @staticmethod
    def member_sort_key_format(ra: str) -> str:
        return f'member#{ra}'
    
    @staticmethod
    def associated_action_partition_key_format(member_ra: str) -> str:
        return f'{member_ra}'
    
    @staticmethod
    def associated_action_sort_key_format(action_id: str) -> str:
        return f'associated_action#{action_id}'
    
    @staticmethod
    def gsi1_associated_action_partition_key_format(action_id: str) -> str:
        return f'{action_id}'
    
    @staticmethod
    def gsi1_associated_action_sort_key_format(member_ra: str) -> str:
        return f'associated_action#{member_ra}'

    @staticmethod
    def associated_action_lsi1_partition_key_format(member_ra: str) -> str:
        return f'{member_ra}'
    
    @staticmethod
    def associated_action_lsi1_sort_key_format(start_date: str) -> str:
        return f'{start_date}'
    
    def __init__(self):
        self.dynamo = DynamoDatasource(
            endpoint_url=Environments.get_envs().endpoint_url,
            dynamo_table_name=Environments.get_envs().dynamo_table_name,
            region=Environments.get_envs().region,
            partition_key=Environments.get_envs().dynamo_partition_key,
            sort_key=Environments.get_envs().dynamo_sort_key,
            gsi_partition_key=Environments.get_envs().dynamo_gsi_1_partition_key,
            gsi_sort_key=Environments.get_envs().dynamo_gsi_1_sort_key,
        )
        
        
    def create_project(self, project: Project) -> Project:
        item = ProjectDynamoDTO.from_entity(project).to_dynamo()
        resp = self.dynamo.put_item(item=item, partition_key=self.project_partition_key_format(project), sort_key=self.project_sort_key_format(project.code))
        
        return project
    
    def create_action(self, action: Action) -> Action:
        item = ActionDynamoDTO.from_entity(action).to_dynamo()
        resp = self.dynamo.put_item(item=item, partition_key=self.action_partition_key_format(action.action_id), sort_key=self.action_sort_key_format(action.action_id), is_decimal=True)
        
        return action
    
    def create_associated_action(self, associated_action: AssociatedAction) -> AssociatedAction:
        item = AssociatedActionDynamoDTO.from_entity(associated_action).to_dynamo()
        item['GSI1-PK'] = self.gsi1_associated_action_partition_key_format(associated_action.action_id)
        item['GSI1-SK'] = self.gsi1_associated_action_sort_key_format(associated_action.member_ra)
        resp = self.dynamo.put_item(item=item, partition_key=self.associated_action_partition_key_format(associated_action.member_ra), sort_key=self.associated_action_sort_key_format(associated_action.action_id), is_decimal=True)
        
        return associated_action
    
    def create_member(self, member: Member) -> Member:
        item = MemberDynamoDTO.from_entity(member).to_dynamo()
        resp = self.dynamo.put_item(item=item, partition_key=self.member_partition_key_format(member), sort_key=self.member_sort_key_format(member), is_decimal=True)
        
        return member
    
    def get_action(self, action_id: str) -> Optional[Action]:
        # query →  PK = action_id && SK Begins with action				
        query_string = Key(self.dynamo.partition_key).eq(self.action_partition_key_format(action_id))
        resp = self.dynamo.query(key_condition_expression=query_string, Select='ALL_ATTRIBUTES')
        
        if len(resp['Items']) == 0:
            return None
        elif resp.get("Items")[0]["entity"] != "action":
            return None
        
        action = ActionDynamoDTO.from_dynamo(resp.get("Items")[0]).to_entity()
        return action
            
    def delete_project(self, code: str) -> Optional[Project]:
        delete_project = self.dynamo.delete_item(partition_key=self.project_partition_key_format(code), sort_key=self.project_sort_key_format(code))

        if "Attributes" not in delete_project:
            return None

        return ProjectDynamoDTO.from_dynamo(delete_project['Attributes']).to_entity()
    
    def get_project(self, code: str) -> Project:
        project = self.dynamo.get_item(partition_key=self.project_partition_key_format(code), sort_key=self.project_sort_key_format(code))
        
        if "Item" not in project:
            return None

        project_dto = ProjectDynamoDTO.from_dynamo(project['Item'])
        return project_dto.to_entity()

    def update_project(self, code: str, new_name: Optional[str] = None, new_description: Optional[str] = None, new_po_RA: Optional[str] = None, new_scrum_RA: Optional[str] = None, new_photos: Optional[List[str]] = None, new_members: Optional[List[str]] = None) -> Project:
        project_to_update = self.get_project(code=code)
        
        if project_to_update is None:
            return None
        
        if new_name is not None:
            project_to_update.name = new_name
        if new_description is not None:
            project_to_update.description = new_description
        if new_po_RA is not None:
            project_to_update.po_RA = new_po_RA
        if new_scrum_RA is not None:
            project_to_update.scrum_RA = new_scrum_RA
        if new_photos is not None:
            project_to_update.photos = new_photos
        if new_members is not None:
            project_to_update.members = new_members
            
        update_dict = {
            "name": project_to_update.name,
            "description": project_to_update.description,
            "po_RA": project_to_update.po_RA,
            "scrum_RA": project_to_update.scrum_RA,
            "photos": project_to_update.photos,
            "members": project_to_update.members
        }
        
        resp = self.dynamo.update_item(partition_key=self.project_partition_key_format(project_to_update), sort_key=self.project_sort_key_format(project_to_update.code), update_dict=update_dict)
        
        if "Attributes" not in resp:
            return None
        
        return ProjectDynamoDTO.from_dynamo(resp["Attributes"]).to_entity()
    
    def get_all_projects(self) -> List[Project]:			
        query_string = Key(self.dynamo.partition_key).eq("project")
        resp = self.dynamo.query(key_condition_expression=query_string, Select='ALL_ATTRIBUTES')
        
        projects = []
        for item in resp.get("Items"):
            if item.get("entity") == "project":
                projects.append(ProjectDynamoDTO.from_dynamo(item).to_entity())
        
        return projects
    
    def get_all_members(self) -> List[Member]:
        query_string = Key(self.dynamo.partition_key).eq("member")
        resp = self.dynamo.query(key_condition_expression=query_string, Select='ALL_ATTRIBUTES')

        members = []
        for item in resp.get("Items"):
            if item.get("entity") == "member":
                members.append(MemberDynamoDTO.from_dynamo(item).to_entity())

        return members

    def get_member(self, ra: str) -> Member:
        member = self.dynamo.get_item(partition_key=self.member_partition_key_format(ra), sort_key=self.member_sort_key_format(ra))

        if "Item" not in member:
            return None

        member_dto = MemberDynamoDTO.from_dynamo(member['Item'])
        return member_dto.to_entity()
    
    def get_associated_actions_by_ra(self, ra: str, amount: int, start: Optional[int] = None, end: Optional[int] = None, exclusive_start_key: Optional[dict] = None) -> List[AssociatedAction]:
        query_string = Key(self.dynamo.partition_key).eq(ra)

        if start and end:
            query_string = query_string & Key('start_date').between(start, end)
        elif start and not end:
            query_string = query_string & Key('start_date').gte(start)
        elif end and not start:
            query_string = query_string & Key('start_date').lte(end)
            
        query_params = { 'IndexName': "LSI1", 'key_condition_expression': query_string, 'Select': 'ALL_ATTRIBUTES', 'Limit': amount }
        
        if exclusive_start_key:
            query_params['ExclusiveStartKey'] = {"PK": self.action_partition_key_format(ra), "SK" : self.associated_action_sort_key_format(exclusive_start_key['action_id']), "start_date" : Decimal(str(exclusive_start_key['start_date']))}
        
        resp = self.dynamo.query(**query_params)
        
        associated_actions = []
        for item in resp.get("Items"):
            if item.get("entity") == "associated_action":
                associated_actions.append(AssociatedActionDynamoDTO.from_dynamo(item).to_entity())
        
        return associated_actions
        
    def batch_get_action(self, action_ids: List[str]) -> List[Action]:
        # query →  PK = action_id && SK Begins with action				
        keys = [{self.dynamo.partition_key: self.action_partition_key_format(action_id), self.dynamo.sort_key: self.action_sort_key_format(action_id)} for action_id in action_ids]

        resp = self.dynamo.batch_get_items(keys=keys)

        actions = []
        for item in resp.get("Responses", { }).get(self.dynamo.dynamo_table.name,[]):
            if item.get("entity") == "action":
                actions.append(ActionDynamoDTO.from_dynamo(item).to_entity())

        
        return actions
    
    def batch_update_associated_action_start(self, action_id: str, new_start_date: Optional[int] = None) -> List[AssociatedAction]:
        '''
        Updates all associated actions with new_start_date and returns them, if any
        '''
        
        # we need to query all associated actions with action_id as sort key to get the partition keys, so we can batch_write_items
        
        query_string = Key(self.dynamo.gsi_partition_key).eq(self.gsi1_associated_action_partition_key_format(action_id))
        resp = self.dynamo.query(key_condition_expression=query_string, Select='ALL_ATTRIBUTES', IndexName="GSI1")
        
        if resp["Count"] == 0:
            return []
        
        member_ras = [item['PK'] for item in resp['Items']]
        
        update_dict = {"start_date": new_start_date}
        
        actions = []
        for ra in member_ras:
            update_resp = self.dynamo.update_item(partition_key=self.associated_action_partition_key_format(ra), sort_key=self.associated_action_sort_key_format(action_id), update_dict=update_dict)
            actions.append(AssociatedActionDynamoDTO.from_dynamo(update_resp['Attributes']).to_entity())
            
        return actions
        
    
    def batch_update_associated_action_members(self, action_id: str, members: List[str], start_date: int) -> List[AssociatedAction]:
        pass
    
    def update_action(self, action_id: str, new_owner_ra: Optional[str] = None, new_start_date : Optional[int] = None, new_end_date : Optional[int] = None, new_duration : Optional[int] = None, new_story_id : Optional[str] = None, new_title : Optional[str] = None, new_description : Optional[str] = None, new_project_code : Optional[str] = None, new_associated_members_ra : Optional[List[str]] = None, new_stack_tags : Optional[List[STACK]] = None, new_action_type_tag : Optional[ACTION_TYPE] = None) -> Action:
        
        action = self.get_action(action_id=action_id)
        
        if action is None:
            return None

        update_dict = {
            "owner_ra": new_owner_ra,
            "start_date": new_start_date,
            "end_date": new_end_date,
            "duration": new_duration,
            "story_id": new_story_id,
            "title": new_title,
            "description": new_description,
            "project_code": new_project_code,
            "associated_members_ra": new_associated_members_ra,
            "stack_tags": new_stack_tags,
            "action_type_tag": new_action_type_tag,
        }

        update_dict_without_none = {k: v for k, v in update_dict.items() if v is not None}

        response = self.dynamo.update_item(partition_key=self.action_partition_key_format(action_id), sort_key=self.action_sort_key_format(action_id), update_dict=update_dict_without_none)

        if "Attributes" not in response:
            return None
        
        return ActionDynamoDTO.from_dynamo(response['Attributes']).to_entity()