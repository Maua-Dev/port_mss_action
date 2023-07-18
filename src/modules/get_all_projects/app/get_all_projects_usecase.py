from src.shared.domain.repositories.action_repository_interface import IActionRepository


class GetAllProjectsUsecase:
    def __init__(self, repo: IActionRepository):
        self.repo = repo
        
    def __call__(self):
        projects = []
        
        for project in self.repo.get_all_projects():
            projects.append((project, self.repo.get_members_by_project(code=project.code)))
            
        return projects