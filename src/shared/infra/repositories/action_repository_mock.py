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
    associated_actions: List[AssociatedAction]

    def __init__(self):
        self.projects = [
            Project(
                code="MF",
                name="Maua Food",
                description="É um aplicativo #foramoleza",
                po_RA="21017310",
                scrum_RA="21010757",
                start_date=1634576165000,
                photos=["https://i.imgur.com/gHoRKJU.png"],
                members=["10017310", "21010757", "21017310"]
            ),
            Project(
                code="PT",
                name="Portfólio",
                description="É um site",
                po_RA="22011020",
                scrum_RA="21010757",
                start_date=1673535600000,
                photos=["https://i.imgur.com/gHoRKJU.png"],
                members=["10017310", "21010757", "22011020"]
            ),
            Project(
                code="SF",
                name="Selfie Mauá",
                description="Aplicativo para reconhecimento facial",
                po_RA="22931270",
                scrum_RA="21020532",
                start_date=1686754800000,
                members=["10017310", "19017311", "21010757", "21020532", "22931270" ]
            ),
            Project(
                code="SM",
                name="SMILE",
                description="Site do evento SMILE",
                po_RA="15014025",
                scrum_RA="21010757",
                start_date=1639321200000,
                members=["10017310", "15014025", "19017311", "21010757"]
            ),
            Project(
                code="GM",
                name="Gameficação",
                description="Projeto para organização dos membros do DEV",
                po_RA="22084120",
                scrum_RA="22015940",
                start_date=1672585200000,
                members=["22015940", "22084120"]
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
                active=ACTIVE.ACTIVE
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
                active=ACTIVE.ACTIVE
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
                active=ACTIVE.FREEZE
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
                active=ACTIVE.ACTIVE
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
                active=ACTIVE.DISCONNECTED
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
                active=ACTIVE.ACTIVE
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
                active=ACTIVE.FREEZE
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
                active=ACTIVE.ACTIVE
            )
        ]

        self.actions = [
            Action(owner_ra="10017310",
                   action_id="5f4f13df-e7d3-4a10-9219-197ceae9e3f0",
                   story_id=94,
                   associated_members_ra=[
                       "23017310",
                       "21010757",
                       "22017310",
                       "21017310",
                       "19017310",
                       "19017311"
                   ],
                   stack_tags=[
                       STACK.INFRA
                   ],
                   action_type_tag=ACTION_TYPE.CODEREVIEW,
                   project_code="PT",
                   title="Retrospectiva",
                   description="Revisão de sprint",
                   start_date=1644256000000,
                   end_date=1653756000000,
                   duration=9500000000),
            Action(owner_ra="10017310",
                   action_id="24c7d7a3-6560-4652-a8d6-f2e4f3f23460",
                   story_id=368,
                   associated_members_ra=[
                       "19017311",
                       "23017310",
                       "21010757"
                   ],
                   stack_tags=[
                       STACK.INTERNAL
                   ],
                   action_type_tag=ACTION_TYPE.DESIGN,
                   project_code="SF",
                   title="Retrospectiva",
                   description="Front-End",
                   start_date=1676476000000,
                   end_date=1684306000000,
                   duration=7830000000),
            Action(owner_ra="10017310",
                   action_id="42e01f11-283c-4925-b0aa-e80ac6c1815a",
                   story_id=983,
                   associated_members_ra=[
                       "21017310",
                       "19017310",
                       "19017311",
                       "23017310",
                       "17033730"
                   ],
                   stack_tags=[
                       STACK.INFRA
                   ],
                   action_type_tag=ACTION_TYPE.WORK,
                   project_code="SF",
                   title="Retrospectiva",
                   description="Revisão de sprint",
                   start_date=1641896000000,
                   end_date=1679686000000,
                   duration=37790000000),
            Action(owner_ra="19017311",
                   action_id="ea95d4f7-d5ce-4944-9fa1-ab964655294b",
                   story_id=435,
                   associated_members_ra=[
                       "17033730",
                       "22017310",
                       "10017310",
                       "23017310",
                       "21017310"
                   ],
                   stack_tags=[
                       STACK.FRONTEND
                   ],
                   action_type_tag=ACTION_TYPE.DESIGN,
                   project_code="SF",
                   title="Retrospective",
                   description="Reunião de planning",
                   start_date=1658136000000,
                   end_date=1678116000000,
                   duration=19980000000),
            Action(owner_ra="21017310",
                   action_id="7778ee40-d98b-4187-8b02-052b70cc1ec1",
                   story_id=848,
                   associated_members_ra=[
                       "19017311",
                       "19017310"
                   ],
                   stack_tags=[
                       STACK.INFRA
                   ],
                   action_type_tag=ACTION_TYPE.LEARN,
                   project_code="SF",
                   title="Daily",
                   description="Sprint Planning",
                   start_date=1656666000000,
                   end_date=1687596000000,
                   duration=30930000000),
            Action(owner_ra="21010757",
                   action_id="92cebaa4-02d5-4618-9b32-0c668b8361cd",
                   story_id=144,
                   associated_members_ra=[

                   ],
                   stack_tags=[
                       STACK.INFRA
                   ],
                   action_type_tag=ACTION_TYPE.PRESENTATION,
                   project_code="SM",
                   title="Revisão",
                   description="Review",
                   start_date=1656646000000,
                   end_date=1681286000000,
                   duration=24640000000),
            Action(owner_ra="19017310",
                   action_id="eefe6db8-e03e-42c3-9fd2-1de796139501",
                   story_id=497,
                   associated_members_ra=[
                       "23017310",
                       "10017310",
                       "17033730"
                   ],
                   stack_tags=[
                       STACK.INTERNAL
                   ],
                   action_type_tag=ACTION_TYPE.ARCHITECT,
                   project_code="SM",
                   title="Retrospective",
                   description="Reunião de planning",
                   start_date=1667256000000,
                   end_date=1690046000000,
                   duration=22790000000),
            Action(owner_ra="19017310",
                   action_id="46b35022-1a68-4cc8-a2e5-ae449e43e867",
                   story_id=237,
                   associated_members_ra=[
                       "10017310",
                       "23017310",
                       "19017311",
                       "17033730",
                       "22017310"
                   ],
                   stack_tags=[
                       STACK.BACKEND
                   ],
                   action_type_tag=ACTION_TYPE.WORK,
                   project_code="GM",
                   title="Revisão",
                   description="Sprint Planning",
                   start_date=1688646000000,
                   end_date=1689966000000,
                   duration=1320000000),
            Action(owner_ra="10017310",
                   action_id="711d1d26-f7c6-49e9-b0a0-84bdcfc21349",
                   story_id=43,
                   associated_members_ra=[
                       "22017310",
                       "19017310",
                       "21010757",
                       "19017311"
                   ],
                   stack_tags=[
                       STACK.INTERNAL
                   ],
                   action_type_tag=ACTION_TYPE.PRESENTATION,
                   project_code="MF",
                   title="Revisão",
                   description="Planning Meeting",
                   start_date=1637046000000,
                   end_date=1678676000000,
                   duration=41630000000),
            Action(owner_ra="10017310",
                   action_id="87d4a661-0752-4ce2-9440-05e752e636fc",
                   story_id=932,
                   associated_members_ra=[
                       "21010757",
                       "17033730",
                       "19017310",
                       "23017310"
                   ],
                   stack_tags=[
                       STACK.INFRA
                   ],
                   action_type_tag=ACTION_TYPE.LEARN,
                   project_code="MF",
                   title="Desenvolvimento",
                   description="Revisão de sprint",
                   start_date=1663116000000,
                   end_date=1683606000000,
                   duration=20490000000)
        ]
        self.associated_actions = [
            AssociatedAction(member_ra='10017310',
                             action_id='5f4f13df-e7d3-4a10-9219-197ceae9e3f0',
                             start_date=1644256000000),
            AssociatedAction(member_ra='23017310',
                             action_id='5f4f13df-e7d3-4a10-9219-197ceae9e3f0',
                             start_date=1644256000000),
            AssociatedAction(member_ra='21010757',
                             action_id='5f4f13df-e7d3-4a10-9219-197ceae9e3f0',
                             start_date=1644256000000),
            AssociatedAction(member_ra='22017310',
                             action_id='5f4f13df-e7d3-4a10-9219-197ceae9e3f0',
                             start_date=1644256000000),
            AssociatedAction(member_ra='21017310',
                             action_id='5f4f13df-e7d3-4a10-9219-197ceae9e3f0',
                             start_date=1644256000000),
            AssociatedAction(member_ra='19017310',
                             action_id='5f4f13df-e7d3-4a10-9219-197ceae9e3f0',
                             start_date=1644256000000),
            AssociatedAction(member_ra='19017311',
                             action_id='5f4f13df-e7d3-4a10-9219-197ceae9e3f0',
                             start_date=1644256000000),
            AssociatedAction(member_ra='10017310',
                             action_id='24c7d7a3-6560-4652-a8d6-f2e4f3f23460',
                             start_date=1676476000000),
            AssociatedAction(member_ra='19017311',
                             action_id='24c7d7a3-6560-4652-a8d6-f2e4f3f23460',
                             start_date=1676476000000),
            AssociatedAction(member_ra='23017310',
                             action_id='24c7d7a3-6560-4652-a8d6-f2e4f3f23460',
                             start_date=1676476000000),
            AssociatedAction(member_ra='21010757',
                             action_id='24c7d7a3-6560-4652-a8d6-f2e4f3f23460',
                             start_date=1676476000000),
            AssociatedAction(member_ra='10017310',
                             action_id='42e01f11-283c-4925-b0aa-e80ac6c1815a',
                             start_date=1641896000000),
            AssociatedAction(member_ra='21017310',
                             action_id='42e01f11-283c-4925-b0aa-e80ac6c1815a',
                             start_date=1641896000000),
            AssociatedAction(member_ra='19017310',
                             action_id='42e01f11-283c-4925-b0aa-e80ac6c1815a',
                             start_date=1641896000000),
            AssociatedAction(member_ra='19017311',
                             action_id='42e01f11-283c-4925-b0aa-e80ac6c1815a',
                             start_date=1641896000000),
            AssociatedAction(member_ra='23017310',
                             action_id='42e01f11-283c-4925-b0aa-e80ac6c1815a',
                             start_date=1641896000000),
            AssociatedAction(member_ra='17033730',
                             action_id='42e01f11-283c-4925-b0aa-e80ac6c1815a',
                             start_date=1641896000000),
            AssociatedAction(member_ra='19017311',
                             action_id='ea95d4f7-d5ce-4944-9fa1-ab964655294b',
                             start_date=1658136000000),
            AssociatedAction(member_ra='17033730',
                             action_id='ea95d4f7-d5ce-4944-9fa1-ab964655294b',
                             start_date=1658136000000),
            AssociatedAction(member_ra='22017310',
                             action_id='ea95d4f7-d5ce-4944-9fa1-ab964655294b',
                             start_date=1658136000000),
            AssociatedAction(member_ra='10017310',
                             action_id='ea95d4f7-d5ce-4944-9fa1-ab964655294b',
                             start_date=1658136000000),
            AssociatedAction(member_ra='23017310',
                             action_id='ea95d4f7-d5ce-4944-9fa1-ab964655294b',
                             start_date=1658136000000),
            AssociatedAction(member_ra='21017310',
                             action_id='ea95d4f7-d5ce-4944-9fa1-ab964655294b',
                             start_date=1658136000000),
            AssociatedAction(member_ra='21017310',
                             action_id='7778ee40-d98b-4187-8b02-052b70cc1ec1',
                             start_date=1656666000000),
            AssociatedAction(member_ra='19017311',
                             action_id='7778ee40-d98b-4187-8b02-052b70cc1ec1',
                             start_date=1656666000000),
            AssociatedAction(member_ra='19017310',
                             action_id='7778ee40-d98b-4187-8b02-052b70cc1ec1',
                             start_date=1656666000000),
            AssociatedAction(member_ra='21010757',
                             action_id='92cebaa4-02d5-4618-9b32-0c668b8361cd',
                             start_date=1656646000000),
            AssociatedAction(member_ra='19017310',
                             action_id='eefe6db8-e03e-42c3-9fd2-1de796139501',
                             start_date=1667256000000),
            AssociatedAction(member_ra='23017310',
                             action_id='eefe6db8-e03e-42c3-9fd2-1de796139501',
                             start_date=1667256000000),
            AssociatedAction(member_ra='10017310',
                             action_id='eefe6db8-e03e-42c3-9fd2-1de796139501',
                             start_date=1667256000000),
            AssociatedAction(member_ra='17033730',
                             action_id='eefe6db8-e03e-42c3-9fd2-1de796139501',
                             start_date=1667256000000),
            AssociatedAction(member_ra='19017310',
                             action_id='46b35022-1a68-4cc8-a2e5-ae449e43e867',
                             start_date=1688646000000),
            AssociatedAction(member_ra='10017310',
                             action_id='46b35022-1a68-4cc8-a2e5-ae449e43e867',
                             start_date=1688646000000),
            AssociatedAction(member_ra='23017310',
                             action_id='46b35022-1a68-4cc8-a2e5-ae449e43e867',
                             start_date=1688646000000),
            AssociatedAction(member_ra='19017311',
                             action_id='46b35022-1a68-4cc8-a2e5-ae449e43e867',
                             start_date=1688646000000),
            AssociatedAction(member_ra='17033730',
                             action_id='46b35022-1a68-4cc8-a2e5-ae449e43e867',
                             start_date=1688646000000),
            AssociatedAction(member_ra='22017310',
                             action_id='46b35022-1a68-4cc8-a2e5-ae449e43e867',
                             start_date=1688646000000),
            AssociatedAction(member_ra='10017310',
                             action_id='711d1d26-f7c6-49e9-b0a0-84bdcfc21349',
                             start_date=1637046000000),
            AssociatedAction(member_ra='22017310',
                             action_id='711d1d26-f7c6-49e9-b0a0-84bdcfc21349',
                             start_date=1637046000000),
            AssociatedAction(member_ra='19017310',
                             action_id='711d1d26-f7c6-49e9-b0a0-84bdcfc21349',
                             start_date=1637046000000),
            AssociatedAction(member_ra='21010757',
                             action_id='711d1d26-f7c6-49e9-b0a0-84bdcfc21349',
                             start_date=1637046000000),
            AssociatedAction(member_ra='19017311',
                             action_id='711d1d26-f7c6-49e9-b0a0-84bdcfc21349',
                             start_date=1637046000000),
            AssociatedAction(member_ra='10017310',
                             action_id='87d4a661-0752-4ce2-9440-05e752e636fc',
                             start_date=1663116000000),
            AssociatedAction(member_ra='21010757',
                             action_id='87d4a661-0752-4ce2-9440-05e752e636fc',
                             start_date=1663116000000),
            AssociatedAction(member_ra='17033730',
                             action_id='87d4a661-0752-4ce2-9440-05e752e636fc',
                             start_date=1663116000000),
            AssociatedAction(member_ra='19017310',
                             action_id='87d4a661-0752-4ce2-9440-05e752e636fc',
                             start_date=1663116000000),
            AssociatedAction(member_ra='23017310',
                             action_id='87d4a661-0752-4ce2-9440-05e752e636fc',
                             start_date=1663116000000)
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
        self.associated_actions.append(associatedAction)
        return associatedAction

    def create_project(self, project: Project) -> Optional[Project]:
        self.projects.append(project)
        return project

    def delete_project(self, code: str) -> Project:
        for i in range(len(self.projects)):
            if self.projects[i].code == code:
                return self.projects.pop(i)
        return None

    def get_project(self, code: str) -> Project:
        for project in self.projects:
            if project.code == code:
                return project
        return None
    
    def update_project(self, code: str, new_name: Optional[str] = None, new_description: Optional[str] = None, new_po_RA: Optional[str] = None, new_scrum_RA: Optional[str] = None, new_photos: Optional[List[str]] = None, new_members: Optional[List[str]] = None) -> Project:
        for project in self.projects:
            if project.code == code:
                if new_name is not None:
                    project.name = new_name
                if new_description is not None:
                    project.description = new_description
                if new_po_RA is not None:
                    project.change_po_RA(new_po_RA)
                if new_scrum_RA is not None:
                    project.change_scrum_RA(new_scrum_RA)
                if new_photos is not None:
                    project.photos = new_photos
                if new_members is not None:
                    project.members = new_members

                return project
            
        return None
    
    def get_all_projects(self) -> List[Project]:
        return self.projects

    def get_all_members(self) -> List[Member]:
        return self.members

    def get_member(self, ra: str) -> Member:
        for member in self.members:
            if member.ra == ra:
                return member
        return None
    
    def get_associated_actions_by_ra(self, ra: str, amount: int, start: Optional[int] = None, end: Optional[int] = None, exclusive_start_key: Optional[dict] = None) -> Tuple[List[AssociatedAction], Optional[dict]]:
        associated_actions = sorted(self.associated_actions, key=lambda x: x.start_date, reverse=True)
        associated_actions = list(filter(lambda x: x.member_ra == ra, associated_actions))
        if exclusive_start_key:
            action0 = associated_actions[0]
            while action0 is not None and action0.action_id != exclusive_start_key["action_id"]:
                associated_actions.pop(0)
                action0 = associated_actions[0] if len(associated_actions) > 0 else None
            associated_actions.pop(0) if len(associated_actions) > 0 else None
        if start:
            associated_actions = list(filter(lambda x: x.start_date >= start, associated_actions))
        if end:
            associated_actions = list(filter(lambda x: x.start_date <= end, associated_actions))
        
        
        return associated_actions[:amount]
    
    def batch_get_action(self, action_ids: List[str]) -> List[Action]:
        actions = []
        for action in self.actions:
            if action.action_id in action_ids:
                actions.append(action)
        return actions
    
    def batch_update_associated_action_start(self, action_id: str, new_start_date: int) -> List[AssociatedAction]:
        new_associated_actions = []
        
        for associated_action in self.associated_actions:
            if associated_action.action_id == action_id:
                associated_action.start_date = new_start_date
                new_associated_actions.append(associated_action)
        
        return new_associated_actions
    
    def batch_update_associated_action_members(self, action_id: str, members: List[str], start_date: int) -> List[AssociatedAction]:
        new_associated_actions = []  
        for associated_action in self.associated_actions[:]:
            if associated_action.action_id == action_id:
                self.associated_actions.remove(associated_action)
                
        for member in members:
            self.associated_actions.append(AssociatedAction(member_ra=member, action_id=action_id, start_date=start_date))
        
        return new_associated_actions
    
    def update_action(self, action_id: str, new_owner_ra: Optional[str] = None, new_start_date: Optional[int] = None, new_end_date: Optional[int] = None, new_duration: Optional[int] = None, new_story_id: Optional[str] = None, new_title: Optional[str] = None, new_description: Optional[str] = None, new_project_code: Optional[str] = None, new_associated_members_ra: Optional[List[str]] = None, new_stack_tags: Optional[List[str]] = None, new_action_type_tag: Optional[str] = None) -> Action:
        new_action = None
        for action in self.actions:
            if action.action_id == action_id:
                if new_owner_ra is not None:
                    action.owner_ra = new_owner_ra
                if new_start_date is not None:
                    action.start_date = new_start_date
                if new_end_date is not None:
                    action.end_date = new_end_date
                if new_duration is not None:
                    action.duration = new_duration
                if new_story_id is not -1:
                    action.story_id = new_story_id
                if new_title is not None:
                    action.title = new_title
                if new_description is not '':
                    action.description = new_description
                if new_project_code is not None:
                    action.project_code = new_project_code
                if new_associated_members_ra is not None:
                    action.associated_members_ra = new_associated_members_ra
                if new_stack_tags is not None:
                    action.stack_tags = new_stack_tags
                if new_action_type_tag is not None:
                    action.action_type_tag = new_action_type_tag
                new_action = action
        
        return new_action
    
    def batch_get_member(self, ras: List[str]) -> List[Member]:
        members = []
        for member in self.members:
            if member.ra in ras:
                members.append(member)
        return members