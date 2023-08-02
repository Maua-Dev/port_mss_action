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

        # Adicionar validação de permissão de usuário

        if not Project.validate_project_code(code):
            raise EntityError("code")
        project = self.repo.get_project(code=code)

        if project is None:
            raise NoItemsFound("project")
        
        if type(new_name) != str and new_name is not None:
            raise EntityError("name")
        
        if type(new_description) != str and new_description is not None:
            raise EntityError("description")
        
        if not Project.validate_RA(new_po_RA) and new_po_RA is not None:
            raise EntityError("po_RA")
        
        if not Project.validate_RA(new_scrum_RA) and new_scrum_RA is not None:
            raise EntityError("scrum_RA")
        
        if type(new_photos) != list and new_photos is not None:
            raise EntityError("photos")
        
        if new_photos != None:
            if not all(type(photo) == str for photo in new_photos):
                raise EntityError("photos")
        
        project = self.repo.update_project(code=code,
                                            new_name=new_name,
                                            new_description=new_description,
                                            new_po_RA=new_po_RA,
                                            new_scrum_RA=new_scrum_RA, 
                                            new_photos=new_photos)
        
        return project