from src.modules.get_all_actions_by_ra.app.get_all_actions_by_ra_viewmodel import GetAllActionsByRaViewmodel
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from src.modules.get_all_actions_by_ra.app.get_all_actions_by_ra_usecase import GetAllActionsByRaUsecase

class Test_GetAllActionsByRaViewmodel:
    def test_get_all_actions_by_ra_viewmodel(self):
        repo = ActionRepositoryMock()
        usecase = GetAllActionsByRaUsecase(repo)
        actions = usecase(ra='21017310')
        viewmodel = GetAllActionsByRaViewmodel(actions)
        expected = {
   "actions":[
      { 
         "owner_ra":"21017310",
         "date":"2021-10-18T00:00:00",
         "action_id":"u1e2",
         "title":"Reunião de Diretoria",
         "duration":"02:00:00",
         "project_code":"MF",
         "associated_members_ra":[
            
         ],
         "stack_tags":[
            "INTERNAL"
         ],
         "action_type_tags":[
            "MEETING"
         ]
      },
      {
         "owner_ra":"21017310",
         "date":"2021-10-18T00:00:00",
         "action_id":"dd1d",
         "title":"Code",
         "duration":"01:00:00",
         "project_code":"MF",
         "associated_members_ra":[
            
         ],
         "stack_tags":[
            
         ],
         "action_type_tags":[
            "CODE"
         ]
      },
      {
         "owner_ra":"21010757",
         "date":"2021-10-24T00:00:00",
         "action_id":"9fc2",
         "title":"Code",
         "duration":"04:30:00",
         "project_code":"PT",
         "associated_members_ra":[
            "21017310",
            "22017310"
         ],
         "stack_tags":[
            "BACKEND",
            "FRONTEND"
         ],
         "action_type_tags":[
            "CODE"
         ]
      },
      {
         "owner_ra":"21017310",
         "date":"2022-10-18T00:00:00",
         "action_id":"jf12",
         "title":"Reunião",
         "duration":"01:00:00",
         "project_code":"MF",
         "associated_members_ra":[
            
         ],
         "stack_tags":[
            "BACKEND",
            "FRONTEND"
         ],
         "action_type_tags":[
            
         ]
        }
    ],
   "message":"actions retrieved with success"
    }
        
        assert viewmodel.to_dict() == expected
        
        