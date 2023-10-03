from src.modules.update_action.app.update_action_usecase import UpdateActionUsecase
from src.modules.update_action.app.update_action_viewmodel import UpdateActionViewmodel
from src.modules.update_member.app.update_member_usecase import UpdateMemberUsecase
from src.modules.update_member.app.update_member_viewmodel import UpdateMemberViewmodel
from src.shared.domain.enums.active_enum import ACTIVE
from src.shared.domain.enums.course_enum import COURSE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.enums.stack_enum import STACK
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock


class Test_UpdateMemberViewmodel:
    def test_update_member_viewmodel(self):
        repo = MemberRepositoryMock()
        usecase = UpdateMemberUsecase(repo)
        member = usecase(
            ra=repo.members[0].ra, new_name='Joao Brancas')

        viewmodel = UpdateMemberViewmodel(member=member).to_dict()
        expected = {
            'member': {
                'name':"Joao Brancas",
                'email_dev':"vsoller.devmaua@gmail.com",
                'email':"vsoller@airubio.com",
                'ra':"21017310",
                'role':ROLE.DIRECTOR.value,
                'stack':STACK.INFRA.value,
                'year':1,
                'cellphone':"11991758098",
                'course':COURSE.ECA.value,
                'hired_date':1634576165000,
                'active':ACTIVE.ACTIVE.value,
                'deactivated_date':None
            },
            'message': 'the member was updated'
        }
        
        assert viewmodel == expected