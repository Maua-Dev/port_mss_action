from typing import List, Optional
from src.shared.domain.entities.project import Project
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.enums.stack_enum import STACK
from src.shared.domain.repositories.action_repository_interface import IActionRepository
from src.shared.domain.repositories.member_repository_interface import IMemberRepository
from src.shared.helpers.errors.usecase_errors import DuplicatedItem, ForbiddenAction, UnregisteredUser, UserIsNotFromBusiness, UserIsNotFromAdmin
from src.shared.domain.enums.active_enum import ACTIVE

class CreateProjectUsecase:
    def __init__(self, repo: IActionRepository, repo_member: IMemberRepository):
        self.repo = repo
        self.repo_member = repo_member
        
    def __call__(self, user_id: str, code: str, name: str, description: str, po_user_id: str, scrum_user_id: str, start_date: int, members_user_ids: List[str], photo: Optional[str] = None) -> Project:
        
        project = Project(
            code=code,
            name=name,
            description=description,
            po_user_id=po_user_id,
            scrum_user_id=scrum_user_id,
            start_date=start_date,
            photo=photo,
            members_user_ids=members_user_ids
        )

        if self.repo_member.get_member(user_id=user_id) is None or self.repo_member.get_member(user_id=po_user_id) is None or self.repo_member.get_member(user_id=scrum_user_id) is None or any([self.repo_member.get_member(user_id=member_user_id) is None for member_user_id in members_user_ids]):
            raise UnregisteredUser()
        
        po = self.repo_member.get_member(user_id=po_user_id)

        if po.role not in [ROLE.PO, ROLE.SCRUM]:
            raise UserIsNotFromBusiness()
        
        if po.stack is not STACK.BUSINESS:
            raise UserIsNotFromBusiness()
        
        if po.active != ACTIVE.ACTIVE:
            raise ForbiddenAction("PO is not active.")
        
        scrum = self.repo_member.get_member(user_id=scrum_user_id)

        if scrum.role not in [ROLE.PO, ROLE.SCRUM]:
            raise UserIsNotFromBusiness()
        
        if scrum.stack is not STACK.BUSINESS:
            raise UserIsNotFromBusiness()
        
        if scrum.active != ACTIVE.ACTIVE:
            raise ForbiddenAction("Scrum is not active.")
        
        user = self.repo_member.get_member(user_id=user_id)
        
        if user.active != ACTIVE.ACTIVE:
            raise ForbiddenAction("user. This user is not active.")

        if user.validate_role_admin(user.role) is False:
            raise UserIsNotFromAdmin()

        if self.repo.get_project(code=project.code) is not None:
            raise DuplicatedItem('code')
        
        return self.repo.create_project(project)
        