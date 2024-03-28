from src.shared.domain.entities.action import Action
from src.shared.domain.entities.associated_action import AssociatedAction
from src.shared.domain.entities.member import Member
from src.shared.domain.entities.project import Project
from src.shared.domain.enums.action_type_enum import ACTION_TYPE
from src.shared.domain.enums.active_enum import ACTIVE
from src.shared.domain.enums.course_enum import COURSE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.enums.stack_enum import STACK
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock


class Test_MemberRepositoryMock:
          
    def test_get_member_not_found(self):
        repo = MemberRepositoryMock()
        member = repo.get_member(user_id="1234")
        assert member is None
        
    def test_get_member(self):
        repo = MemberRepositoryMock()
        member = repo.get_member(user_id='93bc6ada-c0d1-7054-66ab-e17414c48ae3')
        assert type(member) == Member
        assert member == repo.members[0]

    def test_batch_get_member(self):
        repo = MemberRepositoryMock()
        members = repo.batch_get_member(user_ids=[repo.members[0].user_id, repo.members[1].user_id])
        assert type(members) == list
        assert all([type(member) == Member for member in members])
        assert len(members) == 2
        assert members[0] == repo.members[0]
        assert members[1] == repo.members[1]
        
    def test_get_all_members(self):
        repo = MemberRepositoryMock()
        members = repo.get_all_members()
        assert type(members) == list
        assert all([type(member) == Member for member in members])
        assert len(members) == len(repo.members)
        assert members == repo.members
        
    def test_create_member(self):
        repo = MemberRepositoryMock()
        member = Member(
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
            user_id="7gh5yf5H-857H-1234-75hng-94832hvng1s"
        )
        repo.create_member(member)
        assert member in repo.members
        
        
    def test_update_member(self):
        repo = MemberRepositoryMock()
        member = repo.update_member(user_id='93bc6ada-c0d1-7054-66ab-e17414c48ae3', hired_date=1000000000000,email="test@gmail.com",new_name='Teste',new_email_dev="teste.devmaua@gmail.com",new_role=ROLE.INTERNAL,new_stack=STACK.DATA_SCIENCE,new_year=234,new_cellphone="11234567890",new_course=COURSE.ECM,new_active=ACTIVE.DISCONNECTED,new_deactivated_date=1234567890)

        assert type(member) == Member
        assert member.name == 'Teste'
        assert member.email_dev == "teste.devmaua@gmail.com"
        assert member.hired_date == 1000000000000
        assert member.email == "test@gmail.com"
        assert member.role == ROLE.INTERNAL
        assert member.stack ==   STACK.DATA_SCIENCE
        assert member.year ==  234
        assert member.cellphone == "11234567890"
        assert member.course ==   COURSE.ECM
        assert member.active ==  ACTIVE.DISCONNECTED
        assert member.deactivated_date == 1234567890                     
        
    def test_update_member_not_found(self):
        repo = MemberRepositoryMock()
        member = repo.update_member(user_id='13bc6ada-c0d1-7054-66ab-e17414c48ae3',  hired_date=1000000000000,email="test@gmail.com",new_name='Teste',new_email_dev="teste.devmaua@gmail.com",new_role=ROLE.INTERNAL,new_stack=STACK.DATA_SCIENCE)
        assert member is None    