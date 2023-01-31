import datetime
from src.shared.domain.entities.action import Action
from src.shared.domain.entities.member import Member
from src.shared.domain.enums.action_type_enum import ACTION_TYPE
from src.shared.domain.enums.active_enum import ACTIVE
from src.shared.domain.enums.course_enum import COURSE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.enums.stack_enum import STACK
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock


class Test_ActionRepositoryMock:
    def test_get_member(self):
        repo = ActionRepositoryMock()
        member = repo.get_member(ra=repo.members[1].ra)
        
        assert type(member) == Member
        assert member == repo.members[1]
        
    def test_get_member_not_found(self):
        repo = ActionRepositoryMock()
        member = repo.get_member(ra="21010101")
        
        assert member is None
    
    def test_get_all_actions_by_ra(self):
        repo = ActionRepositoryMock()
        member = repo.get_member(ra=repo.members[0].ra)
        actions = repo.get_all_actions_by_ra(ra=member.ra)
        expected = [
            Action(
                owner_ra="21017310",
                date=datetime.datetime(2021, 10, 18),
                action_id="u1e2",
                associated_members_ra=None,
                title="Reunião de Diretoria",
                duration=datetime.time(2, 0, 0),
                project_code="MF",
                stack_tags=[STACK.INTERNAL],
                action_type_tags=[ACTION_TYPE.MEETING]
            ),
            Action(
                owner_ra="21017310",
                date=datetime.datetime(2021, 10, 18),
                action_id="dd1d",
                associated_members_ra=None,
                title="Code",
                duration=datetime.time(1, 0, 0),
                project_code="MF",
                stack_tags=None,
                action_type_tags=[ACTION_TYPE.CODE]
            ),
            Action(
                owner_ra="21010757",
                date=datetime.datetime(2021, 10, 24),
                action_id="9fc2",
                associated_members_ra=["21017310", "22017310"],
                title="Code",
                duration=datetime.time(4, 30, 0),
                project_code="PT",
                stack_tags=[STACK.BACKEND, STACK.FRONTEND],
                action_type_tags=[ACTION_TYPE.CODE]
            ),
            Action(
                owner_ra="21017310",
                date=datetime.datetime(2022, 10, 18),
                action_id="jf12",
                associated_members_ra=None,
                title="Reunião",
                duration=datetime.time(1, 0, 0),
                project_code="MF",
                stack_tags=[STACK.BACKEND, STACK.FRONTEND],
                action_type_tags=None
            )
        ]
        
        assert actions == expected
        assert len(actions) == len(expected)
        assert all([type(action) == Action for action in actions])
    
    def test_get_all_actions_by_ra_member_without_actions(self):
        repo = ActionRepositoryMock()
        member = repo.get_member(ra=repo.members[6].ra)
        actions = repo.get_all_actions_by_ra(ra=member.ra)
        
        assert actions == []
        assert len(actions) == 0
        
    def test_create_member(self):
        repo = ActionRepositoryMock()
        member = Member(name="Teste", email="teste.devmaua@gmail.com", ra="12345678", role=ROLE.DEV, stack=STACK.BACKEND, year=2, cellphone="11912345678", course=COURSE.CIC, hired_date=datetime.datetime(2021, 10, 18), active=ACTIVE.ACTIVE)
        len_before = len(repo.members)
        
        new_member = repo.create_member(member=member)
        
        assert len(repo.members) == len_before + 1
        assert new_member == member