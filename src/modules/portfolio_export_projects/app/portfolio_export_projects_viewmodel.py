from typing import List
from src.shared.domain.entities.project import Project


class PortfolioExportProjectsViewModel:
    def __init__(self, projects: List[Project]):
        self.projects = projects

    def to_dict(self):
        return {
            "projects": [
                {
                    "code": project.code,
                    "name": project.name,
                    "description": project.description,
                    "photo": project.photo if project.photo is not None else ""
                }
                for project in self.projects
            ]
        }
