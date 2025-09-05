from typing import Optional
import boto3

class AuthSignUpUsecase:
    def __init__(self, client_id: str, region: str):
        self.client_id = client_id
        self.region = region

    def __call__(self, email: str, password: str, name: Optional[str] = None):
        idp = boto3.client("cognito-idp", region_name=self.region)
        attrs = [{"Name": "email", "Value": email}]
        if name:
            attrs.append({"Name": "name", "Value": name})

        resp = idp.sign_up(
            ClientId=self.client_id,
            Username=email,
            Password=password,
            UserAttributes=attrs
        )
        return {
            "user_sub": resp.get("UserSub"),
            "user_confirmed": resp.get("UserConfirmed", False),
            "code_delivery": resp.get("CodeDeliveryDetails", {})
        }
