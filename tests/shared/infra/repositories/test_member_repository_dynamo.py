import pytest
from src.shared.domain.entities.action import Action
from src.shared.domain.entities.associated_action import AssociatedAction
from src.shared.domain.entities.member import Member
from src.shared.domain.entities.project import Project
from src.shared.domain.enums.action_type_enum import ACTION_TYPE
from src.shared.domain.enums.active_enum import ACTIVE
from src.shared.domain.enums.course_enum import COURSE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.enums.stack_enum import STACK
from src.shared.infra.repositories.member_repository_dynamo import MemberRepositoryDynamo
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock


class Test_MemberRepositoryDynamo:
    @pytest.mark.skip("Can't run test in github actions")
    def test_create_member(self):
        repo = MemberRepositoryDynamo()
        member = Member(name="Joao Branco", email_dev="jbranco.devmaua@gmail.com", email="jbranco@gmail.com", ra="21010757", role=ROLE.HEAD,
                        stack=STACK.BACKEND, year=3, cellphone="11991152348", course=COURSE.ECM, hired_date=1634921765000, active=ACTIVE.ACTIVE, user_id="75648hbr-184n-1985-91han-7ghn4HgF182")
        resp = repo.create_member(member=member)

        assert resp == member

    @pytest.mark.skip("Can't run test in github actions")
    def test_get_all_members(self):
        repo = MemberRepositoryDynamo()
        repo_mock = MemberRepositoryMock()

        members = repo_mock.members

        resp = repo.get_all_members()

        members.sort(key=lambda x: x.user_id)
        print(members)
        print(resp)

        assert resp == members

    @pytest.mark.skip("Can't run test in github actions")
    def test_get_member(self):
        repo = MemberRepositoryDynamo()
        repo_mock = MemberRepositoryMock()

        member = repo_mock.members[0]

        resp = repo.get_member(member.user_id)

        assert resp == member
    @pytest.mark.skip("Can't run test in github actions")    
    def test_delete_member(self):
        repo = MemberRepositoryMock()
        len_before = len(repo.members)
        project = repo.delete_member(user_id="9183jBnh-997H-1010-10god-914gHy46tBh")
        assert len(repo.members) == len_before - 1    
        
    @pytest.mark.skip("Can't run test in github actions")
    def test_update_member(self):
        repo = MemberRepositoryDynamo()
        resp = repo.update_member(user_id="9183jBnh-997H-1010-10god-914gHy46tBh", new_name="Gabriel Bianconi")

        assert resp.name == "Gabriel Bianconi"
        
    @pytest.mark.skip("Can't run test in github actions") 
    def test_batch_get_member(self):
        repo = MemberRepositoryDynamo()
        repo_mock = MemberRepositoryMock()

        members_user_id = [member.user_id for member in repo_mock.members]

        resp = repo.batch_get_member(members_user_id)

        expected_members = repo_mock.members
        expected_members.sort(key=lambda x: x.user_id)

        resp.sort(key=lambda x: x.user_id)

        assert resp == expected_members