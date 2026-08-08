import pytest
import json
from unittest.mock import patch
from src.modules.create_chat.app.create_chat_presenter import lambda_handler

class Test_CreateChatPresenter:
    @patch('src.modules.create_chat.app.create_chat_usecase.CreateChatUsecase.__call__')
    def test_create_chat_presenter_success(self, mock_usecase_call):
        mock_usecase_call.return_value = 'Resposta da AI mockada'
        
        event = {
            'body': json.dumps({
                'question': 'Como funciona a hidratação?'
            }),
            'requestContext': {
                'authorizer': {
                    'claims': {
                        'sub': '75648hbr-184n-1985-91han-7ghn4HgF182',
                        'name': 'Test User',
                        'email': 'test@test.com',
                        'custom:is_admin': 'false',
                        'custom:role': 'USER'
                    }
                }
            }
        }
        
        response = lambda_handler(event, None)
        
        assert response['statusCode'] == 200
        body = json.loads(response['body'])
        assert body['answer'] == 'Resposta da AI mockada'

    def test_create_chat_presenter_missing_question(self):
        event = {
            'body': json.dumps({}),
            'requestContext': {
                'authorizer': {
                    'claims': {
                        'sub': '75648hbr-184n-1985-91han-7ghn4HgF182',
                        'name': 'Test User',
                        'email': 'test@test.com',
                        'custom:is_admin': 'false',
                        'custom:role': 'USER'
                    }
                }
            }
        }
        
        response = lambda_handler(event, None)
        
        assert response['statusCode'] == 400
        assert json.loads(response['body']) == 'Field question is missing'
