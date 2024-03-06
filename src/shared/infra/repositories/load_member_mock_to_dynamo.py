import boto3

from src.shared.infra.repositories.member_repository_dynamo import MemberRepositoryDynamo
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock


def setup_dynamo_table():
    print('Setting up dynamo table...')
    dynamo_client = boto3.client(
        'dynamodb', endpoint_url='http://localhost:8000', region_name='sa-east-1')
    tables = dynamo_client.list_tables()['TableNames']
    table_name = "port_mss_member-table"
    
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
            ],
            BillingMode='PAY_PER_REQUEST',

        )
        print('Table "port_mss_action-table" created!\n')
    else:
        print('Table already exists!\n')


def load_mock_to_local_dynamo():
    repo_dynamo = MemberRepositoryDynamo()
    repo_mock = MemberRepositoryMock()

    print('Loading mock data to dynamo...')

    print('Loading member...')
    count = 0
    for member in repo_mock.members:
        print(f'Loading member {member.user_id}...')
        repo_dynamo.create_member(member=member)
        count += 1
        print(member)

    print('Done!')

def load_mock_to_real_dynamo():
    repo_dynamo = MemberRepositoryDynamo()
    repo_mock = MemberRepositoryMock()

    print('Loading mock data to dynamo...')

    count = 0
    for member in repo_mock.members:
        print(f'Loading member {member.user_id}...')
        repo_dynamo.create_member(member=member)
        count += 1
        print(member)

    print('Done!')


if __name__ == '__main__':
    setup_dynamo_table()
    load_mock_to_real_dynamo()
