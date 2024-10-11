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
    def test_get_all_members(self):
        repo = MemberRepositoryDynamo()
        repo_mock = MemberRepositoryMock()

        members = repo_mock.members

        resp = repo.get_all_members()

        members.sort(key=lambda x: x.user_id)
        
        assert resp == members
        
    @pytest.mark.skip("Can't run test in github actions")
    def test_create_member(self):
        repo = MemberRepositoryDynamo()
        member = Member(name="Gabriel Bianconi", email_dev="gbianconi.devmaua@gmail.com", email="gabrielbianconiconi@gmail.com", ra="20008228", role=ROLE.DEV,
                        stack=STACK.BACKEND, year=3, cellphone="11998472553", course=COURSE.ECM, hired_date=1634921765000, active=ACTIVE.ACTIVE, user_id="15648hbr-154n-1983-91hab-7ghn4HgF182")
        resp = repo.create_member(member=member)

        assert resp == member

    @pytest.mark.skip("Can't run test in github actions")
    def test_get_member(self):
        repo = MemberRepositoryDynamo()
        repo_mock = MemberRepositoryMock()

        member = repo_mock.members[1]

        resp = repo.get_member(member.user_id)

        assert resp == member
    @pytest.mark.skip("Can't run test in github actions")    
    def test_delete_member(self):
        repo_mock = MemberRepositoryMock()
        repo = MemberRepositoryDynamo()
        
        member = repo_mock.members[0]
        deleted_member = repo.delete_member(member.user_id)
        
        assert deleted_member == member    
        
    @pytest.mark.skip("Can't run test in github actions")
    def test_update_member(self):
        repo = MemberRepositoryDynamo()
        resp = repo.update_member(user_id="75648hbr-184n-1985-91han-7ghn4HgF182",new_active=ACTIVE.DISCONNECTED,new_deactivated_date=100000000000009,new_name="test234")
        assert resp.deactivated_date == 100000000000009
        assert resp.active == ACTIVE.DISCONNECTED
        assert resp.name == "test234"   
      

    @pytest.mark.skip("Can't run test in github actions") 
    def test_batch_get_member(self):
        repo = MemberRepositoryDynamo()
        repo_mock = MemberRepositoryMock()

        members_user_id = ["51ah5jaj-c9jm-1345-666ab-e12341c14a3", "76h35dg4-h76v-1875-987hn-h67gfv45Gt4"]

        resp = repo.batch_get_member(members_user_id)
        expected_members = [repo_mock.members[1], repo_mock.members[2]]
        expected_members.sort(key=lambda x: x.user_id)

        resp.sort(key=lambda x: x.user_id)

        assert resp == expected_members
        
    @pytest.mark.skip("Can't test ses in Github")
    def test_send_active_member_email(self):

        repo_activity_dynamo = MemberRepositoryDynamo()
        user = Member(
                name="Lucas Crapino",
                email_dev="lcrapino.devmaua@gmail.com",
                email="lucascrapino@gmail.com",
                ra="22006672",
                role=ROLE.DEV,
                stack=STACK.UX_UI,
                year=1,
                cellphone="11991123498",
                course=COURSE.ECM,
                hired_date=1672592165000,
                active=ACTIVE.ACTIVE,
                deactivated_date=None,
                user_id="9183jBnh-997H-1010-10god-914gHy46tBh"
            )

        send_email = repo_activity_dynamo.send_active_member_email(user)

        assert send_email
        
    @pytest.mark.skip("Can't test dynamo in Github")
    def test_request_upload_member_photo(self):
        repo_dynamo = MemberRepositoryDynamo()
        presigned_post = repo_dynamo.request_upload_member_photo(user_id="51ah5jaj-c9jm-1345-666ab-e12341c14a3")

        assert type(presigned_post) == dict
        assert presigned_post["metadata"]["user_id"] == "51ah5jaj-c9jm-1345-666ab-e12341c14a3"
        assert presigned_post["metadata"]["time_created"].isdecimal()
        assert type(presigned_post["url"]) == str
