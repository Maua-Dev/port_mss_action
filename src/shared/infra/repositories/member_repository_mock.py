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


class MemberRepositoryMock(IActionRepository):
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

   

    def create_member(self, member: Member) -> Member:
        self.members.append(member)
        return member


    def delete_member(self, ra: str) -> Optional[Member]:
        for i in range(len(self.members)):
            if self.members[i].ra == ra:
                return self.members.pop(i)
        return None

    def get_member(self, ra: str) -> Member:
        for member in self.members:
            if member.ra == ra:
                return member
        return None
    
    
    def update_member(self, ra: str, new_name: Optional[str] = None, new_email_dev: Optional[str] = None, new_email: Optional[str] = None, new_role: Optional[ROLE] = None, new_stack: Optional[STACK] = None, new_year: Optional[int] = None, new_cellphone: Optional[str] = None, new_course: Optional[COURSE] = None, new_hired_date: Optional[int] = None, new_deactivated_date: Optional[int] = None, new_active: Optional[ACTIVE] = None) -> Member:
        for member in self.members:
            if member.ra == ra:
                if new_name is not None:
                    member.name = new_name
                if new_email_dev is not None:
                    member.email_dev = new_email_dev
                if new_email is not None:
                    member.email = new_email
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
                if new_hired_date is not None:
                    member.hired_date = new_hired_date 
                if new_active is not None:
                    member.active = new_active
                if new_deactivated_date is not None:
                    member.deactivated_date = new_deactivated_date                    
                return member
            
        return None
    
 

    def get_all_members(self) -> List[Member]:
        return self.members

 
    def batch_get_member(self, ras: List[str]) -> List[Member]:
        members = []
        for member in self.members:
            if member.ra in ras:
                members.append(member)
        return members