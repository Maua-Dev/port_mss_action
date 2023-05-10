from src.modules.get_all_actions_by_ra.app.get_all_actions_by_ra_viewmodel import GetAllActionsByRaViewmodel
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from src.modules.get_all_actions_by_ra.app.get_all_actions_by_ra_usecase import GetAllActionsByRaUsecase

class Test_GetAllActionsByRaViewmodel:
    def test_get_all_actions_by_ra_viewmodel(self):
        repo = ActionRepositoryMock()
        usecase = GetAllActionsByRaUsecase(repo)
        ra = '21017310'
        associated_actions = usecase(ra=ra)
        viewmodel = GetAllActionsByRaViewmodel(associated_actions=associated_actions, ra=ra)
        expected = {
            'actions':[
               {
                  'start_date':1634526000000,
                  'end_date':1634533200000,
                  'duration':7200000,
                  'action_id':'u1e2',
                  'title':'Reunião de Diretoria',
                  'project_code':'MF',
                  'stack_tags':['INTERNAL'],
                  'action_type_tags':['MEETING'],
                  'is_owner':True
               },
               {
                  'start_date':1634526000000,
                  'end_date':1634529600000,
                  'duration':3600000,
                  'action_id':'dd1d',
                  'title':'Code',
                  'project_code':'MF',
                  'stack_tags':[],
                  'action_type_tags':['CODE'],
                  'is_owner':True
               },
               {
                  'start_date':1635044400000,
                  'end_date':1635060600000,
                  'duration':16200000,
                  'action_id':'9fc2',
                  'title':'Code',
                  'project_code':'PT',
                  'stack_tags':['BACKEND', 'FRONTEND'],
                  'action_type_tags':['CODE'],
                  'is_owner':False
               },
               {
                  'start_date':1666062000000,
                  'end_date':1666065600000,
                  'duration':3600000,
                  'action_id':'jf12',
                  'title':'Reunião',
                  'project_code':'MF',
                  'stack_tags':['BACKEND', 'FRONTEND'],
                  'action_type_tags':[],
                  'is_owner':True
               }
            ],
            'ra':'21017310',
            'message':'the actions were retrieved'
         }
        
        assert viewmodel.to_dict() == expected   