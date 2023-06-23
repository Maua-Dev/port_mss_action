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
    def test_create_action(self):
        repo = ActionRepositoryMock()
        action = Action(owner_ra='17033730', start_date=1634526000000, action_id='82fc', story_id=100, duration=2*60*60*1000, associated_members_ra=['12345678'], title='Teste', end_date=1634536800000, project_code='MF', stack_tags=[STACK.BACKEND], action_type_tag=ACTION_TYPE.CODE)
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
        action = Action(owner_ra='17033730', start_date=1634526000000, action_id='82fc', story_id=100, duration=2*60*60*1000, associated_members_ra=['12345678'], title='Teste', end_date=1634536800000, project_code='MF', stack_tags=[STACK.BACKEND], action_type_tag=ACTION_TYPE.CODE)
        associatedAction = AssociatedAction(member_ra='12345678', action=action)
        len_before = len(repo.associatedActions)
        
        new_associated_action = repo.create_associated_action(associatedAction=associatedAction)
        assert len(repo.associatedActions) == len_before + 1
        assert new_associated_action == associatedAction

    def test_create_action_with_associated_members(self):
        repo = ActionRepositoryMock()
        action = Action(owner_ra='17033730', start_date=1634526000000, action_id='82fc', story_id=100, duration=2*60*60*1000, associated_members_ra=['12345678', '98765432'], title='Teste', end_date=1634536800000, project_code='MF', stack_tags=[STACK.BACKEND], action_type_tag=ACTION_TYPE.CODE)
        len_actions_before = len(repo.actions)
        len_associatedActions_before = len(repo.associatedActions)
        new_action = repo.create_action(action=action)
        assert len(repo.actions) == len_actions_before + 1
        assert len(repo.associatedActions) == len_associatedActions_before + 3
        
    def test_delete_project(self):
        repo = ActionRepositoryMock()
        len_before = len(repo.projects)
        project = repo.delete_project(code='MF')
        assert len(repo.projects) == len_before - 1
        assert project.code == 'MF'