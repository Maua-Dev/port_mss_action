import boto3

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
                            'AttributeName': 'occured-date'
                        }
                    ],
                    'Projection': {
                        'ProjectionType': 'ALL',
                    }
                }
            ],
            GlobalSecondaryIndexes=[
                {
                    'IndexName': 'GSI-OWNER',
                    'KeySchema': [
                        {
                            'KeyType': 'HASH',
                            'AttributeName': 'GSI-OWNER-PK'
                        },
                        {
                            'KeyType': 'RANGE',
                            'AttributeName': 'GSI-OWNER-SK'
                        }
                    ],
                    'Projection': {
                        'ProjectionType': 'ALL',
                    }
                },
                {
                    'IndexName': 'GSI-TARGET',
                    'KeySchema': [
                        {
                            'KeyType': 'HASH',
                            'AttributeName': 'GSI-TARGET-PK'
                        },
                        {
                            'KeyType': 'RANGE',
                            'AttributeName': 'GSI-TARGET-SK'
                        }
                    ],
                    'Projection': {
                        'ProjectionType': 'ALL',
                    }
                },
                {
                    'IndexName': 'GSI-APPLIER',
                    'KeySchema': [
                        {
                            'KeyType': 'HASH',
                            'AttributeName': 'GSI-APPLIER-PK'
                        },
                        {
                            'KeyType': 'RANGE',
                            'AttributeName': 'GSI-APPLIER-SK'
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
                    'AttributeName': 'occured-date',
                    'AttributeType': 'N'
                },
                {
                    'AttributeName': 'GSI-OWNER-PK',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'GSI-OWNER-SK',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'GSI-TARGET-PK',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'GSI-TARGET-SK',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'GSI-APPLIER-PK',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'GSI-APPLIER-SK',
                    'AttributeType': 'S'
                }

            ],
            BillingMode='PAY_PER_REQUEST',
        )
        print('Table "port_mss_strike-table" created!\n')
    else:
        print('Table already exists!\n')

def load_mock_to_dynamo():
    repo_dynamo= StrikeRepositoryDynamo()
    repo_mock= StrikeRepositoryMock()

    print('Loading mock data to dynamo...')