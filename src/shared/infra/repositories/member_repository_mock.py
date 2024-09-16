import datetime
from typing import List, Optional
from src.shared.domain.enums.active_enum import ACTIVE
from src.shared.domain.enums.course_enum import COURSE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.repositories.member_repository_interface import IMemberRepository
from src.shared.domain.enums.stack_enum import STACK
from src.shared.domain.entities.member import Member


class MemberRepositoryMock(IMemberRepository):
    members: List[Member]


    def __init__(self):


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
                deactivated_date=None,
                user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                photo=None
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
                deactivated_date=None,
                user_id="51ah5jaj-c9jm-1345-666ab-e12341c14a3",
                photo=None
                              
            ),

            Member(
                name="Luigi Televisão",
                email_dev="ltelevisao.devmaua@gmail.com",
                email="lgtv@gmail.com",
                ra="22017310",
                role=ROLE.DEV,
                stack=STACK.BACKEND,
                year=2,
                cellphone="11991758228",
                course=COURSE.CIC,
                hired_date=1640192165000,
                active=ACTIVE.FREEZE,
                deactivated_date=None,
                user_id="76h35dg4-h76v-1875-987hn-h67gfv45Gt4",
                photo=None
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
                deactivated_date=None,
                user_id="6f5g4h7J-876j-0098-123hb-hgb567fy4hb",
                photo=None
            ),

            Member(
                name="Marcos Pereira Neto",
                email_dev="mneto.devmaua@gmail.com",
                email="mneto@gmail.com",
                ra="19017310",
                role=ROLE.PO,
                stack=STACK.BUSINESS,
                year=4,
                cellphone="11991753208",
                course=COURSE.EMC,
                hired_date=1614567601000,
                active=ACTIVE.DISCONNECTED,
                deactivated_date=None,
                user_id="6574hgyt-785n-9134-18gn4-7gh5uvn36cG",
                photo=None
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
                deactivated_date=None,
                user_id="7gh5yf5H-857H-1234-75hng-94832hvng1s",
                photo=None
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
                deactivated_date=None,
                user_id="7465hvnb-143g-1675-86HnG-75hgnFbcg36",
                photo=None
            ),

            Member(
                name="Henrique Gustavo de Souza",
                email_dev="hsouza.devmaua@gmail.com",
                email="hsouza@gmail.com",
                ra="22015320",
                role=ROLE.DEV,
                stack=STACK.UX_UI,
                year=1,
                cellphone="11991123498",
                course=COURSE.ECM,
                hired_date=1672592165000,
                active=ACTIVE.ACTIVE,
                deactivated_date=None,
                user_id="75648hbr-184n-1985-91han-7ghn4HgF182",
                photo=None
            )
            ,

            Member(
                name="Joao Pedro Soares",
                email_dev="jp.devmaua@gmail.com",
                email="jp@gmail.com",
                ra="21004102",
                role=ROLE.DEV,
                stack=STACK.UX_UI,
                year=1,
                cellphone="11991123498",
                course=COURSE.ECM,
                hired_date=1672592165000,
                active=ACTIVE.ACTIVE,
                deactivated_date=None,
                user_id="9183jBnh-997H-1010-10god-914gHy46tBh",
                photo=None
            )
            ,

            Member(
                name = "Fernandao Presidas",
                email_dev = "fernandinho.devmaua@gmail.com",
                email = "fernandao@gmail.com",
                ra = "22014322",
                role = ROLE.PO,
                stack = STACK.BUSINESS,
                year = 3,
                cellphone = "11991123498",
                course = COURSE.EPM,
                hired_date = 1640192165000,
                active = ACTIVE.ACTIVE,
                deactivated_date = None,
                user_id = "5f55f6a5-a66e-4fff-9faf-72cd478bd5a0",
                photo=None
            )
            ,
            
            Member(
                name = "Carlinhos Miau",
                email_dev = "carlinhos.devmaua@gmail.com",
                email = "carlinhosmiau@gmail.com",
                ra = "23024211",
                role = ROLE.DEV,
                stack = STACK.BACKEND,
                year = 3,
                cellphone = "11998472663",
                course = COURSE.ECM,
                hired_date = 1640192165000,
                active = ACTIVE.ON_HOLD,
                deactivated_date = None,
                user_id = "3b07232f-4f65-42c6-b005-242550b8b8dc",
                photo=None
            )
        ]

   

    def create_member(self, member: Member) -> Member:
        self.members.append(member)
        return member


    def delete_member(self, user_id: str) -> Optional[Member]:
        for i in range(len(self.members)):
            if self.members[i].user_id == user_id:
                return self.members.pop(i)
        return None

    def get_member(self, user_id: str) -> Optional[Member]:
        for member in self.members:
            if member.user_id == user_id:
                return member
        return None
    
    
    def update_member(self, user_id: str, hired_date: int, email:str, new_name: Optional[str] = None, new_email_dev: Optional[str] = None, new_role: Optional[ROLE] = None, new_stack: Optional[STACK] = None, new_year: Optional[int] = None, new_cellphone: Optional[str] = None, new_course: Optional[COURSE] = None, new_active: Optional[ACTIVE] = None) -> Member:
       
        for member in self.members:
            if member.user_id == user_id:
                if new_name is not None:
                    member.name = new_name
                if new_email_dev is not None:
                    member.email_dev = new_email_dev
                if new_role is not None:
                    member.role = new_role
                if new_stack is not None:
                    member.stack = new_stack
                if new_year is not None:
                    member.year = new_year
                if new_cellphone is not None:
                    member.cellphone = new_cellphone
                if new_course is not None:
                    member.course = new_course
                if new_active is not None:
                    member.active = new_active
                    if new_active == ACTIVE.DISCONNECTED:
                        member.deactivated_date = int(datetime.datetime.now().timestamp() * 1000) 
                if member.hired_date is not None:
                    member.hired_date = hired_date
                if member.email is not None:
                    member.email = email
                
                return member
            
        return None
    
 

    def get_all_members(self) -> List[Member]:
        active_members = []
        for member in self.members:
            active_members.append(member)
        return active_members

 
    def batch_get_member(self, user_ids: List[str]) -> List[Member]:
        members = []
        for member in self.members:
            if member.user_id in user_ids:
                members.append(member)
        return members