import pytest
from src.modules.update_member.app.update_member_usecase import UpdateMemberUsecase
from src.shared.domain.enums.active_enum import ACTIVE
from src.shared.domain.enums.course_enum import COURSE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.enums.stack_enum import STACK
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock
from src.shared.helpers.errors.domain_errors import EntityError

class Test_UpdateMemberUsecase:
    def test_update_member_usecase(self):
        repo = MemberRepositoryMock()
        usecase = UpdateMemberUsecase(repo=repo)
        member = usecase(user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",new_name="Joao Branco",
                new_email_dev="jbranco.devmaua@gmail.com",
                new_role=ROLE.HEAD,
                new_stack=STACK.BACKEND,
                new_year=3,
                new_cellphone="11991152348",
                new_course=COURSE.ECM,
                new_active=ACTIVE.ACTIVE,new_deactivated_date=42312123230000)
        
        assert repo.members[0] == member

    def test_update_member_usecase_new_name(self):
        repo = MemberRepositoryMock()
        usecase = UpdateMemberUsecase(repo=repo)
        member = usecase(user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",new_name="Teste Testudo")
        
        assert repo.members[0].name == "Teste Testudo"

    def test_update_member_usecase_new_year(self):
        repo = MemberRepositoryMock()
        usecase = UpdateMemberUsecase(repo=repo)
        member = usecase(user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",new_year=3)
        
        assert repo.members[0].year == 3

    def test_update_member_usecase_new_role(self):
        repo = MemberRepositoryMock()
        usecase = UpdateMemberUsecase(repo=repo)
        member = usecase(user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3", new_role=ROLE.HEAD)
        
        assert repo.members[0].role == ROLE.HEAD

    def test_update_member_usecase_new_stack(self):
        repo = MemberRepositoryMock()
        usecase = UpdateMemberUsecase(repo=repo)
        member = usecase(user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3", new_stack=STACK.FRONTEND)
        
        assert repo.members[0].stack == STACK.FRONTEND

    def test_update_member_usecase_new_year(self):
        repo = MemberRepositoryMock()
        usecase = UpdateMemberUsecase(repo=repo)
        member = usecase(user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3", new_year=5)
        
        assert repo.members[0].year == 5

    def test_update_member_usecase_new_cellphone(self):
        repo = MemberRepositoryMock()
        usecase = UpdateMemberUsecase(repo=repo)
        member = usecase(user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3", new_cellphone="11991751111")
        
        assert repo.members[0].cellphone == "11991751111"

    def test_update_member_usecase_new_course(self):
        repo = MemberRepositoryMock()
        usecase = UpdateMemberUsecase(repo=repo)
        member = usecase(user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3", new_course=COURSE.DSG)
        
        assert repo.members[0].course == COURSE.DSG

    def test_update_member_usecase_new_active(self):
        repo = MemberRepositoryMock()
        usecase = UpdateMemberUsecase(repo=repo)
        member = usecase(user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3", new_active=ACTIVE.DISCONNECTED)
        
        assert repo.members[0].active == ACTIVE.DISCONNECTED



    def test_update_member_no_items_found(self):
        repo = MemberRepositoryMock()
        usecase = UpdateMemberUsecase(repo=repo)

        with pytest.raises(NoItemsFound):
            member = usecase(user_id="93bc6ada-c0d1-7054-66ab-e11111c48ae3",new_name="Joao Branco",
                new_email_dev="jbranco.devmaua@gmail.com",
                new_role=ROLE.HEAD,
                new_stack=STACK.BACKEND,
                new_year=3,
                new_cellphone="11991152348",
                new_course=COURSE.ECM,
                new_active=ACTIVE.ACTIVE)
            

    def test_update_member_name_wrongtype(self):
        with pytest.raises(EntityError):
            repo = MemberRepositoryMock()
            usecase = UpdateMemberUsecase(repo=repo)
            first_user = repo.members[0]

            updated_user = usecase(user_id=first_user.user_id, new_name=3)

    def test_update_member_email_dev_wrongtype(self):
        with pytest.raises(EntityError):
            repo = MemberRepositoryMock()
            usecase = UpdateMemberUsecase(repo=repo)
            first_user = repo.members[0]

            updated_user = usecase(user_id=first_user.user_id, new_email_dev=3)
    
    def test_update_member_email_dev_invalid(self):
        with pytest.raises(EntityError):
            repo = MemberRepositoryMock()
            usecase = UpdateMemberUsecase(repo=repo)
            first_user = repo.members[0]

            updated_user = usecase(user_id=first_user.user_id, new_email_dev="@gmail.com")

    def test_update_member_role_wrongtype(self):
        with pytest.raises(EntityError):
            repo = MemberRepositoryMock()
            usecase = UpdateMemberUsecase(repo=repo)
            first_user = repo.members[0]

            updated_user = usecase(user_id=first_user.user_id, new_role="@gmail.com")   
            
    def test_update_member_stack_wrongtype(self):
        with pytest.raises(EntityError):
            repo = MemberRepositoryMock()
            usecase = UpdateMemberUsecase(repo=repo)
            first_user = repo.members[0]

            updated_user = usecase(user_id=first_user.user_id, new_stack="@gmail.com")   

    def test_update_member_new_year_wrongtype(self):
        with pytest.raises(EntityError):
            repo = MemberRepositoryMock()
            usecase = UpdateMemberUsecase(repo=repo)
            first_user = repo.members[0]

            updated_user = usecase(user_id=first_user.user_id, new_year="@gmail.com")   

    def test_update_member_new_year_higher_than_6(self):
        with pytest.raises(EntityError):
            repo = MemberRepositoryMock()
            usecase = UpdateMemberUsecase(repo=repo)
            first_user = repo.members[0]

            updated_user = usecase(user_id=first_user.user_id, new_year=7)   

    def test_update_member_new_year_lesser_than_1(self):
        with pytest.raises(EntityError):
            repo = MemberRepositoryMock()
            usecase = UpdateMemberUsecase(repo=repo)
            first_user = repo.members[0]

            updated_user = usecase(user_id=first_user.user_id, new_year=0)   

    def test_update_member_new_cellphone_wrongtype(self):
        with pytest.raises(EntityError):
            repo = MemberRepositoryMock()
            usecase = UpdateMemberUsecase(repo=repo)
            first_user = repo.members[0]

            updated_user = usecase(user_id=first_user.user_id, new_cellphone=0)  

    def test_update_member_new_cellphone_invalid(self):
        with pytest.raises(EntityError):
            repo = MemberRepositoryMock()
            usecase = UpdateMemberUsecase(repo=repo)
            first_user = repo.members[0]

            updated_user = usecase(user_id=first_user.user_id, new_cellphone="0")  

    def test_update_member_new_course_wrongtype(self):
        with pytest.raises(EntityError):
            repo = MemberRepositoryMock()
            usecase = UpdateMemberUsecase(repo=repo)
            first_user = repo.members[0]

            updated_user = usecase(user_id=first_user.user_id, new_course=0)

    def test_update_member_new_deactivated_date_wrongtype(self):
        with pytest.raises(EntityError):
            repo = MemberRepositoryMock()
            usecase = UpdateMemberUsecase(repo=repo)
            first_user = repo.members[0]

            updated_user = usecase(user_id=first_user.user_id, new_deactivated_date=0)  
  
    def test_update_member_new_active_date_wrongtype(self):
        with pytest.raises(EntityError):
            repo = MemberRepositoryMock()
            usecase = UpdateMemberUsecase(repo=repo)
            first_user = repo.members[0]

            updated_user = usecase(user_id=first_user.user_id, new_active=0)  