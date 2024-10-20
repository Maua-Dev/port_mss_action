from decimal import Decimal
from typing import Optional
from src.shared.domain.entities.member import Member
from src.shared.domain.repositories.member_repository_interface import IMemberRepository
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound, UserNotAllowed

from src.shared.domain.repositories.action_repository_interface import IActionRepository
from datetime import datetime


class GetAllMembersUsecase:
    def __init__(self, memberrepo: IMemberRepository, actionrepo: IActionRepository):
        self.memberrepo = memberrepo
        self.actionrepo = actionrepo
        
    def __call__(self,user_id: str) -> list:
        member = self.memberrepo.get_member(user_id)
        if member is None:
            raise NoItemsFound('user_id')
        

        is_active = Member.validate_active(member.active)
        

        members = self.memberrepo.get_all_members()
        projects = self.actionrepo.get_all_projects()
        
        member_projects = {member.user_id: [] for member in members}
        
        for project in projects:
            project_name = project.name
            for member_user_id in project.members_user_ids:
                if member_user_id in member_projects:
                    member_projects[member_user_id].append(project_name)
                    
        for member in members:
            member_user_id = member.user_id
            member.project = member_projects.get(member_user_id, [])
            
   
        if not is_active:
            raise UserNotAllowed()
        
        return members
