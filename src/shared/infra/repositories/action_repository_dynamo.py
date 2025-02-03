import base64
import datetime
from decimal import Decimal
import imghdr
import os
import hashlib
from typing import List, Optional
from src.shared.domain.entities.action import Action
from src.shared.domain.entities.associated_action import AssociatedAction
from src.shared.domain.entities.member import Member
from src.shared.domain.entities.project import Project
from src.shared.domain.repositories.action_repository_interface import IActionRepository
from src.shared.environments import Environments
from botocore.config import Config
from src.shared.helpers.errors.controller_errors import WrongTypeFile
from src.shared.helpers.utils.compose_invalid_action_email import compose_invalid_action_email
from src.shared.infra.dto.action_dynamo_dto import ActionDynamoDTO
from src.shared.infra.dto.associated_action_dynamo_dto import AssociatedActionDynamoDTO
from src.shared.infra.dto.member_dynamo_dto import MemberDynamoDTO
from src.shared.infra.dto.project_dynamo_dto import ProjectDynamoDTO
from src.shared.infra.external.dynamo.datasources.dynamo_datasource import DynamoDatasource
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.domain.enums.action_type_enum import ACTION_TYPE
from src.shared.domain.enums.stack_enum import STACK

from boto3.dynamodb.conditions import Key, Attr
import boto3

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
    def member_sort_key_format(user_id: str) -> str:
        return f'member#{user_id}'
    
    @staticmethod
    def associated_action_partition_key_format(user_id: str) -> str:
        return f'{user_id}'
    
    @staticmethod
    def associated_action_sort_key_format(action_id: str) -> str:
        return f'associated_action#{action_id}'
    
    @staticmethod
    def gsi1_associated_action_partition_key_format(action_id: str) -> str:
        return f'{action_id}'
    
    @staticmethod
    def gsi1_associated_action_sort_key_format(user_id: str) -> str:
        return f'associated_action#{user_id}'

    @staticmethod
    def associated_action_lsi1_partition_key_format(user_id: str) -> str:
        return f'{user_id}'
    
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

        my_config = Config(
            region_name=Environments.get_envs().region,
            signature_version='s3v4',
        )
        self.s3_client = boto3.client(
            's3', config=my_config, region_name=Environments.get_envs().region)
        
        self.cloud_front_distribution_domain_assets_project = Environments.get_envs().cloud_front_distribution_domain_assets_project

        self.S3_BUCKET_NAME = Environments.get_envs().s3_bucket_name_project
        
        
    def create_project(self, project: Project) -> Project:

        if project.photo is not None:
            url = self.upload_project_photo(project.code, project.photo)
            project.photo = url  

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
        item['GSI1-SK'] = self.gsi1_associated_action_sort_key_format(associated_action.user_id)
        resp = self.dynamo.put_item(item=item, partition_key=self.associated_action_partition_key_format(associated_action.user_id), sort_key=self.associated_action_sort_key_format(associated_action.action_id), is_decimal=True)
        
        return associated_action
    
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

    def update_project(self, code: str, new_name: Optional[str] = None, new_description: Optional[str] = None, new_po_user_id: Optional[str] = None, new_scrum_user_id: Optional[str] = None, new_photo: Optional[str] = None, new_members_user_ids: Optional[List[str]] = None) -> Project:
        project_to_update = self.get_project(code=code)
        
        if project_to_update is None:
            return None
        
        if new_name is not None:
            project_to_update.name = new_name
        if new_description is not None:
            project_to_update.description = new_description
        if new_po_user_id is not None:
            project_to_update.po_user_id = new_po_user_id
        if new_scrum_user_id is not None:
            project_to_update.scrum_user_id = new_scrum_user_id
        if new_photo is not None:
            if new_photo[:5] == "https":
                url = new_photo
            else:
                if project_to_update.photo is not None:
                    s3_key = self.generate_key(code)
                    self.s3_client.delete_object(Bucket=self.S3_BUCKET_NAME, Key=s3_key)
                url = self.upload_project_photo(code, new_photo)
            project_to_update.photo = url
        if new_members_user_ids is not None:
            project_to_update.members_user_ids = new_members_user_ids
            
        update_dict = {
            "name": project_to_update.name,
            "description": project_to_update.description,
            "po_user_id": project_to_update.po_user_id,
            "scrum_user_id": project_to_update.scrum_user_id,
            "photo": project_to_update.photo,
            "members_user_ids": project_to_update.members_user_ids if project_to_update.members_user_ids is not None else None
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
    
    def get_associated_actions_by_user_id(self, user_id: str, amount: Optional[int] = None, start: Optional[int] = None, end: Optional[int] = None, exclusive_start_key: Optional[dict] = None) -> List[AssociatedAction]:
        query_string = Key(self.dynamo.partition_key).eq(user_id)

        if amount is None:
            amount = 20
            
        if start and end:
            query_string = query_string & Key('start_date').between(start, end)
        elif start and not end:
            query_string = query_string & Key('start_date').gte(start)
        elif end and not start:
            query_string = query_string & Key('start_date').lte(end)
            
            
        query_params = { 'IndexName': "LSI1", 'key_condition_expression': query_string, 'Select': 'ALL_ATTRIBUTES', 'Limit': amount, 'ScanIndexForward': False }
        
        if exclusive_start_key:
            query_params['ExclusiveStartKey'] = {"PK": self.action_partition_key_format(user_id), "SK" : self.associated_action_sort_key_format(exclusive_start_key['action_id']), "start_date" : Decimal(str(exclusive_start_key['start_date']))}
        resp = self.dynamo.query(**query_params)
        
        associated_actions = []
        for item in resp.get("Items"):
            if item.get("entity") == "associated_action":
                associated_actions.append(AssociatedActionDynamoDTO.from_dynamo(item).to_entity())
        
        return associated_actions
        
    def batch_get_action(self, action_ids: List[str]) -> List[Action]:
        # query →  PK = action_id && SK Begins with action	
        if len(action_ids) == 0:
            return []
        			
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
        
        user_ids = [item['PK'] for item in resp['Items']]
        
        update_dict = {"start_date": new_start_date}
        
        actions = []
        for user_id in user_ids:
            update_resp = self.dynamo.update_item(partition_key=self.associated_action_partition_key_format(user_id), sort_key=self.associated_action_sort_key_format(action_id), update_dict=update_dict)
            actions.append(AssociatedActionDynamoDTO.from_dynamo(update_resp['Attributes']).to_entity())
            
        return actions
        
    
    def batch_update_associated_action_members(self, action_id: str, user_ids: List[str], start_date: int) -> List[AssociatedAction]:
        query_string = Key(self.dynamo.gsi_partition_key).eq(self.gsi1_associated_action_partition_key_format(action_id))
        resp = self.dynamo.query(key_condition_expression=query_string, Select='ALL_ATTRIBUTES', IndexName="GSI1")
            
        if resp["Count"] == 0:
            return []
            
        member_user_ids = [item['PK'] for item in resp['Items']]
            
        for user_id in member_user_ids:
            self.dynamo.delete_item(partition_key=self.associated_action_partition_key_format(user_id), sort_key=self.associated_action_sort_key_format(action_id))
            
        actions = []
        for user_id in user_ids:
            associated_action = AssociatedAction(action_id=action_id, start_date=start_date, user_id=user_id)
            actions.append(self.create_associated_action(associated_action))
                
        return actions
    
    def update_action(self, action_id: str, new_user_id: Optional[str] = None, new_is_valid: Optional[bool] = None, new_start_date : Optional[int] = None, new_end_date : Optional[int] = None, new_duration : Optional[int] = None, new_story_id : Optional[str] = None, new_title : Optional[str] = None, new_description : Optional[str] = None, new_project_code : Optional[str] = None, new_associated_members_user_ids : Optional[List[str]] = None, new_stack_tags : Optional[List[STACK]] = None, new_action_type_tag : Optional[ACTION_TYPE] = None) -> Action:
        
        action = self.get_action(action_id=action_id)
        
        if action is None:
            return None

        update_dict = {
            "user_id": new_user_id,
            "start_date": Decimal(str(new_start_date)) if new_start_date is not None else None,
            "end_date": Decimal(str(new_end_date)) if new_end_date is not None else None,
            "duration": Decimal(str(new_duration)) if new_duration is not None else None,
            "story_id": Decimal(new_story_id) if new_story_id is not None else None,
            "is_valid": new_is_valid,
            "title": new_title,
            "description": new_description,
            "project_code": new_project_code,
            "associated_members_user_ids": new_associated_members_user_ids,
            "stack_tags": [stack.value for stack in new_stack_tags] if new_stack_tags is not None else None,
            "action_type_tag": new_action_type_tag.value if new_action_type_tag is not None else None,
        }

        update_dict_without_none = {k: v for k, v in update_dict.items() if v is not None}

        response = self.dynamo.update_item(partition_key=self.action_partition_key_format(action_id), sort_key=self.action_sort_key_format(action_id), update_dict=update_dict_without_none)

        if "Attributes" not in response:
            return None
        
        return ActionDynamoDTO.from_dynamo(response['Attributes']).to_entity()
    

    def delete_action(self, action_id: str) -> Optional[Action]:
        delete_action = self.dynamo.delete_item(partition_key=self.action_partition_key_format(action_id), sort_key=self.action_sort_key_format(action_id))

        if "Attributes" not in delete_action:
            return None
        
        self.batch_delete_associated_actions(action_id=action_id)

        return ActionDynamoDTO.from_dynamo(delete_action['Attributes']).to_entity()

    def batch_delete_associated_actions(self, action_id: str) -> List[AssociatedAction]:
        query_string = Key(self.dynamo.gsi_partition_key).eq(self.gsi1_associated_action_partition_key_format(action_id))
        resp = self.dynamo.query(key_condition_expression=query_string, Select='ALL_ATTRIBUTES', IndexName="GSI1")
        
        if resp["Count"] == 0:
            return []
        
        user_ids = [item['PK'] for item in resp['Items']]
        
        for user_id in user_ids:
            self.dynamo.delete_item(partition_key=self.associated_action_partition_key_format(user_id), sort_key=self.associated_action_sort_key_format(action_id))
            
        return [AssociatedActionDynamoDTO.from_dynamo(item).to_entity() for item in resp['Items']]

    def scan_actions_by_start_date(self, start_date, end_date):
        expression = Attr('start_date').between(start_date,end_date) & Attr('SK').begins_with('action#')

        resp = self.dynamo.scan_items(expression)
        
        if resp["Count"] == 0:
            return []
        
        return [ActionDynamoDTO.from_dynamo(item).to_entity for item in resp['Items']]
    
    def get_all_actions_durations_by_user_id(self, start_date: int , end_date:int) -> dict:
        expression = Attr('SK').begins_with('action#') & Attr('start_date').between(start_date, end_date) & Attr('end_date').lte(end_date)
        
        resp = self.dynamo.scan_items(expression)
        
        if resp["Count"] == 0:
            return {}
        
        durations_by_user_id = {}
        
        for item in resp['Items']:
            action = ActionDynamoDTO.from_dynamo(item).to_entity()
            
            if action.duration is not None:
                if action.user_id in durations_by_user_id:
                    durations_by_user_id[action.user_id] += action.duration
                else:
                    durations_by_user_id[action.user_id] = action.duration
                
                for associated_user_id in action.associated_members_user_ids:
                    if associated_user_id in durations_by_user_id:
                        durations_by_user_id[associated_user_id] += action.duration
                    else:
                        durations_by_user_id[associated_user_id] = action.duration
        
        return durations_by_user_id

    def get_action_durations_for_user(self, user_id: str, start_date: int, end_date: int) -> int:
        expression = Attr('SK').begins_with('action#') & Attr('start_date').between(start_date, end_date) & Attr('end_date').lte(end_date)
        
        resp = self.dynamo.scan_items(expression)
        
        if resp["Count"] == 0:
            return 0
        
        total_duration = 0
        
        for item in resp['Items']:
            action = ActionDynamoDTO.from_dynamo(item).to_entity()
            
            if action.duration is not None:
                
                if action.user_id == user_id:
                    total_duration += action.duration
                
                if user_id in action.associated_members_user_ids:
                    total_duration += action.duration
        
        return total_duration

        
    def send_invalid_action_email(self, member: Member, action: Action) -> bool:
        try:
            client_ses = boto3.client('ses', region_name=Environments.get_envs().region)

            member_active_composed_html = compose_invalid_action_email(member, action)

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
        
    def generate_key(self, code: str, file_type: str) -> str:

        key = f"{code}.{file_type}"
        return key
        
    def upload_project_photo(self, code: str, photo: str) -> str:
        try:
            photo_bytes = base64.b64decode(photo)
            

            file_type = imghdr.what(None, photo_bytes)
            if file_type is None:
                raise WrongTypeFile()
            
            s3_key = self.generate_key(code, file_type)

            content_type = f"'image/{file_type}"

            self.s3_client.put_object(
                Bucket=self.S3_BUCKET_NAME,
                Key=f"{s3_key}",
                Body=photo_bytes,
                ContentType= content_type
            )

            meta = {
                "photo": photo,
                "time_created": str(datetime.datetime.now().timestamp() * 1000)
            }

            presigned_url = self.s3_client.generate_presigned_url(
                ClientMethod='put_object',
                Params={
                    'Bucket': self.S3_BUCKET_NAME,
                    'Key': s3_key,
                    'Metadata': meta,
                    'ContentDisposition': 'inline',
                },
                ExpiresIn=600,
            )

            presigned_url = presigned_url.replace(
                f"{self.S3_BUCKET_NAME}.s3.amazonaws.com", self.cloud_front_distribution_domain_assets_project)

            return presigned_url
        except Exception as e:
            print(e)
            raise e

    def get_all_actions_durations_by_project(self, start_date: int , end_date:int) -> dict:
        expression = Attr('SK').begins_with('action#') & Attr('start_date').between(start_date, end_date) & Attr('end_date').lte(end_date)
        
        resp = self.dynamo.scan_items(expression)
        
        if resp["Count"] == 0:
            return {}
        
        durations_by_project = {}
        
        for item in resp['Items']:
            action = ActionDynamoDTO.from_dynamo(item).to_entity()

            if action.duration is not None:
                if action.project_code in durations_by_project:
                    durations_by_project[action.project_code] += action.duration
                else:
                    durations_by_project[action.project_code] = action.duration
        
        return durations_by_project
    
    def get_all_actions_by_project_code(self, project_code: str, amount: Optional[int] = None, start: Optional[int] = None, end: Optional[int] = None, exclusive_start_key: Optional[dict] = None) -> List[Action]:
        query_string = Attr('project_code').eq(project_code)

        # query_params = {
        #     'IndexName': "LSI1",
        #     'FilterExpression': Attr('project_code').eq(project_code),
        #     'Select': 'ALL_ATTRIBUTES',
        #     'Limit': amount,
        #     'ScanIndexForward': False
        # }

        # if exclusive_start_key:
        #     query_params['ExclusiveStartKey'] = {
        #         "start_date": Decimal(str(exclusive_start_key['start_date']))
        #     }

        resp = self.dynamo.scan_items(query_string)
        actions = []
        for item in resp.get("Items", []):
            if item.get("entity") == "action":
                actions.append(ActionDynamoDTO.from_dynamo(item).to_entity())


        return actions
    def get_projects_with_actions_and_associations(self) -> dict:
   
        projects_resp = self.dynamo.scan_items(Attr('SK').begins_with('project#'))

        if projects_resp["Count"] == 0:
            return {}

        projects_with_details = {}

        # Iterar sobre os projetos
        for project_item in projects_resp['Items']:
            # Converter o projeto para uma entidade
            project = ProjectDynamoDTO.from_dynamo(project_item).to_entity()
            project_code = project.code

            # Buscar ações relacionadas ao projeto
            actions_expression = Attr('SK').begins_with('action#') & Attr('project_code').eq(project_code)
            actions_resp = self.dynamo.scan_items(actions_expression)

            actions = (
                [
                    ActionDynamoDTO.from_dynamo(action_item).to_entity()
                    for action_item in actions_resp['Items']
                ]
                if actions_resp["Count"] > 0
                else []
            )

            actions_with_associations = []

            # Para cada ação, buscar suas associações
            for action in actions:
                associations_expression = Attr('SK').begins_with('associated_action#') & Attr('action_id').eq(action.action_id)
                associations_resp = self.dynamo.scan_items(associations_expression)

                associations = (
                    [
                        AssociatedActionDynamoDTO.from_dynamo(assoc_item).to_entity()
                        for assoc_item in associations_resp['Items']
                    ]
                    if associations_resp["Count"] > 0
                    else []
                )

                # Montar a estrutura de cada ação com suas associações
                actions_with_associations.append({
                    "action_id": action.action_id,
                    "title": action.title,
                    "description": action.description,
                    "start_date": action.start_date,
                    "end_date": action.end_date,
                    "duration": action.duration,
                    "user_id": action.user_id,
                    "associated_members_user_ids": action.associated_members_user_ids,
                    "stack_tags": action.stack_tags,
                    "action_type_tag": action.action_type_tag,
                    "associations": [
                        {
                            "associated_action_id": assoc.action_id,
                            "user_id": assoc.user_id,
                            "start_date": assoc.start_date
                        }
                        for assoc in associations
                    ]
                })

            # Montar os detalhes do projeto com as ações e associações
            projects_with_details[project_code] = {
                "project_name": project.name,
                "description": project.description,
                "po_user_id": project.po_user_id,
                "scrum_user_id": project.scrum_user_id,
                "photo": project.photo,
                "members_user_ids": project.members_user_ids,
                "actions": actions_with_associations
            }

        return projects_with_details

    
    def get_all_actions_by_user_id(self, user_id: str, start: Optional[int] = None, end: Optional[int] = None) -> dict[str, List[dict]]:
  
   
        actions_expression = (
            Attr('SK').begins_with('action#') &
            Attr('user_id').eq(user_id) &
            Attr('start_date').between(start, end) &
            Attr('end_date').lte(end)
        )
        actions_resp = self.dynamo.scan_items(actions_expression)

        if actions_resp["Count"] == 0:
            return {"actions": [], "associated_actions": []}

        actions = [
            ActionDynamoDTO.from_dynamo(item).to_entity()
            for item in actions_resp['Items']
        ]

        associated_actions = []

        # Busca as ações associadas relacionadas a cada ação encontrada
        for action in actions:
            associated_expression = (
                Attr('SK').begins_with('associated_action#') &
                Attr('action_id').eq(action.action_id)
            )
            associated_resp = self.dynamo.scan_items(associated_expression)

            if associated_resp["Count"] > 0:
                associated_actions.extend([
                    AssociatedActionDynamoDTO.from_dynamo(item).to_entity()
                    for item in associated_resp['Items']
                ])

        # Estrutura a resposta com as ações e suas associadas
        return {
            "actions": [
                {
                    "action_id": action.action_id,
                    "title": action.title,
                    "description": action.description,
                    "start_date": action.start_date,
                    "end_date": action.end_date,
                    "duration": action.duration,
                    "user_id": action.user_id,
                    "associated_members_user_ids": action.associated_members_user_ids,
                    "stack_tags": action.stack_tags,
                    "action_type_tag": action.action_type_tag
                }
                for action in actions
            ],
            "associated_actions": [
                {
                    "associated_action_id": associated_actions.action_id,
                    "user_id": assoc.user_id,
                    "start_date": assoc.start_date,
                    "action_id": assoc.action_id 
                }
                for assoc in associated_actions
            ]
        }

    
    def get_all_actions_and_associated_actions_by_project_code(self, project_code: str, start: Optional[int] = None, end: Optional[int] = None) -> dict[str, List[Action]]:

        expression = Attr('SK').begins_with('action#') & Attr('project_code').eq(project_code)

        if start:
            expression = expression & Attr('start_date').gte(start)
        if end:
            expression = expression & Attr('end_date').lte(end)

        actions_resp = self.dynamo.scan_items(expression)

        if actions_resp["Count"] == 0:
            return {"actions": [], "associated_actions": []}

        actions = [
            ActionDynamoDTO.from_dynamo(item).to_entity()
            for item in actions_resp['Items']
        ]

        action_ids = {action.action_id for action in actions}

        associated_expression = Attr('SK').begins_with('associated_action#') & Attr('action_id').is_in(list(action_ids))

        associated_resp = self.dynamo.scan_items(associated_expression)

        associated_actions = (
            [
                AssociatedActionDynamoDTO.from_dynamo(item).to_entity()
                for item in associated_resp['Items']
            ]
            if associated_resp["Count"] > 0
            else []
        )
        return {
            "actions": actions,
            "associated_actions": associated_actions,
        }
    def create_csv_actions(self,actions: List[dict], associated_actions: List[dict]) -> str:
        """
        Gera o conteúdo de um arquivo CSV com as ações e as ações associadas.
        """
        # Cabeçalhos do CSV
        csv = (
            'Action ID, Title, Description, Start Date, End Date, Duration, User ID, Associated Members, Stack Tags, Action Type\n'
        )

        # Adicionar ações ao CSV
        for action in actions:
            csv += (
                f"{action['action_id']}, {action['title']}, {action['description']}, {action['start_date']}, "
                f"{action['end_date']}, {action['duration']}, {action['user_id']}, "
                f"{';'.join(action['associated_members_user_ids']) if action['associated_members_user_ids'] else ''}, "
                f"{';'.join(action['stack_tags']) if action['stack_tags'] else ''}, {action['action_type_tag']}\n"
            )

        # Separador entre ações e ações associadas
        csv += '\nAssociated Actions\n'
        csv += 'Associated Action ID, User ID, Start Date, Action ID\n'

        # Adicionar ações associadas ao CSV
        for assoc_action in associated_actions:
            csv += (
                f"{assoc_action['associated_action_id']}, {assoc_action['user_id']}, "
                f"{assoc_action['start_date']}, {assoc_action['action_id']}\n"
            )

        return csv


    def download_actions_csv(self, user_id: Optional[str] = None, project_code: Optional[str] = None, start: Optional[int] = None, end: Optional[int] = None) -> bytes:
        """
        Gera e faz o download de um CSV contendo ações e ações associadas, com base no user_id ou project_code.
        """
        try:
            # Verificar se HASH_KEY está definido
            hash_key = os.environ.get('HASH_KEY')
            if not hash_key:
                raise ValueError("HASH_KEY não está definido nas variáveis de ambiente.")

            prefix = hashlib.sha256(hash_key.encode('utf-8')).hexdigest()

            # Obter ações e ações associadas
            if user_id:
                actions_data = self.get_all_actions_by_user_id(user_id, start, end)
            elif project_code:
                actions_data = self.get_all_actions_and_associated_actions_by_project_code(project_code, start, end)
            else:
                raise ValueError("É necessário fornecer user_id ou project_code.")

            actions = actions_data['actions']
            associated_actions = actions_data['associated_actions']

            # Gerar CSV
            csv_content = self.create_csv_actions(actions, associated_actions)

            # Definir chave S3
            csv_key = f"{prefix}/actions_{user_id or project_code}.csv"

            # Fazer upload do CSV para o S3
            self.s3_client.put_object(
                Bucket=self.S3_BUCKET_NAME,
                Key=csv_key,
                Body=csv_content,
                ContentType="text/csv"
            )

            # Gerar URL pré-assinada para download
            presigned_url = self.s3_client.generate_presigned_url(
                ClientMethod='get_object',
                Params={
                    'Bucket': self.S3_BUCKET_NAME,
                    'Key': csv_key
                },
                ExpiresIn=600  # URL expira em 10 minutos
            )

            # Substituir domínio S3 pelo CloudFront, se aplicável
            if hasattr(self, 'cloud_front_distribution_domain_assets_project'):
                presigned_url = presigned_url.replace(
                    f"{self.S3_BUCKET_NAME}.s3.amazonaws.com",
                    self.cloud_front_distribution_domain_assets_project
                )

            return presigned_url

        except Exception as err:
            print(f"Erro ao criar ou baixar o CSV: {err}")
            return None
