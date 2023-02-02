import datetime
from typing import List
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
from src.shared.helpers.errors.usecase_errors import NoItemsFound

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
                description="É um aplicativo #foramoleza"
                ),
            Project(
                code="PT",
                name="Portfólio",
                description="É um site"
            ),
            Project(
                code="SF",
                name="Selfie Mauá",
                description="Aplicativo para reconhecimento facial"
            ),
            Project(
                code="SM",
                name="SMILE",
                description="Site do evento SMILE"
            ),
            Project(
                code="GM",
                name="Gameficação",
                description="Projeto para organização dos membros do DEV"
            )
        ]
        
        self.members = [
            Member(
            name="Vitor Guirão MPNTM",
            email="vsoller.devmaua@gmail.com",
            ra="21017310",
            role=ROLE.DIRECTOR,
            stack=STACK.INFRA,
            year=1,
            cellphone="11991758098",
            course=COURSE.ECA,
            hired_date=1634576165,
            active=ACTIVE.ACTIVE,
            projects=[
                self.projects[0]
            ]
            ),
            
            Member(
            name="Joao Branco",
            email="jbranco.devmaua@gmail.com",
            ra="21010757",
            role=ROLE.HEAD,
            stack=STACK.BACKEND,
            year=3,
            cellphone="11991152348",
            course=COURSE.ECM,
            hired_date=1634921765,
            active=ACTIVE.ACTIVE,
            projects=[
                self.projects[0],
                self.projects[1],
                self.projects[2]
            ]
            ),
            
            Member(
            name="Luigi Televisão",
            email="ltelevisao.devmaua@gmail.com",
            ra="22017310",
            role=ROLE.DEV,
            stack=STACK.DATA_SCIENCE,
            year=2,
            cellphone="11991758228",
            course=COURSE.CIC,
            hired_date=1640192165,
            active=ACTIVE.FREEZE,
            projects=[
            ]
            ),
            
            Member(
            name="Little Ronald",
            email="lronald.devmaua@gmail.com",
            ra="10017310",
            role=ROLE.DIRECTOR,
            stack=STACK.FRONTEND,
            year=6,
            cellphone="11991759998",
            course=COURSE.ECM,
            hired_date=1293036965,
            active=ACTIVE.ACTIVE,
            projects=[
                self.projects[0],
                self.projects[1],
                self.projects[2],
                self.projects[3]
            

            ]
            ),
            
            Member(
            name="Marcos Pereira Neto",
            email="mneto.devmaua@gmail.com",
            ra="19017310",
            role=ROLE.PO,
            stack=STACK.PO,
            year=4,
            cellphone="11991753208",
            course=COURSE.EMC,
            hired_date=1545497765,
            active=ACTIVE.DISCONNECTED,
            projects=[
            ],
            deactivated_date=1577033765
            ),
            
            Member(
            name="Rubicks Cube",
            email="rcube.devmaua@gmail.com",
            ra="19017310",
            role=ROLE.DEV,
            stack=STACK.BACKEND,
            year=3,
            cellphone="11911758098",
            course=COURSE.ECM,
            hired_date=1640192165,
            active=ACTIVE.ACTIVE,
            projects=[
                self.projects[3],
                self.projects[2]
            ]
            ),
            
            Member(
            name="Django Fett",
            email="dfett.devmaua@gmail.com",
            ra="17033730",
            role=ROLE.INTERNAL,
            stack=STACK.INTERNAL,
            year=2,
            cellphone="11915758098",
            course=COURSE.ECA,
            hired_date=1609606565,
            active=ACTIVE.FREEZE,
            projects=[
            ]
            ),
            
            Member(
            name="Henrique Gustavo de Souza",
            email="hsouza.devmaua@gmail.com",
            ra="23017310",
            role=ROLE.DEV,
            stack=STACK.UX_UI,
            year=1,
            cellphone="11991123498",
            course=COURSE.ECM,
            hired_date=1672592165,
            active=ACTIVE.ACTIVE,
            projects=[
            ]
            )
        ]
        
        self.actions = [
            Action(
                owner_ra=self.members[0].ra,
                date=1634526000,
                action_id="u1e2",
                associated_members_ra=None,
                title="Reunião de Diretoria",
                duration=datetime.time(2, 0, 0),
                project_code=self.projects[0].code,
                stack_tags=[STACK.INTERNAL],
                action_type_tags=[ACTION_TYPE.MEETING]
            ),
            
            Action(
                owner_ra=self.members[1].ra,
                date=1635044400,
                action_id="9fc2",
                associated_members_ra=[self.members[0].ra, self.members[2].ra],
                title="Code",
                duration=datetime.time(4, 30, 0),
                project_code=self.projects[1].code,
                stack_tags=[STACK.BACKEND, STACK.FRONTEND],
                action_type_tags=[ACTION_TYPE.CODE]
            ),
            Action(
                owner_ra=self.members[2].ra,
                date=1636081200,
                action_id="921f",
                associated_members_ra=[self.members[3].ra],
                title="Design",
                duration=datetime.time(1, 30, 0),
                project_code=self.projects[2].code,
                stack_tags=[STACK.UX_UI],
                action_type_tags=[ACTION_TYPE.DESIGN]
            ),
            
            Action(
                owner_ra=self.members[3].ra,
                date=1636081200,
                action_id="0d2d",
                associated_members_ra=[],
                title="Estudo",
                duration=datetime.time(0, 30, 0),
                project_code=self.projects[2].code,
                stack_tags=[STACK.INTERNAL],
                action_type_tags=[ACTION_TYPE.LEARN]
            ),
            Action(
                owner_ra=self.members[0].ra,
                date=1634526000,
                action_id="dd1d",
                associated_members_ra=None,
                title="Code",
                duration=datetime.time(1, 0, 0),
                project_code=self.projects[0].code,
                stack_tags=None,
                action_type_tags=[ACTION_TYPE.CODE]
            ),
            
            Action(
                owner_ra=self.members[5].ra,
                date=1634526000,
                action_id="jgrl",
                associated_members_ra=None,
                title="Reunião",
                duration=datetime.time(1, 0, 0),
                project_code=self.projects[0].code,
                stack_tags=[STACK.BACKEND, STACK.FRONTEND],
                action_type_tags=None
            ),
            Action(
                owner_ra=self.members[0].ra,
                date=1666062000,
                action_id="jf12",
                associated_members_ra=None,
                title="Reunião",
                duration=datetime.time(1, 0, 0),
                project_code=self.projects[0].code,
                stack_tags=[STACK.BACKEND, STACK.FRONTEND],
                action_type_tags=None
            ),
            
            Action(
                owner_ra=self.members[4].ra,
                date=1634526000,
                action_id='32kd',
                associated_members_ra=None,
                title="Hackathon",
                duration=datetime.time(10, 0, 0),
                project_code=self.projects[0].code,
                stack_tags=None,
                action_type_tags=None
            ),
            
            
        ]
        self.associatedActions = [
            AssociatedAction(
                member_ra=self.members[0].ra,
                action=self.actions[0]
            ),
            AssociatedAction(
                member_ra=self.members[1].ra,
                action=self.actions[1]
            ),
            AssociatedAction(
                member_ra=self.members[2].ra,
                action=self.actions[1]
            ),
            AssociatedAction(
                member_ra=self.members[0].ra,
                action=self.actions[1]
            ),
            AssociatedAction(
                member_ra=self.members[3].ra,
                action=self.actions[2]
            ),
            AssociatedAction(
                member_ra=self.members[2].ra,
                action=self.actions[2]
            ),
            AssociatedAction(
                member_ra=self.members[3].ra,
                action=self.actions[3]
            ),
            AssociatedAction(
                member_ra=self.members[0].ra,
                action=self.actions[4]
            ),
            AssociatedAction(
                member_ra=self.members[5].ra,
                action=self.actions[5]
            ),
            AssociatedAction(
                member_ra=self.members[0].ra,
                action=self.actions[6]
            ),
            AssociatedAction(
                member_ra=self.members[4].ra,
                action=self.actions[7]
            ),
        ]

    def get_member(self, ra: str) -> Member:
        for member in self.members:
            if member.ra == ra:
                return member
            
        return None

    def get_all_actions_by_ra(self, ra: str) -> List[Action]:
        owner_actions = [action for action in self.actions if action.owner_ra == ra]
        associated_actions = [action for action in self.actions if ra in action.associated_members_ra]
        actions = owner_actions + associated_actions
        actions.sort(key=lambda action: action.date)
        return actions
    
    def create_member(self, member: Member) -> Member:
        self.members.append(member)
        return member
    
    def create_action(self, action: Action) -> Action:
        self.actions.append(action)
        self.create_associated_action(AssociatedAction(action.owner_ra, action))
        if action.associated_members_ra is not None:
            for ra in action.associated_members_ra:
                self.create_associated_action(AssociatedAction(ra, action))
        
        return action
    
    def get_action(self, action_id: str) -> Action:
        for action in self.actions:
            if action.action_id == action_id:
                return action
        return None
    
    def create_associated_action(self, associatedAction: AssociatedAction) -> AssociatedAction:
        self.associatedActions.append(associatedAction)
        return associatedAction