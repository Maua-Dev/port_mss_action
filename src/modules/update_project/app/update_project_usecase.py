from typing import List
from src.shared.domain.entities.member import Member
from src.shared.domain.entities.project import Project
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.repositories.action_repository_interface import IActionRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound, ForbiddenAction


class UpdateProjectUsecase:
    def __init__(self, repo: IActionRepository):
        self.repo = repo

    def __call__(self, code, new_name: str, new_description: str, new_po_RA: str, new_scrum_RA: str, new_photos: List[str]) -> Project:

        if not Project.validate_project_code(code):
            raise EntityError("code")
        project = self.repo.get_project(code=code)

        if project is None:
            raise NoItemsFound("project")
        
        project = self.repo.update_project(code=code,
                                            new_name=new_name,
                                            new_description=new_description,
                                            new_po_RA=new_po_RA,
                                            new_scrum_RA=new_scrum_RA, 
                                            new_photos=new_photos)
        
        return project