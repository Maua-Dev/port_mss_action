from src.modules.get_upload_url.app.get_upload_url_viewmodel import GetUploadUrlViewModel

class Test_GetUploadUrlViewModel:
    def test_get_upload_url_viewmodel(self):
        viewmodel = GetUploadUrlViewModel("https://example.com/presigned_url")
        expected = {
            'upload_url': "https://example.com/presigned_url",
            'message': 'presigned url generated successfully'
        }
        assert viewmodel.to_dict() == expected
