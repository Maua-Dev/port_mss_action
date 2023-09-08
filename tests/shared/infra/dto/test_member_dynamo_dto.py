from src.shared.domain.entities.member import Member
from src.shared.domain.enums.active_enum import ACTIVE
from src.shared.domain.enums.course_enum import COURSE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.enums.stack_enum import STACK
from src.shared.infra.dto.member_dynamo_dto import MemberDynamoDTO


class Test_MemberDynamoDTO:

    def test_member_dynamo_dto_from_entity(self):
        member = Member(
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

        member_dto = MemberDynamoDTO.from_entity(member)
        assert member_dto == MemberDynamoDTO(name="Henrique Gustavo de Souza", email_dev="hsouza.devmaua@gmail.com", email="hsouza@gmail.com", ra="23017310",
                                             role=ROLE.DEV, stack=STACK.UX_UI, year=1, cellphone="11991123498", course=COURSE.ECM, hired_date=1672592165000, active=ACTIVE.ACTIVE)

    def test_member_dynamo_dto_to_dynamo(self):
        member_dto = MemberDynamoDTO(name="Henrique Gustavo de Souza", email_dev="hsouza.devmaua@gmail.com", email="hsouza@gmail.com", ra="23017310",
                                     role=ROLE.DEV, stack=STACK.UX_UI, year=1, cellphone="11991123498", course=COURSE.ECM, hired_date=1672592165000, active=ACTIVE.ACTIVE)

        member_dynamo = member_dto.to_dynamo()

        assert member_dynamo == {"entity": "member", "name": "Henrique Gustavo de Souza", "email_dev": "hsouza.devmaua@gmail.com", "email": "hsouza@gmail.com",
                                 "ra": "23017310", "role": "DEV", "stack": "UX_UI", "year": 1, "cellphone": "11991123498", "course": "ECM", "hired_date": 1672592165000, "active": "ACTIVE"}
    
    def test_member_dynamo_dto_from_dynamo(self):
        member_dynamo = {"entity": "member", "name": "Henrique Gustavo de Souza", "email_dev": "hsouza.devmaua@gmail.com", "email": "hsouza@gmail.com",
                                 "ra": "23017310", "role": "DEV", "stack": "UX_UI", "year": 1, "cellphone": "11991123498", "course": "ECM", "hired_date": 1672592165000, "active": "ACTIVE"}
        
        member_dto = MemberDynamoDTO.from_dynamo(member_dynamo)
        
        assert member_dto == MemberDynamoDTO(name="Henrique Gustavo de Souza", email_dev="hsouza.devmaua@gmail.com", email="hsouza@gmail.com", ra="23017310",
                                             role=ROLE.DEV, stack=STACK.UX_UI, year=1, cellphone="11991123498", course=COURSE.ECM, hired_date=1672592165000, active=ACTIVE.ACTIVE)
        
    def test_member_dynamo_dto_to_entity(self):
        member_dto =  MemberDynamoDTO(name="Henrique Gustavo de Souza", email_dev="hsouza.devmaua@gmail.com", email="hsouza@gmail.com", ra="23017310",
                                             role=ROLE.DEV, stack=STACK.UX_UI, year=1, cellphone="11991123498", course=COURSE.ECM, hired_date=1672592165000, active=ACTIVE.ACTIVE)
        
        member = member_dto.to_entity()
        
        assert member == Member(
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
        
    def test_member_dynamo_dto_from_entity_to_dynamo(self):
        member = Member(
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
        
        member_dynamo = MemberDynamoDTO.from_entity(member).to_dynamo()
        
        assert member_dynamo == {"entity": "member", "name": "Henrique Gustavo de Souza", "email_dev": "hsouza.devmaua@gmail.com", "email": "hsouza@gmail.com",
                                 "ra": "23017310", "role": "DEV", "stack": "UX_UI", "year": 1, "cellphone": "11991123498", "course": "ECM", "hired_date": 1672592165000, "active": "ACTIVE"}
        
    def test_member_dynamo_dto_from_dynamo_to_entity(self):       
        member_dynamo = {"entity": "member", "name": "Henrique Gustavo de Souza", "email_dev": "hsouza.devmaua@gmail.com", "email": "hsouza@gmail.com",
                                 "ra": "23017310", "role": "DEV", "stack": "UX_UI", "year": 1, "cellphone": "11991123498", "course": "ECM", "hired_date": 1672592165000, "active": "ACTIVE"}
        
        member = MemberDynamoDTO.from_dynamo(member_dynamo).to_entity()
        
        assert member == Member(
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