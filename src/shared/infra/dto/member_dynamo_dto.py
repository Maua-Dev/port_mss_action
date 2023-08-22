from decimal import Decimal
from typing import Optional
from src.shared.domain.entities.member import Member
from src.shared.domain.enums.active_enum import ACTIVE
from src.shared.domain.enums.course_enum import COURSE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.enums.stack_enum import STACK


class MemberDynamoDTO:
    name: str
    email_dev: str
    email: str
    ra: str
    role: ROLE
    stack: STACK
    year: int
    cellphone: str
    course: COURSE
    hired_date: int
    deactivated_date: Optional[int] = None
    active: ACTIVE
    
    def __init__(self, name: str, email_dev: str, email: str, ra: str, role: ROLE, stack: STACK, year: int, cellphone: str, course: COURSE, hired_date: int, active: ACTIVE, deactivated_date: Optional[int] = None):
        self.name = name
        self.email_dev = email_dev
        self.email = email
        self.ra = ra
        self.role = role
        self.stack = stack
        self.year = year
        self.cellphone = cellphone
        self.course = course
        self.hired_date = hired_date
        self.deactivated_date = deactivated_date
        self.active = active
        
    @staticmethod
    def from_entity(member: Member) -> "MemberDynamoDTO":
        return MemberDynamoDTO(
            name=member.name,
            email_dev=member.email_dev,
            email=member.email,
            ra=member.ra,
            role=member.role,
            stack=member.stack,
            year=member.year,
            cellphone=member.cellphone,
            course=member.course,
            hired_date=member.hired_date,
            deactivated_date=member.deactivated_date,
            active=member.active
        )
        
    def to_dynamo(self) -> dict:
        data =  {
            "entity": "member",
            "name": self.name,
            "email_dev": self.email_dev,
            "email": self.email,
            "ra": self.ra,
            "role": self.role.value,
            "stack": self.stack.value,
            "year": Decimal(self.year),
            "cellphone": self.cellphone,
            "course": self.course.value,
            "hired_date": Decimal(self.hired_date),
            "deactivated_date": Decimal(self.deactivated_date) if self.deactivated_date else None,
            "active": self.active.value
        }
        
        data_without_none_values = {k: v for k, v in data.items() if v is not None}
        return data_without_none_values
        
    @staticmethod
    def from_dynamo(member_data: dict) -> "MemberDynamoDTO":
        return MemberDynamoDTO(
            name=member_data["name"],
            email_dev=member_data["email_dev"],
            email=member_data["email"],
            ra=member_data["ra"],
            role=ROLE(member_data["role"]),
            stack=STACK(member_data["stack"]),
            year=int(member_data["year"]),
            cellphone=member_data["cellphone"],
            course=COURSE(member_data["course"]),
            hired_date=int(member_data["hired_date"]),
            deactivated_date=int(member_data["deactivated_date"]) if "deactivated_date" in member_data else None,
            active=ACTIVE(member_data["active"])
        )
    
    def to_entity(self) -> Member:   
        return Member(
            name=self.name,
            email_dev=self.email_dev,
            email=self.email,
            ra=self.ra,
            role=self.role,
            stack=self.stack,
            year=self.year,
            cellphone=self.cellphone,
            course=self.course,
            hired_date=self.hired_date,
            deactivated_date=self.deactivated_date,
            active=self.active
        )
        
    def __repr__(self): 
        return f"MemberDynamoDTO(name={self.name}, email_dev={self.email_dev}, email={self.email}, ra={self.ra}, role={self.role}, stack={self.stack}, year={self.year}, cellphone={self.cellphone}, course={self.course}, hired_date={self.hired_date}, deactivated_date={self.deactivated_date}, active={self.active})"
    
    def __eq__(self, other):
        if not isinstance(other, MemberDynamoDTO):
            return False
        return self.name == other.name and self.email_dev == other.email_dev and self.email == other.email and self.ra == other.ra and self.role == other.role and self.stack == other.stack and self.year == other.year and self.cellphone == other.cellphone and self.course == other.course and self.hired_date == other.hired_date and self.deactivated_date == other.deactivated_date and self.active == other.active