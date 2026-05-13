class BedrockIngestionViewModel:
    def __init__(self, data: dict):
        self.data = data

    def to_dict(self):
        return {
            'data': self.data,
            'message': 'Bedrock ingestion started successfully'
        }
