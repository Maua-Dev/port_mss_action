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
            active=ACTIVE.ACTIVE ,
            user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
            deactivated_date=None)
        
     
        viewmodel = CreateMemberViewmodel(member=member).to_dict()
        expected = {
                    'member':{
            'name' : 'Vitor Guirão MPNTM',
            'email_dev' : "vsoller.devmaua@gmail.com",
            'email' : "vsoller@airubio.com",
            'ra' : "21017310",
            'role' : ROLE.DIRECTOR.value,
            'stack' : STACK.INFRA.value,
            'year' : 1,
            'cellphone' : "11991758098",
            'course' : COURSE.ECA.value,
            'hired_date' : 1614567601000,
            'active' : ACTIVE.ACTIVE.value,
            'user_id' : "93bc6ada-c0d1-7054-66ab-e17414c48ae3",
            'deactivated_date' : None
                    },
                    'message':'the member was created'
        }
       
        assert viewmodel == expected

   