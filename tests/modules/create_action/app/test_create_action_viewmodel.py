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
        
        action = Action(owner_ra='17033730', start_time=1634526000000, action_id='82fc', associated_members_ra=['19017310'], title='Teste', end_time=1634536800000, project_code='MF', stack_tags=[STACK.BACKEND], action_type_tags=[ACTION_TYPE.CODE])
        
        viewmodel = CreateActionViewmodel(action=usecase(action=action)).to_dict()
        
        expected = {
            'action':{
                'owner_ra':'17033730',
                'start_time':1634526000000,
                'end_time':1634536800000,
                'duration':10800000,
                'action_id':'82fc',
                'title':'Teste',
                'project_code':'MF',
                'associated_members_ra':['19017310'],
                'stack_tags':['BACKEND'],
                'action_type_tags':['CODE']
            },
            'message':'the action was created'
            }
       
        assert viewmodel == expected

    def test_create_action_viewmodel_without_tags(self):
        repo = ActionRepositoryMock()
        usecase = CreateActionUsecase(repo=repo)
        
        action = Action(owner_ra='17033730', start_time=1634526000000, action_id='82fc', associated_members_ra=None, title='Teste', end_time=1634536800000, project_code='MF', stack_tags=None, action_type_tags=None)
        
        viewmodel = CreateActionViewmodel(action=usecase(action=action)).to_dict()
        
        expected = {
            'action':{
                'owner_ra':'17033730',
                'start_time':1634526000000,
                'end_time':1634536800000,
                'duration':10800000,
                'action_id':'82fc',
                'title':'Teste',
                'project_code':'MF',
                'associated_members_ra':[],
                'stack_tags':[],
                'action_type_tags':[]
            },
            'message':'the action was created'
            }
       
        assert viewmodel == expected