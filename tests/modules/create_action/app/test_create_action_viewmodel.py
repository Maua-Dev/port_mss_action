from src.modules.create_action.app.create_action_usecase import CreateActionUsecase
from src.modules.create_action.app.create_action_viewmodel import CreateActionViewmodel
from src.shared.domain.entities.action import Action
from src.shared.domain.enums.action_type_enum import ACTION_TYPE
from src.shared.domain.enums.stack_enum import STACK
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock


class Test_CreateActionViewmodel:
    def test_create_action_viewmodel(self):
        repo = ActionRepositoryMock()
        usecase = CreateActionUsecase(repo=repo)
        
        action = Action(owner_ra='17033730', start_date=1634526000000, duration=2*60*60*1000, action_id='82fc', story_id=100, associated_members_ra=['19017310'], title='Teste', end_date=1634536800000, project_code='MF', stack_tags=[STACK.BACKEND], action_type_tag=ACTION_TYPE.CODE)
        
        viewmodel = CreateActionViewmodel(action=usecase(action=action)).to_dict()
        
        expected = {
            'action':{
                'owner_ra':'17033730',
                'start_date':1634526000000,
                'end_date':1634536800000,
                'duration':7200000,
                'action_id':'82fc',
                'story_id': 100,
                'title':'Teste',
                'description':"Apenas um teste",
                'project_code':'MF',
                'associated_members_ra':['19017310'],
                'stack_tags':['BACKEND'],
                'action_type_tag':'CODE'
            },
            'message':'the action was created'
            }
       
        assert viewmodel == expected

    def test_create_action_viewmodel_story_id_is_none(self):
        repo = ActionRepositoryMock()
        usecase = CreateActionUsecase(repo=repo)
        
        action = Action(owner_ra='17033730', start_date=1634526000000, duration=2*60*60*1000, action_id='82fc', story_id=None, associated_members_ra=['19017310'], title='Teste', end_date=1634536800000, project_code='MF', stack_tags=[STACK.BACKEND], action_type_tag=ACTION_TYPE.CODE)
        
        viewmodel = CreateActionViewmodel(action=usecase(action=action)).to_dict()
        
        expected = {
            'action':{
                'owner_ra':'17033730',
                'start_date':1634526000000,
                'end_date':1634536800000,
                'duration':7200000,
                'action_id':'82fc',
                'story_id': None,
                'title':'Teste',
                'project_code':'MF',
                'associated_members_ra':['19017310'],
                'stack_tags':['BACKEND'],
                'action_type_tag':'CODE'
            },
            'message':'the action was created'
            }
       
        assert viewmodel == expected

    def test_create_action_viewmodel_associated_members_is_none(self):
        repo = ActionRepositoryMock()
        usecase = CreateActionUsecase(repo=repo)
        
        action = Action(owner_ra='17033730', start_date=1634526000000, duration=2*60*60*1000, action_id='82fc', story_id=100, associated_members_ra=None, title='Teste', end_date=1634536800000, project_code='MF', stack_tags=[STACK.BACKEND], action_type_tag=ACTION_TYPE.CODE)
        
        viewmodel = CreateActionViewmodel(action=usecase(action=action)).to_dict()
        
        expected = {
            'action':{
                'owner_ra':'17033730',
                'start_date':1634526000000,
                'end_date':1634536800000,
                'duration':7200000,
                'action_id':'82fc',
                'story_id': 100,
                'title':'Teste',
                'description':None,
                'project_code':'MF',
                'associated_members_ra':[],
                'stack_tags':['BACKEND'],
                'action_type_tag':'CODE'
            },
            'message':'the action was created'
            }
       
        assert viewmodel == expected