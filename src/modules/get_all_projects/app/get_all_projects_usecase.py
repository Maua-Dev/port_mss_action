from src.shared.domain.repositories.action_repository_interface import IActionRepository


class GetAllProjectsUsecase:
    def __init__(self, repo: IActionRepository):
        self.repo = repo
        
    def __call__(self):
        projects = self.repo.get_all_projects()
        members = self.repo.get_all_members()
        
        projects_with_members = []
        for project in projects:
            members_in_project = []
            for member in members:
                if project.code in member.projects:
                    members_in_project.append(member)
            projects_with_members.append((project, members_in_project))
    
        return projects_with_members