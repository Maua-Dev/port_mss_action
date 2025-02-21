from typing import Optional, Tuple
from src.shared.domain.repositories.action_repository_interface import IActionRepository
from src.shared.domain.repositories.member_repository_interface import IMemberRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound ,PaginationAmountInvalid, UnregisteredUser, UserNotAllowed, UserIsNotFromAdmin
from src.shared.domain.entities.member import Member
from src.shared.domain.entities.project import Project
from src.shared.domain.enums.active_enum import ACTIVE
from datetime import datetime
from decimal import Decimal
class DownloadProjectsUsecase:
    def __init__(self, repo: IActionRepository, repo_member: IMemberRepository):
        self.repo = repo
        self.repo_member = repo_member
        
    def __call__(self, user_id: str, start: Optional[int] = None, end: Optional[int] = None, exclusive_start_key: Optional[dict] = None, member_user_id: Optional[str] = None,project_code: Optional[str] = None):

   
        if Member.validate_user_id(user_id) is False:
            raise EntityError('user_id')
        
        if self.repo_member.get_member(user_id=user_id) is None:
            raise UnregisteredUser()
        user = self.repo_member.get_member(user_id=user_id)
        
        if start is None :
            now = datetime.now()
            year = now.year

            if (now.month <= 6) or (now.month == 12):
                if (now.month <= 6): 
                    start = datetime(year-1, 12, 1).timestamp() * 1000
                else:
                    start = datetime(year, 12, 1).timestamp() * 1000
            else:  
                start = datetime(year, 7, 1).timestamp() * 1000
        

        if end is None:
            now = datetime.now()
            year = now.year

            if (now.month <= 6) or (now.month == 12): 
                if (now.month <= 6): 
                    end = datetime(year, 6, 30).timestamp() * 1000
                else:
                    end = datetime(year+1, 6, 30).timestamp() * 1000
            else:  
                end = datetime(year, 11, 30).timestamp() * 1000

        start, end = Decimal(start), Decimal(end)
        
        if member_user_id is not None:
            if Member.validate_user_id(member_user_id) is False:
                raise EntityError('member_user_id')
            if not self.repo_member.get_member(user_id=member_user_id):
                raise UnregisteredUser()
        is_admin = Member.validate_role_admin(user.role) or Member.validate_role_external(user.role)
        if not is_admin:
            raise UserIsNotFromAdmin()
        if user.active != ACTIVE.ACTIVE:
            raise UserNotAllowed()
        if start is not None and end is not None:
            if start > end:
                raise ForbiddenAction("start must be less than end")
        if project_code is not None:
            if Project.validate_project_code(project_code) is False:
                raise EntityError('project_code')
            
            result = self.repo.get_all_actions_and_associated_actions_by_project_code(project_code=project_code, start=start, end=end)
            if result.get('actions') == [] and result.get('associated_actions') == []:
                raise NoItemsFound('actions')
        
            
        download_link = self.repo.download_actions_csv( email = user.email,user_id= member_user_id, project_code=project_code, start=start, end=end)
     

        return download_link