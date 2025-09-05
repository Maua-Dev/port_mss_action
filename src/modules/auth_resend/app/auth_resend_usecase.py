import boto3

class AuthResendUsecase:
    def __init__(self, client_id: str, region: str):
        self.client_id = client_id
        self.region = region

    def __call__(self, email: str):
        idp = boto3.client("cognito-idp", region_name=self.region)
        resp = idp.resend_confirmation_code(ClientId=self.client_id, Username=email)
        return {"code_delivery": resp.get("CodeDeliveryDetails", {})}
