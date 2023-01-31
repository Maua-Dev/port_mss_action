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
            repo.actions[0], repo.actions[1], repo.actions[4], repo.actions[6]
        ]
        expected.sort(key=lambda action: action.date)
        
        assert len(actions) == len(expected)
        assert actions == expected
        assert all([type(action) == Action for action in actions])
    
    def test_get_all_actions_by_ra_member_without_actions(self):
        repo = ActionRepositoryMock()
        member = repo.get_member(ra=repo.members[6].ra)
        actions = repo.get_all_actions_by_ra(ra=member.ra)
        
        assert actions == []
        assert len(actions) == 0
        
    def test_create_member(self):
        repo = ActionRepositoryMock()
        member = Member(name="Teste", email="teste.devmaua@gmail.com", ra="12345678", role=ROLE.DEV, stack=STACK.BACKEND, year=2, cellphone="11912345678", course=COURSE.CIC, hired_date=1634526000, active=ACTIVE.ACTIVE)
        len_before = len(repo.members)
        
        new_member = repo.create_member(member=member)
        
        assert len(repo.members) == len_before + 1
        assert new_member == member