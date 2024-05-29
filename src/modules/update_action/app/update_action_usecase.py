from typing import List, Optional
from src.shared.domain.entities.action import Action
from src.shared.domain.entities.member import Member
from src.shared.domain.enums.action_type_enum import ACTION_TYPE
from src.shared.domain.enums.stack_enum import STACK
from src.shared.domain.repositories.action_repository_interface import IActionRepository
from src.shared.domain.repositories.member_repository_interface import IMemberRepository
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound, UnregisteredUser


class UpdateActionUsecase:
    def __init__(self, repo: IActionRepository, repo_member: IMemberRepository):
        self.repo = repo
        self.repo_member = repo_member
        
    def __call__(self, action_id: str,
                user_id: str, 
                new_start_date: Optional[int] = None, 
                new_end_date: Optional[int] = None, 
                new_duration: Optional[int] = None, 
                new_story_id: Optional[int] = -1, 
                new_title: Optional[str] = None, 
                new_description: Optional[str] = '', 
                new_project_code: Optional[str] = None, 
                new_associated_members_user_ids: Optional[List[str]] = None, 
                new_stack_tags: Optional[List[STACK]] = None, 
                new_action_type_tag: Optional[ACTION_TYPE] = None) -> Action:
        
        user = self.repo_member.get_member(user_id)
        if user is None:
            raise UnregisteredUser()  
        
        action = self.repo.get_action(action_id)
        if not action:
            raise NoItemsFound('action')
        
        is_admin = Member.validate_role_admin(user.role)
        if is_admin == False and user_id != action.user_id:
            raise ForbiddenAction('This user can´t update this action. He is not the owner of the action or an admin.')
        
        members = None
        if (new_associated_members_user_ids) and (user_id == action.user_id):
            members = new_associated_members_user_ids + [action.user_id]
        else:
            members = [action.user_id]

        
        start_date = new_start_date if new_start_date is not None else action.start_date
        if members != None and set(members) != set([action.user_id] + action.associated_members_user_ids):
            self.repo.batch_update_associated_action_members(action_id, members, start_date=start_date)
        elif start_date != action.start_date:
            self.repo.batch_update_associated_action_members(action_id, members, start_date=new_start_date)
            
        description = new_description if new_description != '' else action.description
        story_id = new_story_id if new_story_id != -1 else action.story_id
        story_id = new_story_id if new_story_id != 0 else None

        return self.repo.update_action(action_id=action_id, new_user_id=action.user_id, new_start_date=new_start_date, new_end_date=new_end_date, new_duration=new_duration, new_story_id=story_id, new_title=new_title, new_description=description, new_project_code=new_project_code, new_associated_members_user_ids=new_associated_members_user_ids, new_stack_tags=new_stack_tags, new_action_type_tag=new_action_type_tag)
        