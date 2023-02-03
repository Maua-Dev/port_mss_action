from src.shared.domain.entities.action import Action
from src.shared.domain.entities.associated_action import AssociatedAction
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
            repo.associatedActions[0], repo.associatedActions[3], repo.associatedActions[7], repo.associatedActions[9]
        ]
        expected.sort(key=lambda associated_action: associated_action.action.start_time)
        
        assert len(actions) == len(expected)
        assert actions == expected
        assert all([type(action) == AssociatedAction for action in actions])
        assert all([action.member_ra == repo.members[0].ra for action in actions])
    
    def test_get_all_actions_by_ra_member_without_actions(self):
        repo = ActionRepositoryMock()
        member = repo.get_member(ra=repo.members[6].ra)
        actions = repo.get_all_actions_by_ra(ra=member.ra)
        
        assert actions == []
        assert len(actions) == 0
        
    def test_create_member(self):
        repo = ActionRepositoryMock()
        member = Member(name="Teste", email="teste.devmaua@gmail.com", ra="12345678", role=ROLE.DEV, stack=STACK.BACKEND, year=2, cellphone="11912345678", course=COURSE.CIC, hired_date=1634526000000, active=ACTIVE.ACTIVE)
        len_before = len(repo.members)
        
        new_member = repo.create_member(member=member)
        
        assert len(repo.members) == len_before + 1
        assert new_member == member
        
    def test_create_action(self):
        repo = ActionRepositoryMock()
        action = Action(owner_ra='17033730', start_time=1634526000000, action_id='82fc', associated_members_ra=['12345678'], title='Teste', end_time=1634536800000, project_code='MF', stack_tags=[STACK.BACKEND], action_type_tags=[ACTION_TYPE.CODE])
        len_before = len(repo.actions)
        
        new_action = repo.create_action(action=action)
        assert len(repo.actions) == len_before + 1
        assert new_action == action

    def test_get_action(self):
        repo = ActionRepositoryMock()
        action = repo.get_action(action_id=repo.actions[0].action_id)

        assert type(action) == Action
        assert action == repo.actions[0]
        
    def test_get_action_not_found(self):
        repo = ActionRepositoryMock()
        action = repo.get_action(action_id="1234")

        assert action is None
        
    def test_create_associated_action(self):
        repo = ActionRepositoryMock()
        action = Action(owner_ra='17033730', start_time=1634526000000, action_id='82fc', associated_members_ra=['12345678'], title='Teste', end_time=1634536800000, project_code='MF', stack_tags=[STACK.BACKEND], action_type_tags=[ACTION_TYPE.CODE])
        associatedAction = AssociatedAction(member_ra='12345678', action=action)
        len_before = len(repo.associatedActions)
        
        new_associated_action = repo.create_associated_action(associatedAction=associatedAction)
        assert len(repo.associatedActions) == len_before + 1
        assert new_associated_action == associatedAction

    def test_create_action_with_associated_members(self):
        repo = ActionRepositoryMock()
        action = Action(owner_ra='17033730', start_time=1634526000000, action_id='82fc', associated_members_ra=['12345678', '98765432'], title='Teste', end_time=1634536800000, project_code='MF', stack_tags=[STACK.BACKEND], action_type_tags=[ACTION_TYPE.CODE])
        len_actions_before = len(repo.actions)
        len_associatedActions_before = len(repo.associatedActions)
        new_action = repo.create_action(action=action)
        assert len(repo.actions) == len_actions_before + 1
        assert len(repo.associatedActions) == len_associatedActions_before + 3
        
    def test_get_members(self):
        repo = ActionRepositoryMock()
        ras = [repo.members[0].ra, repo.members[1].ra]
        members = repo.get_members(ras=ras)
        assert len(members) == len(ras)
        assert all([type(member) == Member for member in members])
        assert members == [repo.members[0], repo.members[1]]
        