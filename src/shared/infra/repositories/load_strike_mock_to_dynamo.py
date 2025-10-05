import boto3

from src.shared.infra.repositories.strike_repository_dynamo import StrikeRepositoryDynamo
from src.shared.infra.repositories.strike_repository_mock import StrikeRepositoryMock

def setup_dynamo_table():
    print('Setting up dynamo table...')
    dynamo_client = boto3.client(
        'dynamodb', endpoint_url='http://localhost:8000', region_name='sa-east-1')
    tables= dynamo_client.list_tables()['TableNames']
    table_name= "port_mss_strike-table"

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
            GlobalSecondaryIndexes=[
                {
                    'IndexName': 'GSI-STRIKE',
                    'KeySchema': [
                        {
                            'KeyType': 'HASH',
                            'AttributeName': 'GSI-STRIKE-PK'
                        },
                    ],
                    'Projection': {
                        'ProjectionType': 'ALL'
                    }
                },

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
                    'AttributeName': 'GSI-STRIKE-PK',
                    'AttributeType': 'S'
                },
            ],
            BillingMode='PAY_PER_REQUEST',
        )
        print('Table "port_mss_strike-table" created!\n')
    else:
        print('Table already exists!\n')


def load_mock_to_local_dynamo():
    repo_dynamo= StrikeRepositoryDynamo()
    repo_mock= StrikeRepositoryMock()

    print('Loading mock data to dynamo...')

    print('Loading strikes...')

    count= 0

    for strike in repo_mock.strikes:
        print(f'Loading strikes {strike.strike_id}...')

        repo_dynamo.create_strike(strike=strike)
        count+= 1

        print(strike)
    
    print('Done!')
    print(count)


def load_mock_to_real_dynamo():
    repo_dynamo= StrikeRepositoryDynamo()
    repo_mock= StrikeRepositoryMock()

    print('Loading mock data to dynamo...')

    count = 0

    for strike in repo_mock.strikes:
        print(f'Loading strikes {strike.strike_id}...')

        repo_dynamo.create_strike(strike=strike)
        count+= 1

        print(strike)
    
    print('Done!')

if __name__ == '__main__':
    setup_dynamo_table()
    load_mock_to_real_dynamo()