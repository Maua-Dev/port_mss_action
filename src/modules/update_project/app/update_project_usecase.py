from typing import List, Optional
from src.shared.domain.entities.member import Member
from src.shared.domain.entities.project import Project
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.repositories.action_repository_interface import IActionRepository
from src.shared.domain.repositories.member_repository_interface import IMemberRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound, ForbiddenAction, UnregisteredUser
from src.shared.domain.enums.active_enum import ACTIVE

class UpdateProjectUsecase:
    def __init__(self, repo: IActionRepository, repo_member: IMemberRepository):
        self.repo = repo
        self.repo_member = repo_member
    def __call__(self, code, user_id: str, new_name: Optional[str] = None, new_description: Optional[str] = None, new_po_user_id: Optional[str] = None, new_scrum_user_id: Optional[str] = None, new_photos: Optional[List[str]] = None, new_members_user_ids: Optional[List[str]] = None) -> Project:

        if self.repo_member.get_member(user_id) is None:
            raise UnregisteredUser()

        user = self.repo_member.get_member(user_id=user_id)
        
        if user.active != ACTIVE.ACTIVE:
            raise ForbiddenAction("user. This user is not active.")
        
        if user.validate_role_admin(user.role) is False:
            raise ForbiddenAction("this user. is not allowed to update a project as he is not an admin")

        
        if not Project.validate_project_code(code):
            raise EntityError("code")
        project = self.repo.get_project(code=code)

        if project is None:
            raise NoItemsFound("project")
        
        if new_po_user_id is not None:
            if new_po_user_id not in new_members_user_ids:
                raise EntityError("po_user_id")
            
        if new_scrum_user_id is not None:
            if new_scrum_user_id not in new_members_user_ids:
                raise EntityError("scrum_user_id")

        project = self.repo.update_project(code=code,
                                            new_name=new_name,
                                            new_description=new_description,
                                            new_po_user_id=new_po_user_id,
                                            new_scrum_user_id=new_scrum_user_id, 
                                            new_photos=new_photos,
                                            new_members_user_ids=new_members_user_ids)
        
        return project