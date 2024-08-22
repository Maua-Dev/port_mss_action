from src.modules.get_all_members.app.get_all_members_usecase import GetAllMembersUsecase
from src.shared.domain.entities.member import Member
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound
import pytest
class Test_GetAllMembersUseCase:
    def test_get_all_members_usecase(self):
        memberrepo = MemberRepositoryMock()
        actionrepo = ActionRepositoryMock()
        usecase = GetAllMembersUsecase(memberrepo=memberrepo, actionrepo=actionrepo)
        
        members = usecase("93bc6ada-c0d1-7054-66ab-e17414c48ae3", start_date= 1624576165000, end_date= 1690046000000)
        assert type(members) == list
        assert len(members) == 11
        assert all([type(member) == Member for member in members])
        assert members[0].hours_worked == 143960000000


    def test_get_all_members_usecase_user_id_not_found(self):

        memberrepo = MemberRepositoryMock()
        actionrepo = ActionRepositoryMock()
        usecase = GetAllMembersUsecase(memberrepo=memberrepo, actionrepo=actionrepo)
        
        with pytest.raises(NoItemsFound):
            members = usecase(user_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxdxxxxxx", start_date= 1624576165000, end_date= 1690046000000)

    def test_get_all_member_usecase_inactive_user(self):
        memberrepo = MemberRepositoryMock()
        actionrepo = ActionRepositoryMock()
        usecase = GetAllMembersUsecase(memberrepo=memberrepo, actionrepo=actionrepo)
        
        with pytest.raises(ForbiddenAction):
            members = usecase(user_id="76h35dg4-h76v-1875-987hn-h67gfv45Gt4", start_date= 1624576165000, end_date= 1690046000000)
    
    def test_get_all_members_usecase_no_start_and_end_date(self):
        memberrepo = MemberRepositoryMock()
        actionrepo = ActionRepositoryMock()
        usecase = GetAllMembersUsecase(memberrepo=memberrepo, actionrepo=actionrepo)
        
        members = usecase("93bc6ada-c0d1-7054-66ab-e17414c48ae3")
        assert type(members) == list
        assert len(members) == 11
        assert all([type(member) == Member for member in members])
        assert members[0].hours_worked == 0

