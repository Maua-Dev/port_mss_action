import pytest
from src.modules.create_chat.app.create_chat_viewmodel import CreateChatViewmodel

class Test_CreateChatViewmodel:
    def test_create_chat_viewmodel(self):
        answer = 'Esta é uma resposta de teste.'
        
        viewmodel = CreateChatViewmodel(answer=answer)
        
        expected_dict = {
            'answer': 'Esta é uma resposta de teste.'
        }
        
        assert viewmodel.to_dict() == expected_dict
