from src.shared.domain.entities.action import Action
from src.shared.domain.entities.associated_action import AssociatedAction
from src.shared.domain.entities.project import Project
from src.shared.domain.enums.action_type_enum import ACTION_TYPE
from src.shared.domain.enums.stack_enum import STACK
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock


class Test_ActionRepositoryMock:
    def test_create_action(self):
        repo = ActionRepositoryMock()
        action = Action(user_id="7465hvnb-143g-1675-86HnG-75hgnFbcg36", start_date=1634526000000, is_valid=True, action_id='87d4a661-0752-4ce2-9440-05e752e636fc', story_id=100, duration=2*60*60*1000,  associated_members_user_ids=["51ah5jaj-c9jm-1345-666ab-e12341c14a3"], title='Teste', end_date=1634536800000, project_code='MF', stack_tags=[STACK.BACKEND], action_type_tag=ACTION_TYPE.CODE)
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
        action = Action(user_id="7465hvnb-143g-1675-86HnG-75hgnFbcg36", start_date=1634526000000, action_id='87d4a661-0752-4ce2-9440-05e752e636fc', is_valid=True, story_id=100, duration=2*60*60*1000, associated_members_user_ids=["93bc6ada-c0d1-7054-66ab-e17414c48ae3"], title='Teste', end_date=1634536800000, project_code='MF', stack_tags=[STACK.BACKEND], action_type_tag=ACTION_TYPE.CODE)
        associatedAction = AssociatedAction(action_id=action.action_id, start_date=action.start_date, user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3")
        len_before = len(repo.associated_actions)
        
        new_associated_action = repo.create_associated_action(associatedAction=associatedAction)
        assert len(repo.associated_actions) == len_before + 1
        assert new_associated_action == associatedAction
        
    def test_create_project(self):
        repo = ActionRepositoryMock()
        len_before = len(repo.projects)
        project = repo.create_project(project=Project(code='DM', name='DevMedias', description='Projeto que calcula a média de notas e quanto um aluno precisa tirar para passar de ano', po_user_id='93bc6ada-c0d1-7054-66ab-e17414c48ae3', scrum_user_id='7465hvnb-143g-1675-86HnG-75hgnFbcg36', start_date=1649955600000, photo='https://i.imgur.com/7QF7uCk.png', members_user_ids=['93bc6ada-c0d1-7054-66ab-e17414c48ae3', '7465hvnb-143g-1675-86HnG-75hgnFbcg36']))
        assert len(repo.projects) == len_before + 1
        assert project == repo.projects[-1]
        assert repo.projects[-1].code == 'DM'
        assert repo.projects[-1].photo == 'https://i.imgur.com/7QF7uCk.png'
        assert repo.projects[-1].members_user_ids == ['7465hvnb-143g-1675-86HnG-75hgnFbcg36','93bc6ada-c0d1-7054-66ab-e17414c48ae3']
        
    def test_delete_project(self):
        repo = ActionRepositoryMock()
        len_before = len(repo.projects)
        project = repo.delete_project(code='MF')
        assert len(repo.projects) == len_before - 1
        assert project.code == 'MF'
        
    def test_get_project(self):
        repo = ActionRepositoryMock()
        project = repo.get_project(code='MF')
        assert type(project) == Project
        assert project == repo.projects[0]
        
    def test_get_all_projects(self):
        repo = ActionRepositoryMock()
        projects = repo.get_all_projects()
        assert projects == repo.projects

    def test_update_project(self):
        repo = ActionRepositoryMock()
        project = repo.update_project(code='MF', new_name='Teste', new_description='Teste', new_po_user_id='93bc6ada-c0d1-7054-66ab-e17414c48ae3', new_scrum_user_id='7465hvnb-143g-1675-86HnG-75hgnFbcg36', new_photo='https://i.imgur.com/7QF7uCk.png', new_members_user_ids=['93bc6ada-c0d1-7054-66ab-e17414c48ae3', '7465hvnb-143g-1675-86HnG-75hgnFbcg36'])
        assert type(project) == Project
        assert project.name == 'Teste'
        assert project.description == 'Teste'
        assert project.po_user_id == '93bc6ada-c0d1-7054-66ab-e17414c48ae3'
        assert project.scrum_user_id == '7465hvnb-143g-1675-86HnG-75hgnFbcg36'
        assert project.photo == 'https://i.imgur.com/7QF7uCk.png'
        assert project.members_user_ids == ['93bc6ada-c0d1-7054-66ab-e17414c48ae3', '7465hvnb-143g-1675-86HnG-75hgnFbcg36']

    def test_update_project_not_found(self):
        repo = ActionRepositoryMock()
        project = repo.update_project(code='DM', new_name='Teste', new_description='Teste', new_po_user_id='93bc6ada-c0d1-7054-66ab-e17414c48ae3', new_scrum_user_id='7465hvnb-143g-1675-86HnG-75hgnFbcg36')
        assert project is None

    def test_get_associated_actions_by_user_id(self):
        repo = ActionRepositoryMock()
        associated_actions = repo.get_associated_actions_by_user_id(user_id='93bc6ada-c0d1-7054-66ab-e17414c48ae3', amount=20)
        assert type(associated_actions) == list
        assert all([type(associated_action) == AssociatedAction for associated_action in associated_actions])
        assert all([associated_action.user_id == '93bc6ada-c0d1-7054-66ab-e17414c48ae3' for associated_action in associated_actions])
        
    def test_get_associated_actions_by_user_id_with_start(self):
        repo = ActionRepositoryMock()
        associated_actions = repo.get_associated_actions_by_user_id(user_id='93bc6ada-c0d1-7054-66ab-e17414c48ae3', start=1658136000000, amount=20)
        assert type(associated_actions) == list
        assert all([type(associated_action) == AssociatedAction for associated_action in associated_actions])
        assert all([associated_action.user_id == '93bc6ada-c0d1-7054-66ab-e17414c48ae3' for associated_action in associated_actions])
        assert all([associated_action.start_date >= 1658136000000 for associated_action in associated_actions])
        
    def test_get_associated_actions_by_user_id_with_end(self):
        repo = ActionRepositoryMock()
        associated_actions = repo.get_associated_actions_by_user_id(user_id='93bc6ada-c0d1-7054-66ab-e17414c48ae3', end=1676476000000, amount=20)
        assert type(associated_actions) == list
        assert all([type(associated_action) == AssociatedAction for associated_action in associated_actions])
        assert all([associated_action.user_id == '93bc6ada-c0d1-7054-66ab-e17414c48ae3' for associated_action in associated_actions])
        assert all([associated_action.start_date <= 1676476000000 for associated_action in associated_actions])
        
    def test_get_associated_actions_by_user_id_exclusive_start_key(self):
        repo = ActionRepositoryMock()
        associated_actions = repo.get_associated_actions_by_user_id(user_id='93bc6ada-c0d1-7054-66ab-e17414c48ae3', exclusive_start_key={'action_id' : '87d4a661-0752-4ce2-9440-05e752e636fc', 'start_date' :1658136000000}, amount=20)
        assert type(associated_actions) == list
        assert all([type(associated_action) == AssociatedAction for associated_action in associated_actions])
        assert all([associated_action.user_id == '93bc6ada-c0d1-7054-66ab-e17414c48ae3' for associated_action in associated_actions])
        assert all([associated_action.action_id != '87d4a661-0752-4ce2-9440-05e752e636fc' for associated_action in associated_actions])
        
    def test_batch_get_action(self):
        repo = ActionRepositoryMock()
        actions = repo.batch_get_action(action_ids=[repo.actions[0].action_id, repo.actions[1].action_id])
        assert type(actions) == list
        assert all([type(action) == Action for action in actions])
        assert len(actions) == 2
        assert actions[0] == repo.actions[0]
        assert actions[1] == repo.actions[1]

    def test_batch_update_associated_action_start(self):
        repo = ActionRepositoryMock()
        action_id = repo.actions[0].action_id
        associated_actions = repo.batch_update_associated_action_start(action_id=action_id, new_start_date=1658136000000)
        assert type(associated_actions) == list
        assert all(associated_action.start_date == 1658136000000 for associated_action in repo.associated_actions if associated_action.action_id == action_id)
        
    def test_batch_update_associated_action_members(self):
        repo = ActionRepositoryMock()
        action_id = repo.actions[0].action_id
        associated_actions = repo.batch_update_associated_action_members(action_id=action_id, start_date=1658136000000, user_ids=['93bc6ada-c0d1-7054-66ab-e17414c48ae3'])
        assert type(associated_actions) == list
        assert len([associated_action for associated_action in repo.associated_actions if associated_action.action_id == action_id]) == 1
        assert all(associated_action.user_id == '93bc6ada-c0d1-7054-66ab-e17414c48ae3' for associated_action in repo.associated_actions if associated_action.action_id == action_id)
        
    def test_update_action(self):
        repo = ActionRepositoryMock()
        action = repo.update_action(action_id=repo.actions[0].action_id, new_title='Teste', new_description='Teste', new_start_date=1658136000000, new_end_date=1676476000000, new_project_code='MF', new_user_id='93bc6ada-c0d1-7054-66ab-e17414c48ae3', new_associated_members_user_ids=['76h35dg4-h76v-1875-987hn-h67gfv45Gt4'], new_is_valid=False, new_story_id=200, new_duration=2*60*60*1000, new_stack_tags=[STACK.BACKEND], new_action_type_tag=ACTION_TYPE.CODE)
        assert type(action) == Action
        assert repo.actions[0] == action

    def test_batch_delete_associated_actions_(self):
        repo = ActionRepositoryMock()
        len_before = len(repo.associated_actions)
        associated_actions = repo.batch_delete_associated_actions(action_id=repo.actions[0].action_id)
        assert type(associated_actions) == list
        assert len(associated_actions) == 7
        assert len(repo.associated_actions) == len_before - 7
        assert associated_actions[0].action_id == repo.actions[0].action_id


    def test_delete_action(self):
        repo = ActionRepositoryMock()
        action = repo.actions[0]
        len_before = len(repo.actions)
        deleted_action = repo.delete_action(action.action_id)
        assert type(deleted_action) == Action
        assert len(repo.actions) == len_before - 1
        assert deleted_action == action

    def test_get_associated_actions_by_user_id_not_found(self):
        repo = ActionRepositoryMock()
        associated_actions = repo.get_associated_actions_by_user_id(user_id='1234', amount=20)
        assert associated_actions == []

    def test_batch_get_action_not_found(self):
        repo = ActionRepositoryMock()
        actions = repo.batch_get_action(action_ids=['1234'])
        assert actions == []
    
    def test_get_all_actions_durations_by_user_id(self):
   
        repo_mock = ActionRepositoryMock()

        resp = repo_mock.get_all_actions_durations_by_user_id(1624576165000, 1690046000000)

        assert resp == {'51ah5jaj-c9jm-1345-666ab-e12341c14a3': 104090000000, 
                            '6574hgyt-785n-9134-18gn4-7gh5uvn36cG': 184430000000, 
                            '6f5g4h7J-876j-0098-123hb-hgb567fy4hb': 160010000000, 
                            '7465hvnb-143g-1675-86HnG-75hgnFbcg36': 79580000000, 
                            '75648hbr-184n-1985-91han-7ghn4HgF182': 119700000000, 
                            '76h35dg4-h76v-1875-987hn-h67gfv45Gt4': 72430000000, 
                            '7gh5yf5H-857H-1234-75hng-94832hvng1s': 107350000000, 
                            '93bc6ada-c0d1-7054-66ab-e17414c48ae3': 143960000000}
        
    def test_get_action_durations_for_user(self):
        
        repo_mock = ActionRepositoryMock()

        resp = repo_mock.get_action_durations_for_user(start_date=1624576165000, end_date=1690046000000, user_id='93bc6ada-c0d1-7054-66ab-e17414c48ae3')

        assert resp == 143960000000

    