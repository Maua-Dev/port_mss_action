from src.shared.domain.repositories.action_repository_interface import IActionRepository
from src.shared.domain.repositories.member_repository_interface import IMemberRepository
from src.shared.helpers.errors.usecase_errors import UnregisteredUser,ForbiddenAction, UserNotAllowed
from src.shared.domain.enums.active_enum import ACTIVE

class GetAllProjectsUsecase:
    def __init__(self, repo: IActionRepository, repo_member: IMemberRepository):
        self.repo = repo
        self.repo_member = repo_member
        
    def __call__(self, user_id: str):
        
        if self.repo_member.get_member(user_id) is None:
            raise UnregisteredUser()
        user = self.repo_member.get_member(user_id=user_id)
        if user.active != ACTIVE.ACTIVE:
            raise UserNotAllowed()
        projects = self.repo.get_all_projects()
    
        return projects