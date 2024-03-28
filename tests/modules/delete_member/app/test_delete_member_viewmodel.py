from src.modules.delete_member.app.delete_member_viewmodel import DeleteMemberViewModel
from src.shared.domain.entities.member import Member
from src.shared.domain.enums.active_enum import ACTIVE
from src.shared.domain.enums.course_enum import COURSE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.enums.stack_enum import STACK

class Test_DeleteMemberViewModel:
    def test_delete_member_viewmodel(self):
        member = Member(
            name="Gabriel Bianconi",
            email_dev="gbianconi.devmaua@gmail.com",
            email="gbianconi@gmail.com",
            ra="20008229",
            role=ROLE.DIRECTOR,
            stack=STACK.INFRA,
            year=1,
            cellphone="11991758098",
            course=COURSE.ECA,
            hired_date=1634576165000,
            active=ACTIVE.ACTIVE,
            user_id="164fg536-c0d1-7054-66ab-e17414c48ae3"
        )
        viewmodel = DeleteMemberViewModel(member).to_dict()
        expected = {
            'member': {
                'name': 'Gabriel Bianconi',
                'email_dev': 'gbianconi.devmaua@gmail.com',
                'email': 'gbianconi@gmail.com',
                'ra': '20008229',
                'role': 'DIRECTOR',
                'stack': 'INFRA',
                'year': 1,
                'cellphone': '11991758098',
                'course': 'ECA',
                'hired_date': 1634576165000,
                'deactivated_date': None,
                'active': 'ACTIVE',
                'user_id': "164fg536-c0d1-7054-66ab-e17414c48ae3"
            },
            'message': 'the member was deleted'
        }
        assert viewmodel == expected
        
    def test_delete_member_viewmodel_with_deactivated_date(self):
        member = Member(
            name="Gabriel Bianconi",
            email_dev="gbianconi.devmaua@gmail.com",
            email="gbianconi@gmail.com",
            ra="20008229",
            role=ROLE.DIRECTOR,
            stack=STACK.INFRA,
            year=1,
            cellphone="11991758098",
            course=COURSE.ECA,
            hired_date=1634576165000,
            deactivated_date=1634576165600,
            active=ACTIVE.DISCONNECTED,
            user_id="164fg536-c0d1-7054-66ab-e17414c48ae3"
        )
        viewmodel = DeleteMemberViewModel(member).to_dict()
        expected = {
            'member': {
                'name': 'Gabriel Bianconi',
                'email_dev': 'gbianconi.devmaua@gmail.com',
                'email': 'gbianconi@gmail.com',
                'ra': '20008229',
                'role': 'DIRECTOR',
                'stack': 'INFRA',
                'year': 1,
                'cellphone': '11991758098',
                'course': 'ECA',
                'hired_date': 1634576165000,
                'deactivated_date': 1634576165600,
                'active': 'DISCONNECTED',
                'user_id': "164fg536-c0d1-7054-66ab-e17414c48ae3"
            },
            'message': 'the member was deleted'
        }
        assert viewmodel == expected
            
