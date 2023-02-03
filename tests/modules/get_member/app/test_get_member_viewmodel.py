from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from src.modules.get_member.app.get_member_viewmodel import GetMemberViewmodel

class Test_GetMemberViewmodel:
    
    def test_get_member_viewmodel(self):
        repo = ActionRepositoryMock()
        
        member = repo.members[0]
        viewmodel = GetMemberViewmodel(member=member).to_dict()
        
        expected = {
            'member':{
                'name':'Vitor Guirão MPNTM',
                'email':'vsoller.devmaua@gmail.com',
                'ra':'21017310',
                'role':'DIRECTOR',
                'stack':'INFRA',
                'year':1,
                'cellphone':'11991758098',
                'course':'ECA',
                'hired_date':1634576165000,
                'deactivated_date':None,
                'active':'ACTIVE',
                'projects':[
                    {
                        'code':'MF',
                        'name':'Maua Food',
                        'description':'É um aplicativo #foramoleza'
                    }
                ]
            },
            'message':'the member was retrieved'
        }
        
        assert viewmodel == expected