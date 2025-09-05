import boto3

class AuthSignInUsecase:
    def __init__(self, client_id: str, region: str):
        self.client_id = client_id
        self.region = region

    def __call__(self, email: str, password: str):
        idp = boto3.client("cognito-idp", region_name=self.region)
        try:
            resp = idp.initiate_auth(
                ClientId=self.client_id,
                AuthFlow="USER_PASSWORD_AUTH",
                AuthParameters={"USERNAME": email, "PASSWORD": password}
            )
            if "AuthenticationResult" in resp:
                ar = resp["AuthenticationResult"]
                return {
                    "access_token": ar.get("AccessToken"),
                    "id_token": ar.get("IdToken"),
                    "refresh_token": ar.get("RefreshToken"),
                    "expires_in": ar.get("ExpiresIn")
                }
            return {"challenge": resp.get("ChallengeName")}

        except idp.exceptions.UserNotConfirmedException:
            return {"error": "UserNotConfirmed", "message": "Usuário não confirmado. Verifique seu e-mail."}

        except idp.exceptions.NotAuthorizedException as e:
            return {"error": "NotAuthorized", "message": str(e)}

        except Exception as e:
            raise e
