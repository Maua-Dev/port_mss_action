from typing import List
from src.shared.domain.entities.project import Project
from src.shared.domain.repositories.action_repository_interface import IActionRepository
from src.shared.helpers.errors.domain_errors import EntityError


class CreateProjectUsecase:
    def __init__(self, repo: IActionRepository):
        self.repo = repo
        
    def __call__(self, code: str, name: str, description: str, po_RA: str, scrum_RA: str, start_date: int, members: List[str], photos: list = None) -> Project:
        
        # if self.repo.get_project(project_id=project.project_id) is not None:
        #     raise DuplicatedItem('project_id')
        
        project = Project(
            code=code,
            name=name,
            description=description,
            po_RA=po_RA,
            scrum_RA=scrum_RA,
            start_date=start_date,
            photos=photos,
            members=members
        )
        
        return self.repo.create_project(project)
        