from typing import List, Optional, Tuple
from src.shared.domain.enums.active_enum import ACTIVE
from src.shared.domain.enums.course_enum import COURSE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.repositories.action_repository_interface import IActionRepository
from src.shared.domain.entities.action import Action
from src.shared.domain.entities.project import Project
from src.shared.domain.entities.associated_action import AssociatedAction
from src.shared.domain.enums.stack_enum import STACK
from src.shared.domain.enums.action_type_enum import ACTION_TYPE
from src.shared.domain.entities.member import Member

class ActionRepositoryMock(IActionRepository):
    members: List[Member]
    projects: List[Project]
    actions: List[Action]
    associatedActions: List[AssociatedAction]

    def __init__(self):
        self.projects = [
            Project(
                code="MF",
                name="Maua Food",
                description="É um aplicativo #foramoleza",
                po_RA="21017310",
                scrum_RA="21010757",
                start_date=1634576165000,
                photos=["https://i.imgur.com/gHoRKJU.png"]
                ),
            Project(
                code="PT",
                name="Portfólio",
                description="É um site",
                po_RA="22011020",
                scrum_RA="21010757",
                start_date=1673535600000,
                photos=["https://i.imgur.com/gHoRKJU.png"]
            ),
            Project(
                code="SF",
                name="Selfie Mauá",
                description="Aplicativo para reconhecimento facial",
                po_RA="22931270",
                scrum_RA="21020532",
                start_date=1686754800000
            ),
            Project(
                code="SM",
                name="SMILE",
                description="Site do evento SMILE",
                po_RA="15014025",
                scrum_RA="21010757",
                start_date=1639321200000
            ),
            Project(
                code="GM",
                name="Gameficação",
                description="Projeto para organização dos membros do DEV",
                po_RA="22084120",
                scrum_RA="22015940",
                start_date=1672585200000
            )
        ]
        
        self.members = [
            Member(
            name="Vitor Guirão MPNTM",
            email_dev="vsoller.devmaua@gmail.com",
            email="vsoller@airubio.com",
            ra="21017310",
            role=ROLE.DIRECTOR,
            stack=STACK.INFRA,
            year=1,
            cellphone="11991758098",
            course=COURSE.ECA,
            hired_date=1634576165000,
            active=ACTIVE.ACTIVE,
            projects=[
                self.projects[0].code
            ]
            ),
            
            Member(
            name="Joao Branco",
            email_dev="jbranco.devmaua@gmail.com",
            email="jbranco@gmail.com",
            ra="21010757",
            role=ROLE.HEAD,
            stack=STACK.BACKEND,
            year=3,
            cellphone="11991152348",
            course=COURSE.ECM,
            hired_date=1634921765000,
            active=ACTIVE.ACTIVE,
            projects=[
                self.projects[0].code,
                self.projects[1].code,
                self.projects[2].code
            ]
            ),
            
            Member(
            name="Luigi Televisão",
            email_dev="ltelevisao.devmaua@gmail.com",
            email="lgtv@gmail.com",
            ra="22017310",
            role=ROLE.DEV,
            stack=STACK.DATA_SCIENCE,
            year=2,
            cellphone="11991758228",
            course=COURSE.CIC,
            hired_date=1640192165000,
            active=ACTIVE.FREEZE,
            projects=[
            ]
            ),
            
            Member(
            name="Little Ronald",
            email_dev="lronald.devmaua@gmail.com",
            email="lronald@gmail.com",
            ra="10017310",
            role=ROLE.DIRECTOR,
            stack=STACK.FRONTEND,
            year=6,
            cellphone="11991759998",
            course=COURSE.ECM,
            hired_date=1614567601000,
            active=ACTIVE.ACTIVE,
            projects=[
                self.projects[0].code,
                self.projects[1].code,
                self.projects[2].code,
                self.projects[3].code
            

            ]
            ),
            
            Member(
            name="Marcos Pereira Neto",
            email_dev="mneto.devmaua@gmail.com",
            email="mneto@gmail.com",
            ra="19017310",
            role=ROLE.PO,
            stack=STACK.PO,
            year=4,
            cellphone="11991753208",
            course=COURSE.EMC,
            hired_date=1614567601000,
            active=ACTIVE.DISCONNECTED,
            projects=[
            ],
            deactivated_date=1646103601000
            ),
            
            Member(
            name="Rubicks Cube",
            email_dev="rcube.devmaua@gmail.com",
            email="rubikscube@gmail.com",
            ra="19017311",
            role=ROLE.DEV,
            stack=STACK.BACKEND,
            year=3,
            cellphone="11911758098",
            course=COURSE.ECM,
            hired_date=1640192165000,
            active=ACTIVE.ACTIVE,
            projects=[
                self.projects[3].code,
                self.projects[2].code
            ]
            ),
            
            Member(
            name="Django Fett",
            email_dev="dfett.devmaua@gmail.com",
            email="djangofett@starwars.com",
            ra="17033730",
            role=ROLE.INTERNAL,
            stack=STACK.INTERNAL,
            year=2,
            cellphone="11915758098",
            course=COURSE.ECA,
            hired_date=1609606565000,
            active=ACTIVE.FREEZE,
            projects=[
            ]
            ),
            
            Member(
            name="Henrique Gustavo de Souza",
            email_dev="hsouza.devmaua@gmail.com",
            email="hsouza@gmail.com",
            ra="23017310",
            role=ROLE.DEV,
            stack=STACK.UX_UI,
            year=1,
            cellphone="11991123498",
            course=COURSE.ECM,
            hired_date=1672592165000,
            active=ACTIVE.ACTIVE,
            projects=[
            ]
            )
        ]
        
        self.actions = [
            Action(
                owner_ra=self.members[0].ra,
                start_date=1634526000000,
                end_date=1634533200000,
                duration=7200000,
                action_id="20876e6b-d06d-439e-a939-a47a428e1c5e",
                story_id=100,
                associated_members_ra=[],
                title="Reunião de Diretoria",
                description="Reunião de diretoria para discutir sobre o futuro do DEV",
                project_code=self.projects[0].code,
                stack_tags=[STACK.INTERNAL],
                action_type_tag=ACTION_TYPE.MEETING
            ),
            
            Action(
                owner_ra=self.members[1].ra,
                start_date=1635044400000,
                end_date=1635060600000,
                duration=7200000,
                action_id="7aebb724-ec15-4075-87ad-3cac20ba99f7",
                story_id=100,
                associated_members_ra=[self.members[0].ra, self.members[2].ra],
                title="Code",
                description="Codando o site do DEV",
                project_code=self.projects[1].code,
                stack_tags=[STACK.BACKEND, STACK.FRONTEND],
                action_type_tag=ACTION_TYPE.CODE
            ),
            Action(
                owner_ra=self.members[2].ra,
                start_date=1636081200000,
                end_date=1636086600000,
                duration=5400000,
                action_id="dd34c4eb-7d80-4c81-a0ce-65cb80e9b09f",
                story_id=100,
                associated_members_ra=[self.members[3].ra],
                title="Design",
                description="Criando o design do site do DEV",
                project_code=self.projects[2].code,
                stack_tags=[STACK.UX_UI],
                action_type_tag=ACTION_TYPE.DESIGN
            ),
            
            Action(
                owner_ra=self.members[3].ra,
                start_date=1636081200000,
                end_date=1636083000000,
                duration=1800000,
                action_id="dcf34559-c2cd-4f98-abb9-1166818c4fd1",
                story_id=100,
                associated_members_ra=[],
                title="Estudo",
                project_code=self.projects[2].code,
                stack_tags=[STACK.INTERNAL],
                action_type_tag=ACTION_TYPE.LEARN
            ),
            Action(
                owner_ra=self.members[0].ra,
                start_date=1634526000000,
                end_date=1634529600000,
                duration=3600000,
                action_id="bc873180-b3f1-43d9-b3d1-6fcfb843b612",
                story_id=100,
                associated_members_ra=[],
                title="Code",
                project_code=self.projects[0].code,
                stack_tags=[STACK.BACKEND],
                action_type_tag=ACTION_TYPE.CODE
            ),
            
            Action(
                owner_ra=self.members[5].ra,
                start_date=1634526000000,
                end_date=1634529600000,
                duration=3600000,
                action_id="0f1b60e5-2171-4cb6-9538-b67e3b58622a",
                story_id=100,
                associated_members_ra=[],
                title="Reunião",
                project_code=self.projects[0].code,
                stack_tags=[STACK.BACKEND, STACK.FRONTEND],
                action_type_tag=ACTION_TYPE.CODE
            ),
            Action(
                owner_ra=self.members[0].ra,
                start_date=1666062000000,
                end_date=1666065600000,
                duration=3600000,
                action_id="3af810f9-094e-4d7c-ac34-80be80fc271b",
                story_id=100,
                associated_members_ra=[],
                title="Reunião",
                project_code=self.projects[0].code,
                stack_tags=[STACK.BACKEND, STACK.FRONTEND],
                action_type_tag=ACTION_TYPE.CODE
            ),
            
            Action(
                owner_ra=self.members[4].ra,
                start_date=1634526000000,
                end_date=1634562000000,
                duration=3600000,
                action_id='85db77bb-ea3d-4a09-b9b5-017b3a87653c',
                story_id=100,
                associated_members_ra=[],
                title="Hackathon",
                project_code=self.projects[0].code,
                stack_tags=[STACK.BACKEND],
                action_type_tag=ACTION_TYPE.CODE
            ),
            
            
        ]
        self.associatedActions = [
            AssociatedAction(
                member_ra=self.members[0].ra,
                action_id=self.actions[0].action_id
            ),
            AssociatedAction(
                member_ra=self.members[1].ra,
                action_id=self.actions[1].action_id
            ),
            AssociatedAction(
                member_ra=self.members[2].ra,
                action_id=self.actions[1].action_id
            ),
            AssociatedAction(
                member_ra=self.members[0].ra,
                action_id=self.actions[1].action_id
            ),
            AssociatedAction(
                member_ra=self.members[3].ra,
                action_id=self.actions[2].action_id
            ),
            AssociatedAction(
                member_ra=self.members[2].ra,
                action_id=self.actions[2].action_id
            ),
            AssociatedAction(
                member_ra=self.members[3].ra,
                action_id=self.actions[3].action_id
            ),
            AssociatedAction(
                member_ra=self.members[0].ra,
                action_id=self.actions[4].action_id
            ),
            AssociatedAction(
                member_ra=self.members[5].ra,
                action_id=self.actions[5].action_id
            ),
            AssociatedAction(
                member_ra=self.members[0].ra,
                action_id=self.actions[6].action_id
            ),
            AssociatedAction(
                member_ra=self.members[4].ra,
                action_id=self.actions[7].action_id
            ),
        ]

    def create_action(self, action: Action) -> Action:
        self.actions.append(action)
        return action
    
    def get_action(self, action_id: str) -> Optional[Action]:
        for action in self.actions:
            if action.action_id == action_id:
                return action
        return None
    
    def create_associated_action(self, associatedAction: AssociatedAction) -> AssociatedAction:
        self.associatedActions.append(associatedAction)
        return associatedAction
    
    def create_project(self, project: Project) -> Optional[Project]:
        self.projects.append(project)
        return project
    
    def delete_project(self, code: str) -> Project:
        for i in range(len(self.projects)):
            if self.projects[i].code == code:
                return self.projects.pop(i)
        return None

    def get_members_by_project(self, code: str) -> List[Member]:
        members = []
        for member in self.members:
            for project_code in member.projects:
                if project_code == code:
                    members.append(member)
        return members
    
    def get_project(self, code: str) -> Project:
        for project in self.projects:
            if project.code == code:
                return project
        return None
    
    def get_all_projects(self) -> List[Project]:
        return self.projects
    
    def get_all_members(self) -> List[Member]:
        return self.members