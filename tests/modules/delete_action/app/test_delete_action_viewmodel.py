from src.modules.delete_action.app.delete_action_viewmodel import DeleteActionViewModel
from src.shared.domain.entities.action import Action
from src.shared.domain.enums.stack_enum import STACK
from src.shared.domain.enums.action_type_enum import ACTION_TYPE

class Test_DeleteActionViewModel:
    def test_delete_action_viewmodel(self):
        action = Action(
            user_id='93bc6ada-c0d1-7054-66ab-e17414c48ae3',
            start_date=1641896000000,
            stack_tags=[STACK.BACKEND],
            end_date=1679686000000,
            duration=37790000000,
            action_id='93bc6ada-c0d1-7054-66ab-e17414c48ae3',
            story_id=100,
            is_valid=True,
            title='Create a new route',
            project_code='PI',
            action_type_tag=ACTION_TYPE.CODE,
            associated_members_user_ids=['51ah5jaj-c9jm-1345-666ab-e12341c14a3'],
            description='Create a new route in the project'
        )
        viewmodel = DeleteActionViewModel(action).to_dict()
        expected = {
            'action':{
                'user_id':'93bc6ada-c0d1-7054-66ab-e17414c48ae3',
                'start_date':1641896000000,
                'end_date':1679686000000,
                'duration':37790000000,
                'action_id':'93bc6ada-c0d1-7054-66ab-e17414c48ae3',
                'is_valid':True,
                'story_id':100,
                'title':'Create a new route',
                'description':'Create a new route in the project',
                'project_code':'PI',
                'associated_members_user_ids':['51ah5jaj-c9jm-1345-666ab-e12341c14a3'],
                'stack_tags':['BACKEND'],
                'action_type_tag':'CODE'
            },
            'message':'the action was deleted for all the members in this action'
            }

        assert viewmodel == expected


    def test_delete_action_viewmodel_story_id_is_none(self):
        
        action = Action(start_date=1634526000000, duration=2*60*60*1000, action_id='a571c870-d7da-4a25-951c-2ca2d2398a14', story_id=None, associated_members_user_ids=['7465hvnb-143g-1675-86HnG-75hgnFbcg36'], title='Teste', end_date=1634536800000, project_code='MF', stack_tags=[STACK.BACKEND], action_type_tag=ACTION_TYPE.CODE, is_valid=True, user_id="9183jBnh-997H-1010-10god-914gHy46tBh")
        
        viewmodel = DeleteActionViewModel(action=action).to_dict()
        
        expected = {
            'action':{
                'start_date':1634526000000,
                'end_date':1634536800000,
                'duration':7200000,
                'action_id':'a571c870-d7da-4a25-951c-2ca2d2398a14',
                'story_id':None,
                'title':'Teste',
                'description':None,
                'project_code':'MF',
                'associated_members_user_ids':['7465hvnb-143g-1675-86HnG-75hgnFbcg36'
                ],
                'stack_tags':[
                    'BACKEND'
                ],
                'action_type_tag':'CODE',
                'is_valid':True,
                'user_id':'9183jBnh-997H-1010-10god-914gHy46tBh'
            },
            'message':'the action was deleted for all the members in this action'
            }
       
        assert viewmodel == expected