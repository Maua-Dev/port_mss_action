from typing import Dict, List

from src.shared.domain.entities.project import Project
from src.shared.domain.enums.stack_enum import STACK

MS_IN_HOUR = 3600000


class GetHoursChartViewmodel:
    projects: List[Project]
    hours_by_project: Dict[str, int]
    hours_by_project_and_stack: Dict[str, Dict[str, int]]

    def __init__(self, projects: List[Project], hours_by_project: Dict[str, int], hours_by_project_and_stack: Dict[str, Dict[str, int]]):
        self.projects = projects
        self.hours_by_project = hours_by_project
        self.hours_by_project_and_stack = hours_by_project_and_stack

    def to_dict(self) -> dict:
        areas = [stack.value for stack in STACK]

        hours_by_project = {
            project.code: round(self.hours_by_project.get(project.code, 0) / MS_IN_HOUR, 2)
            for project in self.projects
        }

        hours_by_project_and_area = {
            project.code: {
                area: round(self.hours_by_project_and_stack.get(project.code, {}).get(area, 0) / MS_IN_HOUR, 2)
                for area in areas
            }
            for project in self.projects
        }

        hours_by_area = {
            area: round(sum(hours_by_project_and_area[code][area] for code in hours_by_project_and_area), 2)
            for area in areas
        }

        total_projects = len(self.projects)
        active_projects = len([code for code, hours in hours_by_project.items() if hours > 0])

        return {
            'projects': [{'code': project.code, 'name': project.name} for project in self.projects],
            'areas': areas,
            'hours_by_project_and_area': hours_by_project_and_area,
            'hours_by_project': hours_by_project,
            'hours_by_area': hours_by_area,
            'total_hours': round(sum(hours_by_project.values()), 2),
            'total_projects': total_projects,
            'active_projects': active_projects,
            'message': 'the hours chart data was retrieved'
        }