from src.modules.get_member.app.get_member_controller import GetMemberController
from src.modules.get_member.app.get_member_usecase import GetMemberUsecase
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from src.shared.helpers.external_interfaces.http_models import HttpRequest

class Test_GetMemberController:
    member_repo = MemberRepositoryMock()
    action_repo = ActionRepositoryMock()
    first_member = member_repo.members[0]
    usecase = GetMemberUsecase(member_repo = member_repo, action_repo = action_repo)
    controller = GetMemberController(usecase)
    
    def test_get_member_controller(self):
        request = HttpRequest(
            body={
                'requester_user': {
                    "sub": self.first_member.user_id,
                    "name": self.first_member.name,
                    "email": self.first_member.email,
                    "custom:isMaua": True
                },
                'start_date': 1624576165000,	
                'end_date': 1690046000000
            }
        )

        expected_dict = {
            'member':{
                'name' : self.first_member.name,
                'email_dev' : self.first_member.email_dev,
                'email' : self.first_member.email,
                'ra' : self.first_member.ra,
                'role' : self.first_member.role.value,
                'stack' : self.first_member.stack.value,
                'year' : self.first_member.year,
                'cellphone' : self.first_member.cellphone,
                'course' : self.first_member.course.value,
                'hired_date' : self.first_member.hired_date,
                'deactivated_date' : self.first_member.deactivated_date,
                'active' : self.first_member.active.value,
                'user_id' : self.first_member.user_id,
                'hours_worked' : 143960000000
            },
            "message" : "the member was retrieved"
        }
        
        response = self.controller(request)

        assert response.status_code == 200
        assert response.body == expected_dict
        
    def test_get_controller_with_invalid_id(self):
        request = HttpRequest(
            body={
                'requester_user': {
                    "sub": "Um id no formato inválido",
                    "name": self.first_member.name,
                    "email": self.first_member.email,
                    "custom:isMaua": True
                }
            }
        )

        response = self.controller(request)

        assert response.status_code == 400

    def test_get_controller_without_id(self):
        request = HttpRequest(
            body={
                'requester_user': {
                    "sub": None,
                    "name": self.first_member.name,
                    "email": self.first_member.email,
                    "custom:isMaua": True
                }
            }
        )

        response = self.controller(request)

        assert response.status_code == 400

    def test_get_controller_with_nonexistentid(self):
        request = HttpRequest(
            body={
                'requester_user': {
                    "sub": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                    "name": self.first_member.name,
                    "email": self.first_member.email,
                    "custom:isMaua": True
                }
            }
        )

        response = self.controller(request)

        assert response.status_code == 403
        assert response.body == "That user is not registered"

    def test_get_controller_with_no_request_user(self):
        request = HttpRequest(
            body={

            }
        )

        response = self.controller(request)
        
        assert response.status_code == 400
        assert response.body == "Field requester_user is missing"

    def test_get_member_contoller_no_start_date_and_end_date(self):
        request = HttpRequest(
            body={
                'requester_user': {
                    "sub": self.first_member.user_id,
                    "name": self.first_member.name,
                    "email": self.first_member.email,
                    "custom:isMaua": True
                }
            }
        )

        expected_dict = {
            'member':{
                'name' : self.first_member.name,
                'email_dev' : self.first_member.email_dev,
                'email' : self.first_member.email,
                'ra' : self.first_member.ra,
                'role' : self.first_member.role.value,
                'stack' : self.first_member.stack.value,
                'year' : self.first_member.year,
                'cellphone' : self.first_member.cellphone,
                'course' : self.first_member.course.value,
                'hired_date' : self.first_member.hired_date,
                'deactivated_date' : self.first_member.deactivated_date,
                'active' : self.first_member.active.value,
                'user_id' : self.first_member.user_id,
                'hours_worked' : 0
            },
            "message" : "the member was retrieved"
        }
        
        response = self.controller(request)

        assert response.status_code == 200
        assert response.body == expected_dict
