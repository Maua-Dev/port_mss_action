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
        member = repo.get_member(ra="1234")
        assert member is None
        
    def test_get_member(self):
        repo = MemberRepositoryMock()
        member = repo.get_member(ra='21017310')
        assert type(member) == Member
        assert member == repo.members[0]

    def test_batch_get_member(self):
        repo = MemberRepositoryMock()
        members = repo.batch_get_member(ras=[repo.members[0].ra, repo.members[1].ra])
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
            active=ACTIVE.ACTIVE
        )
        repo.create_member(member)
        assert member in repo.members
        
        

        
    