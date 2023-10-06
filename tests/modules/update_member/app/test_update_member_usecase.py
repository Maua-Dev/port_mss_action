import pytest
from src.modules.update_member.app.update_member_usecase import UpdateMemberUsecase
from src.shared.domain.enums.active_enum import ACTIVE
from src.shared.domain.enums.course_enum import COURSE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.enums.stack_enum import STACK
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock


class Test_UpdateMemberUsecase:
    def test_update_member_usecase(self):
        repo = MemberRepositoryMock()
        usecase = UpdateMemberUsecase(repo=repo)
        member = usecase(     ra="21017310",new_name="Joao Branco",
                new_email_dev="jbranco.devmaua@gmail.com",
                new_role=ROLE.HEAD,
                new_stack=STACK.BACKEND,
                new_year=3,
                new_cellphone="11991152348",
                new_course=COURSE.ECM,
                new_active=ACTIVE.ACTIVE,new_deactivated_date=1231212323)
        
        assert repo.members[0] == member

    def test_update_member_usecase_new_name(self):
        repo = MemberRepositoryMock()
        usecase = UpdateMemberUsecase(repo=repo)
        member = usecase(     ra="21017310",new_name="Teste Testudo"
              )
        
        assert repo.members[0].name == "Teste Testudo"

    def test_update_member_usecase_new_year(self):
        repo = MemberRepositoryMock()
        usecase = UpdateMemberUsecase(repo=repo)
        member = usecase(     ra="21017310",    new_year=35
              )
        
        assert repo.members[0].year == 35

    def test_update_member_usecase_new_role(self):
        repo = MemberRepositoryMock()
        usecase = UpdateMemberUsecase(repo=repo)
        member = usecase(     ra="21017310", new_role=ROLE.HEAD
              )
        
        assert repo.members[0].role == ROLE.HEAD
    def test_update_member_no_items_found(self):
        repo = MemberRepositoryMock()
        usecase = UpdateMemberUsecase(repo=repo)

        with pytest.raises(NoItemsFound):
            member = usecase(ra="11111111",new_name="Joao Branco",
                new_email_dev="jbranco.devmaua@gmail.com",
                new_role=ROLE.HEAD,
                new_stack=STACK.BACKEND,
                new_year=3,
                new_cellphone="11991152348",
                new_course=COURSE.ECM,
                new_active=ACTIVE.ACTIVE)