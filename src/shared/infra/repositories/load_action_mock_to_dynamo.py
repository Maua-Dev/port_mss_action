import boto3

from src.shared.infra.repositories.action_repository_dynamo import ActionRepositoryDynamo
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock


def setup_dynamo_table():
    print('Setting up dynamo table...')
    dynamo_client = boto3.client(
        'dynamodb', endpoint_url='http://localhost:8000', region_name='sa-east-1')
    tables = dynamo_client.list_tables()['TableNames']
    table_name = "port_mss_action-table"
    
    if not table_name in tables:
        print('Creating table...')
        dynamo_client.create_table(
            TableName=table_name,
            KeySchema=[
                {
                    'AttributeName': 'PK',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': 'SK',
                    'KeyType': 'RANGE'
                }
            ],
            LocalSecondaryIndexes=[
                {
                    'IndexName': 'LSI1',
                    'KeySchema': [
                        {
                            'KeyType': 'HASH',
                            'AttributeName': 'PK'
                        },
                        {
                            'KeyType': 'RANGE',
                            'AttributeName': 'start_date'
                        }
                    ],
                    'Projection': {
                        'ProjectionType': 'ALL',
                    }
                }
            ],
            GlobalSecondaryIndexes=[
                {
                    'IndexName': 'GSI1',
                    'KeySchema': [
                        {
                            'KeyType': 'HASH',
                            'AttributeName': 'GSI1-PK'
                        },
                        {
                            'KeyType': 'RANGE',
                            'AttributeName': 'GSI1-SK'
                        }
                    ],
                    'Projection': {
                        'ProjectionType': 'ALL',
                    }
                }
                ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'PK',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'SK',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'start_date',
                    'AttributeType': 'N'
                },
                {
                    'AttributeName': 'GSI1-PK',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'GSI1-SK',
                    'AttributeType': 'S'
                }
            ],
            BillingMode='PAY_PER_REQUEST',

        )
        print('Table "port_mss_action-table" created!\n')
    else:
        print('Table already exists!\n')


def load_mock_to_local_dynamo():
    repo_dynamo = ActionRepositoryDynamo()
    repo_mock = ActionRepositoryMock()

    print('Loading mock data to dynamo...')

    print('Loading actions...')
    count = 0
    for action in repo_mock.actions:
        print(f'Loading action {action.action_id}...')
        repo_dynamo.create_action(action=action)
        count += 1
        print(action)
    print(f'{count} actions loaded!\n')
    count = 0
    for project in repo_mock.projects:
        print(f'Loading project {project.code}...')
        repo_dynamo.create_project(project=project)
        count += 1
        print(project)
    for associated_action in repo_mock.associated_actions:
        print(f'Loading associated action {associated_action.action_id}...')
        repo_dynamo.create_associated_action(associated_action=associated_action)
        count += 1
        print(associated_action)
    for member in repo_mock.members:
        print(f'Loading member {member.ra}...')
        repo_dynamo.create_member(member=member)
        count += 1
        print(member)

    print('Done!')

def load_mock_to_real_dynamo():
    repo_dynamo = ActionRepositoryDynamo()
    repo_mock = ActionRepositoryMock()

    print('Loading mock data to dynamo...')

    print('Loading actions...')
    count = 0
    for action in repo_mock.actions:
        print(f'Loading action {action.action_id}...')
        repo_dynamo.create_action(action=action)
        count += 1
        print(action)
    print(f'{count} actions loaded!\n')
    count = 0
    for project in repo_mock.projects:
        print(f'Loading project {project.code}...')
        repo_dynamo.create_project(project=project)
        count += 1
        print(project)
    for associated_action in repo_mock.associated_actions:
        print(f'Loading associated action {associated_action.action_id}...')
        repo_dynamo.create_associated_action(associated_action=associated_action)
        count += 1
        print(associated_action)
    for member in repo_mock.members:
        print(f'Loading member {member.ra}...')
        repo_dynamo.create_member(member=member)
        count += 1
        print(member)

    print('Done!')


if __name__ == '__main__':
    # setup_dynamo_table()
    load_mock_to_real_dynamo()
