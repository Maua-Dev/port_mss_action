from typing import List
from src.shared.domain.entities.project import Project
from src.shared.domain.repositories.action_repository_interface import IActionRepository
from src.shared.helpers.errors.usecase_errors import DuplicatedItem


class CreateProjectUsecase:
    def __init__(self, repo: IActionRepository):
        self.repo = repo
        
    def __call__(self, code: str, name: str, description: str, po_user_id: str, scrum_user_id: str, start_date: int, members_user_ids: List[str], photos: list = None) -> Project:
        
        project = Project(
            code=code,
            name=name,
            description=description,
            po_user_id=po_user_id,
            scrum_user_id=scrum_user_id,
            start_date=start_date,
            photos=photos,
            members_user_ids=members_user_ids
        )

        if self.repo.get_project(code=project.code) is not None:
            raise DuplicatedItem('code')
        
        return self.repo.create_project(project)
        