from src.modules.create_action.app.create_action_viewmodel import CreateActionViewmodel
from src.modules.create_member.app.create_member_viewmodel import CreateMemberViewmodel
from src.shared.domain.entities.action import Action
from src.shared.domain.entities.member import Member
import cgi
from src.shared.domain.enums.action_type_enum import ACTION_TYPE
from src.shared.domain.enums.active_enum import ACTIVE
from src.shared.domain.enums.course_enum import COURSE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.enums.stack_enum import STACK
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock


class Test_CreateMemberViewmodel:
    def test_create_member_viewmodel(self):
        repo = MemberRepositoryMock()
        member = Member( name="Vitor Guirão MPNTM",
            email_dev="vsoller.devmaua@gmail.com",
            email="vsoller@airubio.com",
            ra="21017310",
            role=ROLE.DIRECTOR,
            stack=STACK.INFRA,
            year=1,
            cellphone="11991758098",
            course=COURSE.ECA,
            hired_date=1614567601000,
             active=ACTIVE.ACTIVE  ,
                  deactivated_date=None)
        
        # action = Action(owner_ra='17033730', start_date=1634526000000, duration=2*60*60*1000, action_id='a571c870-d7da-4a25-951c-2ca2d2398a14', story_id=100, associated_members_ra=['19017310'], title='Teste', end_date=1634536800000, project_code='MF', stack_tags=[STACK.BACKEND], action_type_tag=ACTION_TYPE.CODE)
        
        # viewmodel = CreateActionViewmodel(action=action).to_dict()
        viewmodel = CreateMemberViewmodel(member=member).to_dict()
        expected = {
                    'member':{
            'name' : 'Vitor Guirão MPNTM',
            'email_dev' : "vsoller.devmaua@gmail.com",
            'email' : "vsoller@airubio.com",
            'ra' : "21017310",
            'role' : ROLE.DIRECTOR,
            'stack' : STACK.INFRA,
            'year' : 1,
            'cellphone' : "11991758098",
            'course' : COURSE.ECA,
            'hired_date' : 1614567601000,
            'active' : ACTIVE.ACTIVE,
            'deactivated_date' : None
                    },
                    'message':'the member was created'
        }
       
        assert viewmodel == expected

   