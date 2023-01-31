from src.modules.create_member.app.create_member_usecase import CreateMemberUsecase
from src.modules.create_member.app.create_member_viewmodel import CreateMemberViewmodel
from src.shared.domain.entities.member import Member
from src.shared.domain.entities.project import Project
from src.shared.domain.enums.active_enum import ACTIVE
from src.shared.domain.enums.course_enum import COURSE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.enums.stack_enum import STACK
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock


class Test_CreateMemberViewmodel:
    def test_create_member_viewmodel(self):
        repo = ActionRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        
        member = Member(name="Teste", email="teste.devmaua@gmail.com", ra="12345678", role=ROLE.DEV, stack=STACK.BACKEND, year=2, cellphone="11912345678", course=COURSE.CIC, hired_date=1634526000, active=ACTIVE.FREEZE, deactivated_date=1666062000, projects=[Project(code="MF", name="Maua Food", description="É um aplicativo #foramoleza")])
        
        memberViewModel = CreateMemberViewmodel(member=usecase(member)).to_dict()
        
        expected = {
            'member' : {
            'name':'Teste',
            'email':'teste.devmaua@gmail.com',
            'ra':'12345678',
            'role':'DEV',
            'stack':'BACKEND',
            'year':2,
            'cellphone':'11912345678',
            'course':'CIC',
            'hired_date':1634526000,
            'deactivated_date':1666062000,
            'active':'FREEZE',
            'projects':[
                {
                    'code':'MF',
                    'name':'Maua Food',
                    'description':'É um aplicativo #foramoleza'
                }
            ]},
            'message':'the member was created'
        }
        
        assert memberViewModel == expected
        
    def test_create_member_viewmodel_deactivated_date_is_none(self):
        repo = ActionRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        
        member = Member(name="Teste", email="teste.devmaua@gmail.com", ra="12345678", role=ROLE.DEV, stack=STACK.BACKEND, year=2, cellphone="11912345678", course=COURSE.CIC, hired_date=1634526000, active=ACTIVE.ACTIVE, deactivated_date=None, projects=[Project(code="MF", name="Maua Food", description="É um aplicativo #foramoleza")])
        
        memberViewModel = CreateMemberViewmodel(member=usecase(member=member)).to_dict()
        
        expected = {
            'member' : {
            'name':'Teste',
            'email':'teste.devmaua@gmail.com',
            'ra':'12345678',
            'role':'DEV',
            'stack':'BACKEND',
            'year':2,
            'cellphone':'11912345678',
            'course':'CIC',
            'hired_date':1634526000,
            'deactivated_date':None,
            'active':'ACTIVE',
            'projects':[
                {
                    'code':'MF',
                    'name':'Maua Food',
                    'description':'É um aplicativo #foramoleza'
                }
            ]},
            'message':'the member was created'
        }
        
        assert memberViewModel == expected