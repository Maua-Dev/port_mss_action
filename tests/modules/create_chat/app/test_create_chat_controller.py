import pytest
from unittest.mock import MagicMock
from src.modules.create_chat.app.create_chat_controller import CreateChatController
from src.modules.create_chat.app.create_chat_usecase import CreateChatUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.helpers.errors.usecase_errors import BedrockIntegrationError

class Test_CreateChatController:
    def test_create_chat_controller_success(self):
        usecase = MagicMock()
        usecase.return_value = 'Resposta da AI'
        
        controller = CreateChatController(usecase)
        
        request = HttpRequest(body={
            'requester_user': {
                'sub': '75648hbr-184n-1985-91han-7ghn4HgF182',
                'name': 'Test User',
                'email': 'test@test.com',
                'custom:is_admin': 'false',
                'custom:role': 'USER'
            },
            'question': 'Qual é a temperatura ideal?'
        })
        
        response = controller(request)
        
        assert response.status_code == 200
        assert response.body['answer'] == 'Resposta da AI'
        usecase.assert_called_once_with(question='Qual é a temperatura ideal?')

    def test_create_chat_controller_missing_requester_user(self):
        usecase = MagicMock()
        
        controller = CreateChatController(usecase)
        
        request = HttpRequest(body={
            'question': 'Qual é a temperatura ideal?'
        })
        
        response = controller(request)
        
        assert response.status_code == 400
        assert response.body == 'Field requester_user is missing'

    def test_create_chat_controller_missing_question(self):
        usecase = MagicMock()
        
        controller = CreateChatController(usecase)
        
        request = HttpRequest(body={
            'requester_user': {
                'sub': '75648hbr-184n-1985-91han-7ghn4HgF182',
                'name': 'Test User',
                'email': 'test@test.com',
                'custom:is_admin': 'false',
                'custom:role': 'USER'
            }
        })
        
        response = controller(request)
        
        assert response.status_code == 400
        assert response.body == 'Field question is missing'

    def test_create_chat_controller_wrong_type_question(self):
        usecase = MagicMock(spec=CreateChatUsecase)
        
        controller = CreateChatController(usecase)
        
        request = HttpRequest(body={
            'requester_user': {
                'sub': '75648hbr-184n-1985-91han-7ghn4HgF182',
                'name': 'Test User',
                'email': 'test@test.com',
                'custom:is_admin': 'false',
                'custom:role': 'USER'
            },
            'question': 123
        })
        
        response = controller(request)
        
        assert response.status_code == 400
        assert response.body == "Field question isn't in the right type.\n Received: <class 'int'>.\n Expected: str"

    def test_create_chat_controller_bedrock_error(self):
        usecase = MagicMock(spec=CreateChatUsecase)
        usecase.side_effect = BedrockIntegrationError('Access denied')
        
        controller = CreateChatController(usecase)
        
        request = HttpRequest(body={
            'requester_user': {
                'sub': '75648hbr-184n-1985-91han-7ghn4HgF182',
                'name': 'Test User',
                'email': 'test@test.com',
                'custom:is_admin': 'false',
                'custom:role': 'USER'
            },
            'question': 'Qual é a temperatura ideal?'
        })
        
        response = controller(request)
        
        assert response.status_code == 503
        assert response.body == 'Error with bedrock integration: Access denied'
