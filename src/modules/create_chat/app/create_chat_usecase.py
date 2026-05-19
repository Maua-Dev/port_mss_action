import boto3
from src.shared.environments import Environments
from botocore.exceptions import ClientError
from src.shared.helpers.errors.usecase_errors import BedrockIntegrationError

class CreateChatUsecase:
    def __init__(self):
        self.client = boto3.client('bedrock-agent-runtime')
        self.knowledge_base_id = Environments.get_envs().knowledge_base_id

    def __call__(self, question: str) -> str:
        system_prompt_template = '''
            <system_prompt>
            Regras de comportamento:
            - Idioma: responda sempre em português.
            - Prioridade das fontes: trate o conteúdo da base como verdade canônica. Em caso de conflito com conhecimento prévio, siga a base.
            - Escopo: não responda nada que não esteja sustentado pela base. Se faltar evidência, diga que não encontrou na base e, se fizer sentido, peça detalhes adicionais.
            - Precisão: não invente nomes, números, datas, citações ou passos. Se algo estiver ambíguo ou incompleto, explicite a incerteza.
            - Concisão: respostas curtas, diretas e úteis. Evite verbosidade.
            </system_prompt>

            <base_de_conhecimento>
            $search_results$
            </base_de_conhecimento>
        '''

        try:
            response = self.client.retrieve_and_generate(
                input={
                    'text': question
                },
                retrieveAndGenerateConfiguration={
                    'type': 'KNOWLEDGE_BASE',
                    'knowledgeBaseConfiguration': {
                        'knowledgeBaseId': self.knowledge_base_id,
                        'modelArn': 'us.amazon.nova-lite-v1:0',
                        'generationConfiguration': {
                            'promptTemplate': {
                                'textPromptTemplate': system_prompt_template
                            }
                        }
                    }
                }
            )

            bedrock_feedback = response['output']['text']
            return bedrock_feedback

        except ClientError as e:
            raise BedrockIntegrationError(e.response['Error']['Message'])
        
        except Exception as e:
            raise BedrockIntegrationError(str(e))
