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
        
        self.actions =[
   Action(owner_ra='10017310',
   action_id='c9ba9a91-4c47-4624-8d6f-dd4acf2feaa2',
   story_id=880,
   associated_members_ra=[
      '21010757',
      '19017311',
      '22017310'
   ],
   stack_tags=[
      STACK.BACKEND
   ],
   action_type_tag=ACTION_TYPE.WORK,
   project_code='SF',
   title='Review',
   description='Planning',
   start_date=1673026000000,
   end_date=1681366000000,
   duration=8340000000),
   Action(owner_ra='10017310',
   action_id='282f56ae-56e4-41af-96fa-3b152c6dc32a',
   story_id=901,
   associated_members_ra=[
      
   ],
   stack_tags=[
      STACK.INFRA
   ],
   action_type_tag=ACTION_TYPE.MEETING,
   project_code='MF',
   title='Planning Meeting',
   description='Sprint Review',
   start_date=1641226000000,
   end_date=1661066000000,
   duration=19840000000),
   Action(owner_ra='19017311',
   action_id='09f84c82-eb1a-4bb2-a13e-4da8160ee4b2',
   story_id=625,
   associated_members_ra=[
      '23017310',
      '21010757',
      '17033730'
   ],
   stack_tags=[
      STACK.DATA_SCIENCE
   ],
   action_type_tag=ACTION_TYPE.WORK,
   project_code='PT',
   title='Sprint Planning',
   description='Sprint Review',
   start_date=1655706000000,
   end_date=1676366000000,
   duration=20660000000),
   Action(owner_ra='21010757',
   action_id='6b09b903-edb1-4e9e-99c4-eff5f9c4d9a5',
   story_id=442,
   associated_members_ra=[
      '22017310'
   ],
   stack_tags=[
      STACK.PO
   ],
   action_type_tag=ACTION_TYPE.MEETING,
   project_code='SF',
   title='Planning Meeting',
   description='Front-End',
   start_date=1674306000000,
   end_date=1687046000000,
   duration=12740000000),
   Action(owner_ra='19017311',
   action_id='2e29e827-954b-4e58-9bf4-0bfea1823990',
   story_id=904,
   associated_members_ra=[
      '22017310',
      '10017310'
   ],
   stack_tags=[
      STACK.INFRA
   ],
   action_type_tag=ACTION_TYPE.PRESENTATION,
   project_code='MF',
   title='Sprint Review',
   description='Revisão de sprint',
   start_date=1656316000000,
   end_date=1659096000000,
   duration=2780000000),
   Action(owner_ra='21010757',
   action_id='3c5a4c97-d3d0-4aec-bea6-b39813b09243',
   story_id=805,
   associated_members_ra=[
      
   ],
   stack_tags=[
      STACK.DATA_SCIENCE
   ],
   action_type_tag=ACTION_TYPE.CODE,
   project_code='SF',
   title='Sprint Planning',
   description='Sprint Planning',
   start_date=1656986000000,
   end_date=1679146000000,
   duration=22160000000),
   Action(owner_ra='21010757',
   action_id='1abc4def-c89e-4914-b725-ec951cf215c0',
   story_id=515,
   associated_members_ra=[
      
   ],
   stack_tags=[
      STACK.BACKEND
   ],
   action_type_tag=ACTION_TYPE.CODEREVIEW,
   project_code='MF',
   title='Desenvolvimento',
   description='Revisão de sprint',
   start_date=1664876000000,
   end_date=1677066000000,
   duration=12190000000),
   Action(owner_ra='19017311',
   action_id='5b81fbe1-df7f-4734-8392-e20220373357',
   story_id=91,
   associated_members_ra=[
      
   ],
   stack_tags=[
      STACK.BACKEND
   ],
   action_type_tag=ACTION_TYPE.ARCHITECT,
   project_code='SF',
   title='Desenvolvimento',
   description='Planning Meeting',
   start_date=1689276000000,
   end_date=1689976000000,
   duration=700000000),
   Action(owner_ra='10017310',
   action_id='a52281fa-a6d8-4879-9b9d-4aa4164378c0',
   story_id=850,
   associated_members_ra=[
      '21017310'
   ],
   stack_tags=[
      STACK.UX_UI
   ],
   action_type_tag=ACTION_TYPE.DESIGN,
   project_code='PT',
   title='Planning Meeting',
   description='Back-End',
   start_date=1641716000000,
   end_date=1645096000000,
   duration=3380000000),
   Action(owner_ra='10017310',
   action_id='02f26f46-950b-4c0f-b396-e679a97f48b8',
   story_id=473,
   associated_members_ra=[
      '21017310',
      '17033730',
      '22017310',
      '19017310',
      '21010757'
   ],
   stack_tags=[
      STACK.BACKEND
   ],
   action_type_tag=ACTION_TYPE.PRESENTATION,
   project_code='SF',
   title='Reunião',
   description='Daily',
   start_date=1639616000000,
   end_date=1682736000000,
   duration=43120000000),
   Action(owner_ra='17033730',
   action_id='1c767341-6ca3-4369-8b1d-4254d3bcb359',
   story_id=930,
   associated_members_ra=[
      '19017310',
      '23017310',
      '21017310',
      '19017311',
      '22017310'
   ],
   stack_tags=[
      STACK.FRONTEND
   ],
   action_type_tag=ACTION_TYPE.MEETING,
   project_code='GM',
   title='Retrospective',
   description='Planning Meeting',
   start_date=1656236000000,
   end_date=1656396000000,
   duration=160000000),
   Action(owner_ra='21010757',
   action_id='40bd995c-8fa4-4ba6-a2e4-a933e89a9eb0',
   story_id=424,
   associated_members_ra=[
      
   ],
   stack_tags=[
      STACK.INTERNAL
   ],
   action_type_tag=ACTION_TYPE.WORK,
   project_code='GM',
   title='Planning',
   description='Reunião de planning',
   start_date=1646336000000,
   end_date=1687936000000,
   duration=41600000000),
   Action(owner_ra='22017310',
   action_id='91e2692b-9639-48ff-86cd-178fd35a09a6',
   story_id=70,
   associated_members_ra=[
      '17033730',
      '21010757'
   ],
   stack_tags=[
      STACK.UX_UI
   ],
   action_type_tag=ACTION_TYPE.LEARN,
   project_code='SM',
   title='Daily',
   description='Back-End',
   start_date=1687086000000,
   end_date=1690266000000,
   duration=3180000000),
   Action(owner_ra='19017310',
   action_id='4c8fd85a-394c-4981-a140-39e9a119459f',
   story_id=301,
   associated_members_ra=[
      
   ],
   stack_tags=[
      STACK.PO
   ],
   action_type_tag=ACTION_TYPE.LEARN,
   project_code='SF',
   title='Daily',
   description='Planning',
   start_date=1681986000000,
   end_date=1688246000000,
   duration=6260000000),
   Action(owner_ra='17033730',
   action_id='521783a3-6748-4480-8a28-d85c9354b1a6',
   story_id=89,
   associated_members_ra=[
      '10017310',
      '21017310',
      '19017311'
   ],
   stack_tags=[
      STACK.DATA_SCIENCE
   ],
   action_type_tag=ACTION_TYPE.PRESENTATION,
   project_code='SF',
   title='Sprint Review',
   description='Sprint Planning',
   start_date=1658396000000,
   end_date=1662866000000,
   duration=4470000000),
   Action(owner_ra='22017310',
   action_id='9c3381b0-2360-4c6a-9089-b38b7be8cd50',
   story_id=317,
   associated_members_ra=[
      '23017310',
      '19017311',
      '19017310',
      '17033730',
      '21010757',
      '10017310'
   ],
   stack_tags=[
      STACK.DATA_SCIENCE
   ],
   action_type_tag=ACTION_TYPE.PRESENTATION,
   project_code='PT',
   title='Planning Meeting',
   description='Back-End',
   start_date=1634566000000,
   end_date=1643786000000,
   duration=9220000000),
   Action(owner_ra='19017310',
   action_id='a95d4d1e-b3d3-4a4d-80dc-bea7d66db42b',
   story_id=340,
   associated_members_ra=[
      '19017311',
      '21010757',
      '17033730'
   ],
   stack_tags=[
      STACK.PO
   ],
   action_type_tag=ACTION_TYPE.PRESENTATION,
   project_code='SM',
   title='Retrospective',
   description='Finalização de sprint',
   start_date=1666036000000,
   end_date=1666296000000,
   duration=260000000),
   Action(owner_ra='21017310',
   action_id='631c0afd-de91-4cee-9ead-41152f471abf',
   story_id=802,
   associated_members_ra=[
      '22017310',
      '17033730',
      '21010757',
      '10017310',
      '19017311'
   ],
   stack_tags=[
      STACK.INFRA
   ],
   action_type_tag=ACTION_TYPE.CODEREVIEW,
   project_code='MF',
   title='Daily',
   description='Planejamento de sprint',
   start_date=1669886000000,
   end_date=1673976000000,
   duration=4090000000),
   Action(owner_ra='17033730',
   action_id='4471736a-3ece-442f-864b-6e7ea7a89064',
   story_id=298,
   associated_members_ra=[
      '21017310',
      '22017310',
      '10017310',
      '21010757',
      '19017310'
   ],
   stack_tags=[
      STACK.INFRA
   ],
   action_type_tag=ACTION_TYPE.CODE,
   project_code='PT',
   title='Sprint Retrospective',
   description='Retrospective',
   start_date=1649946000000,
   end_date=1670696000000,
   duration=20750000000),
   Action(owner_ra='10017310',
   action_id='61029249-e94b-446e-98a7-e92a7bbb2047',
   story_id=511,
   associated_members_ra=[
      '19017311',
      '21017310',
      '22017310',
      '21010757'
   ],
   stack_tags=[
      STACK.INTERNAL
   ],
   action_type_tag=ACTION_TYPE.ARCHITECT,
   project_code='MF',
   title='Daily',
   description='Daily',
   start_date=1648216000000,
   end_date=1660416000000,
   duration=12200000000)
]
        self.associatedActions =[
   AssociatedAction(member_ra='10017310',
   action_id='c9ba9a91-4c47-4624-8d6f-dd4acf2feaa2'),
   AssociatedAction(member_ra='21010757',
   action_id='c9ba9a91-4c47-4624-8d6f-dd4acf2feaa2'),
   AssociatedAction(member_ra='19017311',
   action_id='c9ba9a91-4c47-4624-8d6f-dd4acf2feaa2'),
   AssociatedAction(member_ra='22017310',
   action_id='c9ba9a91-4c47-4624-8d6f-dd4acf2feaa2'),
   AssociatedAction(member_ra='10017310',
   action_id='282f56ae-56e4-41af-96fa-3b152c6dc32a'),
   AssociatedAction(member_ra='19017311',
   action_id='09f84c82-eb1a-4bb2-a13e-4da8160ee4b2'),
   AssociatedAction(member_ra='23017310',
   action_id='09f84c82-eb1a-4bb2-a13e-4da8160ee4b2'),
   AssociatedAction(member_ra='21010757',
   action_id='09f84c82-eb1a-4bb2-a13e-4da8160ee4b2'),
   AssociatedAction(member_ra='17033730',
   action_id='09f84c82-eb1a-4bb2-a13e-4da8160ee4b2'),
   AssociatedAction(member_ra='21010757',
   action_id='6b09b903-edb1-4e9e-99c4-eff5f9c4d9a5'),
   AssociatedAction(member_ra='22017310',
   action_id='6b09b903-edb1-4e9e-99c4-eff5f9c4d9a5'),
   AssociatedAction(member_ra='19017311',
   action_id='2e29e827-954b-4e58-9bf4-0bfea1823990'),
   AssociatedAction(member_ra='22017310',
   action_id='2e29e827-954b-4e58-9bf4-0bfea1823990'),
   AssociatedAction(member_ra='10017310',
   action_id='2e29e827-954b-4e58-9bf4-0bfea1823990'),
   AssociatedAction(member_ra='21010757',
   action_id='3c5a4c97-d3d0-4aec-bea6-b39813b09243'),
   AssociatedAction(member_ra='21010757',
   action_id='1abc4def-c89e-4914-b725-ec951cf215c0'),
   AssociatedAction(member_ra='19017311',
   action_id='5b81fbe1-df7f-4734-8392-e20220373357'),
   AssociatedAction(member_ra='10017310',
   action_id='a52281fa-a6d8-4879-9b9d-4aa4164378c0'),
   AssociatedAction(member_ra='21017310',
   action_id='a52281fa-a6d8-4879-9b9d-4aa4164378c0'),
   AssociatedAction(member_ra='10017310',
   action_id='02f26f46-950b-4c0f-b396-e679a97f48b8'),
   AssociatedAction(member_ra='21017310',
   action_id='02f26f46-950b-4c0f-b396-e679a97f48b8'),
   AssociatedAction(member_ra='17033730',
   action_id='02f26f46-950b-4c0f-b396-e679a97f48b8'),
   AssociatedAction(member_ra='22017310',
   action_id='02f26f46-950b-4c0f-b396-e679a97f48b8'),
   AssociatedAction(member_ra='19017310',
   action_id='02f26f46-950b-4c0f-b396-e679a97f48b8'),
   AssociatedAction(member_ra='21010757',
   action_id='02f26f46-950b-4c0f-b396-e679a97f48b8'),
   AssociatedAction(member_ra='17033730',
   action_id='1c767341-6ca3-4369-8b1d-4254d3bcb359'),
   AssociatedAction(member_ra='19017310',
   action_id='1c767341-6ca3-4369-8b1d-4254d3bcb359'),
   AssociatedAction(member_ra='23017310',
   action_id='1c767341-6ca3-4369-8b1d-4254d3bcb359'),
   AssociatedAction(member_ra='21017310',
   action_id='1c767341-6ca3-4369-8b1d-4254d3bcb359'),
   AssociatedAction(member_ra='19017311',
   action_id='1c767341-6ca3-4369-8b1d-4254d3bcb359'),
   AssociatedAction(member_ra='22017310',
   action_id='1c767341-6ca3-4369-8b1d-4254d3bcb359'),
   AssociatedAction(member_ra='21010757',
   action_id='40bd995c-8fa4-4ba6-a2e4-a933e89a9eb0'),
   AssociatedAction(member_ra='22017310',
   action_id='91e2692b-9639-48ff-86cd-178fd35a09a6'),
   AssociatedAction(member_ra='17033730',
   action_id='91e2692b-9639-48ff-86cd-178fd35a09a6'),
   AssociatedAction(member_ra='21010757',
   action_id='91e2692b-9639-48ff-86cd-178fd35a09a6'),
   AssociatedAction(member_ra='19017310',
   action_id='4c8fd85a-394c-4981-a140-39e9a119459f'),
   AssociatedAction(member_ra='17033730',
   action_id='521783a3-6748-4480-8a28-d85c9354b1a6'),
   AssociatedAction(member_ra='10017310',
   action_id='521783a3-6748-4480-8a28-d85c9354b1a6'),
   AssociatedAction(member_ra='21017310',
   action_id='521783a3-6748-4480-8a28-d85c9354b1a6'),
   AssociatedAction(member_ra='19017311',
   action_id='521783a3-6748-4480-8a28-d85c9354b1a6'),
   AssociatedAction(member_ra='22017310',
   action_id='9c3381b0-2360-4c6a-9089-b38b7be8cd50'),
   AssociatedAction(member_ra='23017310',
   action_id='9c3381b0-2360-4c6a-9089-b38b7be8cd50'),
   AssociatedAction(member_ra='19017311',
   action_id='9c3381b0-2360-4c6a-9089-b38b7be8cd50'),
   AssociatedAction(member_ra='19017310',
   action_id='9c3381b0-2360-4c6a-9089-b38b7be8cd50'),
   AssociatedAction(member_ra='17033730',
   action_id='9c3381b0-2360-4c6a-9089-b38b7be8cd50'),
   AssociatedAction(member_ra='21010757',
   action_id='9c3381b0-2360-4c6a-9089-b38b7be8cd50'),
   AssociatedAction(member_ra='10017310',
   action_id='9c3381b0-2360-4c6a-9089-b38b7be8cd50'),
   AssociatedAction(member_ra='19017310',
   action_id='a95d4d1e-b3d3-4a4d-80dc-bea7d66db42b'),
   AssociatedAction(member_ra='19017311',
   action_id='a95d4d1e-b3d3-4a4d-80dc-bea7d66db42b'),
   AssociatedAction(member_ra='21010757',
   action_id='a95d4d1e-b3d3-4a4d-80dc-bea7d66db42b'),
   AssociatedAction(member_ra='17033730',
   action_id='a95d4d1e-b3d3-4a4d-80dc-bea7d66db42b'),
   AssociatedAction(member_ra='21017310',
   action_id='631c0afd-de91-4cee-9ead-41152f471abf'),
   AssociatedAction(member_ra='22017310',
   action_id='631c0afd-de91-4cee-9ead-41152f471abf'),
   AssociatedAction(member_ra='17033730',
   action_id='631c0afd-de91-4cee-9ead-41152f471abf'),
   AssociatedAction(member_ra='21010757',
   action_id='631c0afd-de91-4cee-9ead-41152f471abf'),
   AssociatedAction(member_ra='10017310',
   action_id='631c0afd-de91-4cee-9ead-41152f471abf'),
   AssociatedAction(member_ra='19017311',
   action_id='631c0afd-de91-4cee-9ead-41152f471abf'),
   AssociatedAction(member_ra='17033730',
   action_id='4471736a-3ece-442f-864b-6e7ea7a89064'),
   AssociatedAction(member_ra='21017310',
   action_id='4471736a-3ece-442f-864b-6e7ea7a89064'),
   AssociatedAction(member_ra='22017310',
   action_id='4471736a-3ece-442f-864b-6e7ea7a89064'),
   AssociatedAction(member_ra='10017310',
   action_id='4471736a-3ece-442f-864b-6e7ea7a89064'),
   AssociatedAction(member_ra='21010757',
   action_id='4471736a-3ece-442f-864b-6e7ea7a89064'),
   AssociatedAction(member_ra='19017310',
   action_id='4471736a-3ece-442f-864b-6e7ea7a89064'),
   AssociatedAction(member_ra='10017310',
   action_id='61029249-e94b-446e-98a7-e92a7bbb2047'),
   AssociatedAction(member_ra='19017311',
   action_id='61029249-e94b-446e-98a7-e92a7bbb2047'),
   AssociatedAction(member_ra='21017310',
   action_id='61029249-e94b-446e-98a7-e92a7bbb2047'),
   AssociatedAction(member_ra='22017310',
   action_id='61029249-e94b-446e-98a7-e92a7bbb2047'),
   AssociatedAction(member_ra='21010757',
   action_id='61029249-e94b-446e-98a7-e92a7bbb2047')
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