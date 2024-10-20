from src.shared.domain.entities.project import Project
from src.shared.domain.repositories.action_repository_interface import IActionRepository
from src.shared.domain.repositories.member_repository_interface import IMemberRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound, UnregisteredUser, UserNotAllowed, UserIsNotFromAdmin
from src.shared.domain.enums.active_enum import ACTIVE

class DeleteProjectUsecase:
    def __init__(self, repo:IActionRepository, repo_member: IMemberRepository):
        self.repo = repo
        self.repo_member = repo_member
    
    def __call__(self, code: str, user_id: str):

        if self.repo_member.get_member(user_id=user_id) is None:
            raise UnregisteredUser()
        
        user = self.repo_member.get_member(user_id=user_id)
        
        if user.active != ACTIVE.ACTIVE:
            raise UserNotAllowed()
        
        if user.validate_role_admin(user.role) is False:
            raise UserIsNotFromAdmin()
        
        if not Project.validate_project_code(code):
            raise EntityError('code')
        
        project = self.repo.delete_project(code=code)
        
        if project is None:
            raise NoItemsFound('project')
        
        return project