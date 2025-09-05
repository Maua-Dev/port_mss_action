import boto3

class AuthConfirmUsecase:
    def __init__(self, client_id: str, region: str):
        self.client_id = client_id
        self.region = region

    def __call__(self, email: str, code: str):
        idp = boto3.client("cognito-idp", region_name=self.region)
        idp.confirm_sign_up(ClientId=self.client_id, Username=email, ConfirmationCode=code)
        return {"ok": True}
