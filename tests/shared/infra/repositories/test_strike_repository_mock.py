from src.shared.domain.entities.strike import Strike
from src.shared.infra.repositories.strike_repository_mock import StrikeRepositoryMock
from src.shared.domain.enums.strike_category import STRIKE_CATEGORY

import pytest
from src.shared.domain.entities.strike import Strike
from src.shared.domain.enums.strike_category import STRIKE_CATEGORY
from src.shared.infra.repositories.strike_repository_mock import StrikeRepositoryMock


class TestStrikeRepositoryMock:
    
    def setup_method(self):
        """Executado antes de cada teste"""
        self.repo = StrikeRepositoryMock()
        self.sample_strike = Strike(
            strike_id="12345678-1234-1234-1234-123456789abc",
            owner_user_id="87654321-4321-4321-4321-cba987654321",
            target_user_id="11111111-2222-3333-4444-555555555555",
            applier_user_id="22222222-3333-4444-5555-666666666666",
            ocurred_date=1704067200000,
            category=STRIKE_CATEGORY.MISCONDUCT,
            description="Teste de strike"
        )

    def test_create_strike(self):
        # Act
        result = self.repo.create_strike(self.sample_strike)
        
        # Assert
        assert result == self.sample_strike
        assert len(self.repo.strikes) == 21  # 20 exemplos + 1 novo
        assert self.sample_strike in self.repo.strikes

    def test_get_all(self):
        # Act
        result = self.repo.get_all()
        
        # Assert
        assert len(result) == 20  # Os 20 exemplos iniciais
        assert isinstance(result, list)
        
    def test_get_all_should_return_copy_not_original_list(self):
        # Act
        result = self.repo.get_all()
        original_length = len(self.repo.strikes)
        
        # Modifica a lista retornada
        result.clear()
        
        # Assert
        assert len(self.repo.strikes) == original_length  # Lista original não foi afetada

    def test_find_by_id_should_return_strike_when_exists(self):
        # Arrange
        existing_strike_id = "a1b2c3d4-e5f6-7890-1234-567890abcdef"  # Primeiro exemplo
        
        # Act
        result = self.repo.find_by_id(existing_strike_id)
        
        # Assert
        assert result is not None
        assert result.strike_id == existing_strike_id
        assert result.category == STRIKE_CATEGORY.MISCONDUCT

    def test_find_by_id_should_return_none_when_not_exists(self):
        # Arrange
        non_existing_id = "99999999-9999-9999-9999-999999999999"
        
        # Act
        result = self.repo.find_by_id(non_existing_id)
        
        # Assert
        assert result is None

    def test_find_by_id_should_return_none_when_id_is_empty(self):
        # Act & Assert
        assert self.repo.find_by_id("") is None
        assert self.repo.find_by_id(None) is None

    def test_remove_should_return_and_remove_strike_when_exists(self):
        # Arrange
        existing_strike_id = "a1b2c3d4-e5f6-7890-1234-567890abcdef"
        initial_count = len(self.repo.strikes)
        
        # Act
        result = self.repo.remove(existing_strike_id)
        
        # Assert
        assert result is not None
        assert result.strike_id == existing_strike_id
        assert len(self.repo.strikes) == initial_count - 1
        
        # Verifica que realmente foi removido
        assert self.repo.find_by_id(existing_strike_id) is None

    def test_remove_should_return_none_when_not_exists(self):
        # Arrange
        non_existing_id = "99999999-9999-9999-9999-999999999999"
        initial_count = len(self.repo.strikes)
        
        # Act
        result = self.repo.remove(non_existing_id)
        
        # Assert
        assert result is None
        assert len(self.repo.strikes) == initial_count  # Não removeu nada

    def test_remove_should_return_none_when_id_is_empty(self):
        # Arrange
        initial_count = len(self.repo.strikes)
        
        # Act & Assert
        assert self.repo.remove("") is None
        assert self.repo.remove(None) is None
        assert len(self.repo.strikes) == initial_count

    def test_remove_twice_same_id_should_work_correctly(self):
        # Arrange
        existing_strike_id = "a1b2c3d4-e5f6-7890-1234-567890abcdef"
        
        # Act
        first_removal = self.repo.remove(existing_strike_id)
        second_removal = self.repo.remove(existing_strike_id)
        
        # Assert
        assert first_removal is not None
        assert second_removal is None  # Já foi removido

    def test_repository_should_start_with_20_examples(self):
        # Assert
        assert len(self.repo.strikes) == 20
        
        # Verifica se tem strikes de todas as categorias
        categories = {strike.category for strike in self.repo.strikes}
        expected_categories = {
            STRIKE_CATEGORY.MISCONDUCT,
            STRIKE_CATEGORY.LACK_OF_COMMITMENT,
            STRIKE_CATEGORY.RULE_VIOLATION,
            STRIKE_CATEGORY.OTHER
        }
        assert categories == expected_categories

    def test_all_example_strikes_have_valid_data(self):
        # Act
        strikes = self.repo.get_all()
        
        # Assert
        for strike in strikes:
            assert len(strike.strike_id) == 36
            assert len(strike.owner_user_id) == 36
            assert len(strike.target_user_id) == 36
            assert len(strike.applier_user_id) == 36
            assert isinstance(strike.ocurred_date, int)
            assert isinstance(strike.category, STRIKE_CATEGORY)
            assert strike.description is not None
            assert len(strike.description) <= 500

    def test_create_multiple_strikes(self):
        # Arrange
        strike1 = Strike(
            strike_id="aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
            owner_user_id="11111111-1111-1111-1111-111111111111",
            target_user_id="22222222-2222-2222-2222-222222222222",
            applier_user_id="33333333-3333-3333-3333-333333333333",
            ocurred_date=1704067200000,
            category=STRIKE_CATEGORY.OTHER,
            description="Strike 1"
        )
        
        strike2 = Strike(
            strike_id="bbbbbbbb-cccc-dddd-eeee-ffffffffffffffff",
            owner_user_id="44444444-4444-4444-4444-444444444444",
            target_user_id="55555555-5555-5555-5555-555555555555",
            applier_user_id="66666666-6666-6666-6666-666666666666",
            ocurred_date=1704153600000,
            category=STRIKE_CATEGORY.RULE_VIOLATION,
            description="Strike 2"
        )
        
        # Act
        self.repo.create_strike(strike1)
        self.repo.create_strike(strike2)
        
        # Assert
        assert len(self.repo.strikes) == 22  # 20 + 2
        assert self.repo.find_by_id(strike1.strike_id) == strike1
        assert self.repo.find_by_id(strike2.strike_id) == strike2