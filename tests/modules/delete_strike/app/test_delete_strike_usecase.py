from tkinter import ACTIVE
import pytest

from src.modules.delete_strike.app.delete_strike_usecase import DeleteStrikeUseCase
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import (
    ForbiddenAction,
    UnregisteredUser,
    UserNotAllowed,
    NoItemsFound,
)
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock
from src.shared.infra.repositories.strike_repository_mock import StrikeRepositoryMock


class Test_DeleteStrikeUseCase:

    def setup_method(self):
        self.repo = StrikeRepositoryMock()
        self.repo_member = MemberRepositoryMock()
        self.usecase = DeleteStrikeUseCase(repo=self.repo, repo_member=self.repo_member)

    def test_delete_strike_success(self):
        len_before = len(self.repo.strikes)
        strike_id_to_delete = self.repo.strikes[0].strike_id
        user_id = self.repo_member.members[0].user_id

        deleted_strike = self.usecase(user_id=user_id, strike_id=strike_id_to_delete)

        assert len(self.repo.strikes) == len_before - 1
        assert deleted_strike.strike_id == strike_id_to_delete

    def test_delete_strike_unregistered_user(self):
        with pytest.raises(UnregisteredUser):
            self.usecase(user_id="non-existent-user", strike_id=self.repo.strikes[0].strike_id)

    def test_delete_strike_invalid_strike_id(self):
        user_id = self.repo_member.members[0].user_id
        with pytest.raises(EntityError):
            self.usecase(user_id=user_id, strike_id="invalid-strike-id")

    def test_delete_strike_not_found(self):
        user_id = self.repo_member.members[0].user_id
        with pytest.raises(NoItemsFound):
            self.usecase(user_id=user_id, strike_id="11111111-2222-3333-4444-555555555555")

    def test_delete_strike_forbidden(self):
        strike = self.repo.strikes[0]
        another_user = next(u for u in self.repo_member.members if u.user_id != strike.owner_user_id and u.active.value == "ACTIVE")

        with pytest.raises(ForbiddenAction):
            self.usecase(user_id=another_user.user_id, strike_id=strike.strike_id)

from tkinter import ACTIVE
import pytest

from src.modules.delete_strike.app.delete_strike_usecase import DeleteStrikeUseCase
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import (
    ForbiddenAction,
    UnregisteredUser,
    UserNotAllowed,
    NoItemsFound,
)
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock
from src.shared.infra.repositories.strike_repository_mock import StrikeRepositoryMock


class Test_DeleteStrikeUseCase:

    def setup_method(self):
        self.repo = StrikeRepositoryMock()
        self.repo_member = MemberRepositoryMock()
        self.usecase = DeleteStrikeUseCase(repo=self.repo, repo_member=self.repo_member)

    def test_delete_strike_success(self):
        len_before = len(self.repo.strikes)
        strike_id_to_delete = self.repo.strikes[0].strike_id
        user_id = self.repo_member.members[0].user_id

        deleted_strike = self.usecase(user_id=user_id, strike_id=strike_id_to_delete)

        assert len(self.repo.strikes) == len_before - 1
        assert deleted_strike.strike_id == strike_id_to_delete

    def test_delete_strike_unregistered_user(self):
        with pytest.raises(UnregisteredUser):
            self.usecase(user_id="non-existent-user", strike_id=self.repo.strikes[0].strike_id)

    def test_delete_strike_not_found(self):
        user_id = self.repo_member.members[0].user_id
        with pytest.raises(NoItemsFound):
            self.usecase(user_id=user_id, strike_id="11111111-2222-3333-4444-555555555555")

    def test_delete_strike_forbidden(self):
        strike = self.repo.strikes[0]
        another_user = next(u for u in self.repo_member.members if u.user_id == "7gh5yf5H-857H-1234-75hng-94832hvng1s" and u.active.value == "ACTIVE")

        with pytest.raises(UserNotAllowed):
            self.usecase(user_id=another_user.user_id, strike_id=strike.strike_id)