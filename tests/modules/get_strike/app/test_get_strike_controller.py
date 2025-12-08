from src.modules.get_strike.app.get_strike_controller import GetStrikeController
from src.modules.get_strike.app.get_strike_usecase import GetStrikeUsecase
from src.modules.get_strike.app.get_strike_viewmodel import GetStrikeViewmodel
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock
from src.shared.infra.repositories.strike_repository_mock import StrikeRepositoryMock
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from pprint import pprint

class Test_GetStrikeController:
    member_repo = MemberRepositoryMock()
    strike_repo = StrikeRepositoryMock()

    usecase = GetStrikeUsecase(repo_strike=strike_repo, repo_member=member_repo)
    controller = GetStrikeController(usecase)

    requester_user = member_repo.members[0]
    target_strike = strike_repo.strikes[0]

    def test_get_strike_controller(self):
        request = HttpRequest(
            body={
                'requester_user': {
                    "sub": self.requester_user.user_id,
                    "name": self.requester_user.name,
                    "email": self.requester_user.email,
                    "custom:isMaua": True
                },
                'strike_id': self.target_strike.strike_id
            }
        )

        # Gerando o esperado dinamicamente usando o Viewmodel para garantir consistência
        expected_dict = GetStrikeViewmodel(self.target_strike).to_dict()

        response = self.controller(request)

        pprint(response.body)

        assert response.status_code == 200
        assert response.body == expected_dict

    def test_get_strike_controller_missing_strike_id(self):
        request = HttpRequest(
            body={
                'requester_user': {
                    "sub": self.requester_user.user_id,
                    "name": self.requester_user.name,
                    "email": self.requester_user.email,
                    "custom:isMaua": True
                }
                # strike_id faltando
            }
        )

        response = self.controller(request)
        assert response.status_code == 400
        assert response.body == "Field strike_id is missing"

    def test_get_strike_controller_not_found(self):
        request = HttpRequest(
            body={
                'requester_user': {
                    "sub": self.requester_user.user_id,
                    "name": self.requester_user.name,
                    "email": self.requester_user.email,
                    "custom:isMaua": True
                },
                'strike_id': "11111111-1111-1111-1111-111111111111" # ID Válido mas inexistente
            }
        )

        response = self.controller(request)
        assert response.status_code == 404

    def test_get_strike_controller_invalid_uuid(self):
        request = HttpRequest(
            body={
                'requester_user': {
                    "sub": self.requester_user.user_id,
                    "name": self.requester_user.name,
                    "email": self.requester_user.email,
                    "custom:isMaua": True
                },
                'strike_id': "id-invalido"
            }
        )

        response = self.controller(request)
        assert response.status_code == 400

    def test_get_strike_controller_forbidden_user(self):
         request = HttpRequest(
            body={
                'requester_user': {
                    "sub": "id-nao-registrado", # User não registrado
                    "name": "Ghost",
                    "email": "ghost@maua.br",
                    "custom:isMaua": True
                },
                'strike_id': self.target_strike.strike_id
            }
        )

         response = self.controller(request)
         assert response.status_code == 403