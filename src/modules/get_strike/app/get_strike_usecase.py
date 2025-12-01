from src.shared.domain.entities.strike import Strike
from src.shared.domain.repositories.strike_repository_interface import IStrikeRepository
from src.shared.domain.repositories.member_repository_interface import IMemberRepository
from src.shared.helpers.errors.controller_errors import WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound, UnregisteredUser, UserNotAllowed
from src.shared.domain.enums.active_enum import ACTIVE

class GetStrikeUsecase:
    def __init__(self, repo_strike: IStrikeRepository, repo_member: IMemberRepository):
        self.repo_strike = repo_strike
        self.repo_member = repo_member

    def __call__(self, strike_id: str, user_id: str):

        # 1. Validação do Usuário Solicitante (Segurança)
        if self.repo_member.get_member(user_id=user_id) is None:
            raise UnregisteredUser()

        user = self.repo_member.get_member(user_id=user_id)
        if user.active != ACTIVE.ACTIVE:
            raise UserNotAllowed()

        # 2. Validação do ID do Strike
        if type(strike_id) is not str:
            raise WrongTypeParameter('strike_id', 'str', type(strike_id))

        if not Strike.validate_strike_id(strike_id):
            raise EntityError('strike_id')

        # 3. Busca no Repositório
        strike = self.repo_strike.find_by_id(strike_id=strike_id)

        if strike is None:
            raise NoItemsFound('strike_id')

        return strike