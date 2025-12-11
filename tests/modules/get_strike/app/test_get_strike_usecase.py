from src.modules.get_strike.app.get_strike_usecase import GetStrikeUsecase
from src.shared.domain.entities.strike import Strike
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock
from src.shared.infra.repositories.strike_repository_mock import StrikeRepositoryMock
from src.shared.helpers.errors.usecase_errors import NoItemsFound, UnregisteredUser, UserNotAllowed
from src.shared.helpers.errors.domain_errors import EntityError
import pytest

class Test_GetStrikeUsecase:

    def test_get_strike_usecase(self):
        member_repo = MemberRepositoryMock()
        strike_repo = StrikeRepositoryMock()
        usecase = GetStrikeUsecase(repo_strike=strike_repo, repo_member=member_repo)

        # Pegando um strike existente no Mock
        target_strike = strike_repo.strikes[0]
        requester_user = member_repo.members[0] # Usuário ativo

        strike = usecase(strike_id=target_strike.strike_id, user_id=requester_user.user_id)

        assert strike == target_strike
        assert isinstance(strike, Strike)

    def test_get_strike_usecase_not_found(self):
        member_repo = MemberRepositoryMock()
        strike_repo = StrikeRepositoryMock()
        usecase = GetStrikeUsecase(repo_strike=strike_repo, repo_member=member_repo)

        requester_user = member_repo.members[0]

        # ID válido (formato uuid) mas inexistente
        non_existent_id = "11111111-1111-1111-1111-111111111111"

        with pytest.raises(NoItemsFound):
            usecase(strike_id=non_existent_id, user_id=requester_user.user_id)

    def test_get_strike_usecase_invalid_id_format(self):
        member_repo = MemberRepositoryMock()
        strike_repo = StrikeRepositoryMock()
        usecase = GetStrikeUsecase(repo_strike=strike_repo, repo_member=member_repo)

        requester_user = member_repo.members[0]

        with pytest.raises(EntityError):
            usecase(strike_id="id_invalido", user_id=requester_user.user_id)

    def test_get_strike_usecase_unregistered_user(self):
        member_repo = MemberRepositoryMock()
        strike_repo = StrikeRepositoryMock()
        usecase = GetStrikeUsecase(repo_strike=strike_repo, repo_member=member_repo)

        target_strike = strike_repo.strikes[0]

        with pytest.raises(UnregisteredUser):
            usecase(strike_id=target_strike.strike_id, user_id='id-nao-registrado')

    def test_get_strike_usecase_inactive_user(self):
        member_repo = MemberRepositoryMock()
        strike_repo = StrikeRepositoryMock()
        usecase = GetStrikeUsecase(repo_strike=strike_repo, repo_member=member_repo)

        target_strike = strike_repo.strikes[0]
        # Assumindo que o membro no índice 2 ou com ID específico esteja inativo/on_hold no Mock
        # Ajuste o índice conforme seu Mock real se necessário
        inactive_user = member_repo.members[2] # Geralmente um user inativo nos mocks padrão

        with pytest.raises(UserNotAllowed):
             usecase(strike_id=target_strike.strike_id, user_id=inactive_user.user_id)