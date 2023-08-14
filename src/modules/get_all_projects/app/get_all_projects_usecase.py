from src.shared.domain.repositories.action_repository_interface import IActionRepository


class GetAllProjectsUsecase:
    def __init__(self, repo: IActionRepository):
        self.repo = repo
        
    def __call__(self):
        projects = self.repo.get_all_projects()
    
        return projects