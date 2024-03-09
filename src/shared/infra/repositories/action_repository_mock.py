from typing import List, Optional, Tuple
from src.shared.domain.repositories.action_repository_interface import IActionRepository
from src.shared.domain.entities.action import Action
from src.shared.domain.entities.project import Project
from src.shared.domain.entities.associated_action import AssociatedAction
from src.shared.domain.enums.stack_enum import STACK
from src.shared.domain.enums.action_type_enum import ACTION_TYPE


class ActionRepositoryMock(IActionRepository):
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


        self.actions = [
            Action(owner_ra="10017310",
                   action_id="5f4f13df-e7d3-4a10-9219-197ceae9e3f0",
                   user_id="6f5g4h7J-876j-0098-123hb-hgb567fy4hb",
                   story_id=94,
                   is_valid=True,
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
                   user_id="6f5g4h7J-876j-0098-123hb-hgb567fy4hb",
                   story_id=368,
                   is_valid=True,
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
                   user_id="6f5g4h7J-876j-0098-123hb-hgb567fy4hb",
                   story_id=983,
                   is_valid=True,
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
                   user_id="7gh5yf5H-857H-1234-75hng-94832hvng1s",
                   story_id=435,
                   is_valid=True,
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
                   user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                   story_id=848,
                   is_valid=True,
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
                   user_id="51ah5jaj-c9jm-1345-666ab-e12341c14a3",
                   story_id=144,
                   is_valid=True,
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
                   user_id="6574hgyt-785n-9134-18gn4-7gh5uvn36cG",
                   story_id=497,
                   is_valid=True,
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
                   user_id="6574hgyt-785n-9134-18gn4-7gh5uvn36cG",
                   story_id=237,
                   is_valid=True,
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
                   user_id="6f5g4h7J-876j-0098-123hb-hgb567fy4hb",
                   story_id=43,
                   is_valid=True,
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
                   user_id="6f5g4h7J-876j-0098-123hb-hgb567fy4hb",
                   story_id=932,
                   is_valid=True,
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
                             start_date=1644256000000,
                             user_id="6f5g4h7J-876j-0098-123hb-hgb567fy4hb"),
            AssociatedAction(member_ra='23017310',
                             action_id='5f4f13df-e7d3-4a10-9219-197ceae9e3f0',
                             start_date=1644256000000,
                             user_id="75648hbr-184n-1985-91han-7ghn4HgF182"),
            AssociatedAction(member_ra='21010757',
                             action_id='5f4f13df-e7d3-4a10-9219-197ceae9e3f0',
                             start_date=1644256000000,
                             user_id="51ah5jaj-c9jm-1345-666ab-e12341c14a3"),
            AssociatedAction(member_ra='22017310',
                             action_id='5f4f13df-e7d3-4a10-9219-197ceae9e3f0',
                             start_date=1644256000000,
                              user_id="76h35dg4-h76v-1875-987hn-h67gfv45Gt4"),
            AssociatedAction(member_ra='21017310',
                             action_id='5f4f13df-e7d3-4a10-9219-197ceae9e3f0',
                             start_date=1644256000000,
                             user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3"),
            AssociatedAction(member_ra='19017310',
                             action_id='5f4f13df-e7d3-4a10-9219-197ceae9e3f0',
                             start_date=1644256000000,
                             user_id="6574hgyt-785n-9134-18gn4-7gh5uvn36cG"),
            AssociatedAction(member_ra='19017311',
                             action_id='5f4f13df-e7d3-4a10-9219-197ceae9e3f0',
                             start_date=1644256000000,
                             user_id="7gh5yf5H-857H-1234-75hng-94832hvng1s"),
            AssociatedAction(member_ra='10017310',
                             action_id='24c7d7a3-6560-4652-a8d6-f2e4f3f23460',
                             start_date=1676476000000,
                             user_id="6f5g4h7J-876j-0098-123hb-hgb567fy4hb"),
            AssociatedAction(member_ra='19017311',
                             action_id='24c7d7a3-6560-4652-a8d6-f2e4f3f23460',
                             start_date=1676476000000,
                             user_id="7gh5yf5H-857H-1234-75hng-94832hvng1s"),
            AssociatedAction(member_ra='23017310',
                             action_id='24c7d7a3-6560-4652-a8d6-f2e4f3f23460',
                             start_date=1676476000000,
                             user_id="75648hbr-184n-1985-91han-7ghn4HgF182"),
            AssociatedAction(member_ra='21010757',
                             action_id='24c7d7a3-6560-4652-a8d6-f2e4f3f23460',
                             start_date=1676476000000,
                             user_id="51ah5jaj-c9jm-1345-666ab-e12341c14a3"),
            AssociatedAction(member_ra='10017310',
                             action_id='42e01f11-283c-4925-b0aa-e80ac6c1815a',
                             start_date=1641896000000,
                             user_id="6f5g4h7J-876j-0098-123hb-hgb567fy4hb"),
            AssociatedAction(member_ra='21017310',
                             action_id='42e01f11-283c-4925-b0aa-e80ac6c1815a',
                             start_date=1641896000000,
                             user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3"),
            AssociatedAction(member_ra='19017310',
                             action_id='42e01f11-283c-4925-b0aa-e80ac6c1815a',
                             start_date=1641896000000,
                             user_id="6574hgyt-785n-9134-18gn4-7gh5uvn36cG"),
            AssociatedAction(member_ra='19017311',
                             action_id='42e01f11-283c-4925-b0aa-e80ac6c1815a',
                             start_date=1641896000000,
                             user_id="7gh5yf5H-857H-1234-75hng-94832hvng1s"),
            AssociatedAction(member_ra='23017310',
                             action_id='42e01f11-283c-4925-b0aa-e80ac6c1815a',
                             start_date=1641896000000,
                             user_id="75648hbr-184n-1985-91han-7ghn4HgF182"),
            AssociatedAction(member_ra='17033730',
                             action_id='42e01f11-283c-4925-b0aa-e80ac6c1815a',
                             start_date=1641896000000,
                             user_id="7465hvnb-143g-1675-86HnG-75hgnFbcg36"),
            AssociatedAction(member_ra='19017311',
                             action_id='ea95d4f7-d5ce-4944-9fa1-ab964655294b',
                             start_date=1658136000000,
                             user_id="7gh5yf5H-857H-1234-75hng-94832hvng1s"),
            AssociatedAction(member_ra='17033730',
                             action_id='ea95d4f7-d5ce-4944-9fa1-ab964655294b',
                             start_date=1658136000000,
                             user_id="7465hvnb-143g-1675-86HnG-75hgnFbcg36"),
            AssociatedAction(member_ra='22017310',
                             action_id='ea95d4f7-d5ce-4944-9fa1-ab964655294b',
                             start_date=1658136000000,
                             user_id="76h35dg4-h76v-1875-987hn-h67gfv45Gt4"),
            AssociatedAction(member_ra='10017310',
                             action_id='ea95d4f7-d5ce-4944-9fa1-ab964655294b',
                             start_date=1658136000000,
                             user_id="6f5g4h7J-876j-0098-123hb-hgb567fy4hb"),
            AssociatedAction(member_ra='23017310',
                             action_id='ea95d4f7-d5ce-4944-9fa1-ab964655294b',
                             start_date=1658136000000,
                             user_id="75648hbr-184n-1985-91han-7ghn4HgF182"),
            AssociatedAction(member_ra='21017310',
                             action_id='ea95d4f7-d5ce-4944-9fa1-ab964655294b',
                             start_date=1658136000000,
                             user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3"),
            AssociatedAction(member_ra='21017310',
                             action_id='7778ee40-d98b-4187-8b02-052b70cc1ec1',
                             start_date=1656666000000,
                             user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3"),
            AssociatedAction(member_ra='19017311',
                             action_id='7778ee40-d98b-4187-8b02-052b70cc1ec1',
                             start_date=1656666000000,
                             user_id="7gh5yf5H-857H-1234-75hng-94832hvng1s"),
            AssociatedAction(member_ra='19017310',
                             action_id='7778ee40-d98b-4187-8b02-052b70cc1ec1',
                             start_date=1656666000000,
                             user_id="6574hgyt-785n-9134-18gn4-7gh5uvn36cG"),
            AssociatedAction(member_ra='21010757',
                             action_id='92cebaa4-02d5-4618-9b32-0c668b8361cd',
                             start_date=1656646000000,
                             user_id="51ah5jaj-c9jm-1345-666ab-e12341c14a3"),
            AssociatedAction(member_ra='19017310',
                             action_id='eefe6db8-e03e-42c3-9fd2-1de796139501',
                             start_date=1667256000000,
                             user_id="6574hgyt-785n-9134-18gn4-7gh5uvn36cG"),
            AssociatedAction(member_ra='23017310',
                             action_id='eefe6db8-e03e-42c3-9fd2-1de796139501',
                             start_date=1667256000000,
                             user_id="75648hbr-184n-1985-91han-7ghn4HgF182"),
            AssociatedAction(member_ra='10017310',
                             action_id='eefe6db8-e03e-42c3-9fd2-1de796139501',
                             start_date=1667256000000,
                             user_id="6f5g4h7J-876j-0098-123hb-hgb567fy4hb"),
            AssociatedAction(member_ra='17033730',
                             action_id='eefe6db8-e03e-42c3-9fd2-1de796139501',
                             start_date=1667256000000,
                             user_id="7465hvnb-143g-1675-86HnG-75hgnFbcg36"),
            AssociatedAction(member_ra='19017310',
                             action_id='46b35022-1a68-4cc8-a2e5-ae449e43e867',
                             start_date=1688646000000,
                             user_id="6574hgyt-785n-9134-18gn4-7gh5uvn36cG"),
            AssociatedAction(member_ra='10017310',
                             action_id='46b35022-1a68-4cc8-a2e5-ae449e43e867',
                             start_date=1688646000000,
                             user_id="6f5g4h7J-876j-0098-123hb-hgb567fy4hb"),
            AssociatedAction(member_ra='23017310',
                             action_id='46b35022-1a68-4cc8-a2e5-ae449e43e867',
                             start_date=1688646000000,
                             user_id="75648hbr-184n-1985-91han-7ghn4HgF182"),
            AssociatedAction(member_ra='19017311',
                             action_id='46b35022-1a68-4cc8-a2e5-ae449e43e867',
                             start_date=1688646000000,
                             user_id="7gh5yf5H-857H-1234-75hng-94832hvng1s"),
            AssociatedAction(member_ra='17033730',
                             action_id='46b35022-1a68-4cc8-a2e5-ae449e43e867',
                             start_date=1688646000000,
                             user_id="7465hvnb-143g-1675-86HnG-75hgnFbcg36"),
            AssociatedAction(member_ra='22017310',
                             action_id='46b35022-1a68-4cc8-a2e5-ae449e43e867',
                             start_date=1688646000000,
                             user_id="76h35dg4-h76v-1875-987hn-h67gfv45Gt4"),
            AssociatedAction(member_ra='10017310',
                             action_id='711d1d26-f7c6-49e9-b0a0-84bdcfc21349',
                             start_date=1637046000000,
                             user_id="6f5g4h7J-876j-0098-123hb-hgb567fy4hb"),
            AssociatedAction(member_ra='22017310',
                             action_id='711d1d26-f7c6-49e9-b0a0-84bdcfc21349',
                             start_date=1637046000000,
                             user_id="76h35dg4-h76v-1875-987hn-h67gfv45Gt4"),
            AssociatedAction(member_ra='19017310',
                             action_id='711d1d26-f7c6-49e9-b0a0-84bdcfc21349',
                             start_date=1637046000000,
                             user_id="6574hgyt-785n-9134-18gn4-7gh5uvn36cG"),
            AssociatedAction(member_ra='21010757',
                             action_id='711d1d26-f7c6-49e9-b0a0-84bdcfc21349',
                             start_date=1637046000000,
                             user_id="51ah5jaj-c9jm-1345-666ab-e12341c14a3"),
            AssociatedAction(member_ra='19017311',
                             action_id='711d1d26-f7c6-49e9-b0a0-84bdcfc21349',
                             start_date=1637046000000,
                             user_id="7gh5yf5H-857H-1234-75hng-94832hvng1s"),
            AssociatedAction(member_ra='10017310',
                             action_id='87d4a661-0752-4ce2-9440-05e752e636fc',
                             start_date=1663116000000,
                             user_id="6f5g4h7J-876j-0098-123hb-hgb567fy4hb"),
            AssociatedAction(member_ra='21010757',
                             action_id='87d4a661-0752-4ce2-9440-05e752e636fc',
                             start_date=1663116000000,
                             user_id="51ah5jaj-c9jm-1345-666ab-e12341c14a3"),
            AssociatedAction(member_ra='17033730',
                             action_id='87d4a661-0752-4ce2-9440-05e752e636fc',
                             start_date=1663116000000,
                             user_id="7465hvnb-143g-1675-86HnG-75hgnFbcg36"),
            AssociatedAction(member_ra='19017310',
                             action_id='87d4a661-0752-4ce2-9440-05e752e636fc',
                             start_date=1663116000000,
                             user_id="6574hgyt-785n-9134-18gn4-7gh5uvn36cG"),
            AssociatedAction(member_ra='23017310',
                             action_id='87d4a661-0752-4ce2-9440-05e752e636fc',
                             start_date=1663116000000,
                             user_id="75648hbr-184n-1985-91han-7ghn4HgF182")
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
    
    def get_associated_actions_by_user_id(self, user_id: str, amount: int, start: Optional[int] = None, end: Optional[int] = None, exclusive_start_key: Optional[dict] = None) -> Tuple[List[AssociatedAction], Optional[dict]]:
        associated_actions = sorted(self.associated_actions, key=lambda x: x.start_date, reverse=True)
        associated_actions = list(filter(lambda x: x.user_id == user_id, associated_actions))
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
    
    def batch_update_associated_action_members(self, action_id: str, members: List[str], user_ids: List[str], start_date: int) -> List[AssociatedAction]:
        new_associated_actions = []  
        for associated_action in self.associated_actions[:]:
            if associated_action.action_id == action_id:
                self.associated_actions.remove(associated_action)
                
        for member in members:
            count = 0
            up_associated_action = self.associated_actions.append(AssociatedAction(member_ra=member, action_id=action_id, start_date=start_date, user_id=user_ids[count]))
            count += 1
            new_associated_actions.append(up_associated_action)        
        
        return new_associated_actions
    
    def update_action(self, action_id: str, new_owner_ra: Optional[str] = None, new_user_id: Optional[str] = None, new_start_date: Optional[int] = None, new_end_date: Optional[int] = None, new_duration: Optional[int] = None, new_is_valid: Optional[bool] = None, new_story_id: Optional[str] = None, new_title: Optional[str] = None, new_description: Optional[str] = None, new_project_code: Optional[str] = None, new_associated_members_ra: Optional[List[str]] = None, new_stack_tags: Optional[List[str]] = None, new_action_type_tag: Optional[str] = None) -> Action:
        new_action = None
        for action in self.actions:
            if action.action_id == action_id:
                if new_owner_ra is not None:
                    action.owner_ra = new_owner_ra
                if new_user_id is not None:
                    action.user_id = new_user_id
                if new_start_date is not None:
                    action.start_date = new_start_date
                if new_end_date is not None:
                    action.end_date = new_end_date
                if new_duration is not None:
                    action.duration = new_duration
                if new_story_id is not -1:
                    action.story_id = new_story_id
                if new_is_valid is not None:
                    action.is_valid = new_is_valid
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
    