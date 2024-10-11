from src.modules.update_member.app.update_member_usecase import UpdateMemberUsecase
from src.modules.update_member.app.update_member_viewmodel import UpdateMemberViewmodel
from src.shared.domain.enums.active_enum import ACTIVE
from src.shared.domain.enums.course_enum import COURSE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.enums.stack_enum import STACK
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock


class Test_UpdateMemberViewmodel:
    def test_update_member_viewmodel(self):
        repo = MemberRepositoryMock()
        usecase = UpdateMemberUsecase(repo)
        member = usecase(
            user_id=repo.members[0].user_id, 
            new_name='Joao Brancas',new_photo='photo')

        viewmodel = UpdateMemberViewmodel(member=member).to_dict()
        expected = {
            'member': {
                'name':"Joao Brancas",
                'email_dev':"vsoller.devmaua@gmail.com",
                'user_id': "93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                'role':ROLE.DIRECTOR.value,
                'stack':STACK.INFRA.value,
                'year':1,
                'cellphone':"11991758098",
                'course':COURSE.ECA.value,
                'hired_date':1634576165000,
                'active':ACTIVE.ACTIVE.value,
                'deactivated_date':repo.members[0].deactivated_date,
                'photo':"photo"
            },
            'message': 'the member was updated'
        }
        
        assert viewmodel == expected