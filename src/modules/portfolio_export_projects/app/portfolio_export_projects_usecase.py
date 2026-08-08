from typing import List
from src.shared.domain.entities.project import Project
from src.shared.domain.repositories.action_repository_interface import IActionRepository


class PortfolioExportProjectsUsecase:
    def __init__(self, action_repo: IActionRepository):
        self.action_repo = action_repo

    def __call__(self) -> List[Project]:
        return self.action_repo.get_all_projects()
