class GetUploadUrlViewModel:
    def __init__(self, url: str):
        self.url = url

    def to_dict(self):
        return {
            'upload_url': self.url,
            'message': 'presigned url generated successfully'
        }