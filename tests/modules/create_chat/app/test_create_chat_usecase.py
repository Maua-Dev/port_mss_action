import pytest
from unittest.mock import patch, MagicMock
from botocore.exceptions import ClientError
from src.modules.create_chat.app.create_chat_usecase import CreateChatUsecase
from src.shared.helpers.errors.usecase_errors import BedrockIntegrationError

class Test_CreateChatUsecase:
    @patch('src.modules.create_chat.app.create_chat_usecase.boto3.client')
    def test_create_chat_usecase_success(self, mock_boto_client):
        mock_client_instance = MagicMock()
        mock_boto_client.return_value = mock_client_instance
        
        mock_client_instance.retrieve_and_generate.return_value = {
            'output': {
                'text': 'A resposta correta da base de conhecimento.'
            }
        }
        
        usecase = CreateChatUsecase()
        
        question = "Qual é a hidratação correta?"
        answer = usecase(question=question)
        
        assert answer == 'A resposta correta da base de conhecimento.'
        mock_client_instance.retrieve_and_generate.assert_called_once()

    @patch('src.modules.create_chat.app.create_chat_usecase.boto3.client')
    def test_create_chat_usecase_client_error(self, mock_boto_client):
        mock_client_instance = MagicMock()
        mock_boto_client.return_value = mock_client_instance
        
        error_response = {'Error': {'Message': 'AccessDeniedException'}}
        mock_client_instance.retrieve_and_generate.side_effect = ClientError(error_response, 'RetrieveAndGenerate')
        
        usecase = CreateChatUsecase()
        
        with pytest.raises(BedrockIntegrationError):
            usecase(question="Qual é a hidratação correta?")

    @patch('src.modules.create_chat.app.create_chat_usecase.boto3.client')
    def test_create_chat_usecase_generic_error(self, mock_boto_client):
        mock_client_instance = MagicMock()
        mock_boto_client.return_value = mock_client_instance
        
        mock_client_instance.retrieve_and_generate.side_effect = Exception("Generic error")
        
        usecase = CreateChatUsecase()
        
        with pytest.raises(BedrockIntegrationError):
            usecase(question="Qual é a hidratação correta?")
