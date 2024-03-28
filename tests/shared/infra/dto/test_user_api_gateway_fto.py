from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO

class Test_UserApiGatewayDTO:
    
    def test_user_api_gateway_dto_from_api_gateway(self):
        user_data = {
            'sub': 'd61dbf66-a10f-11ed-a8fc-0242ac120002',
            'name': 'Vitor Soller',
            'email': 'vitor.soller@gmail.com', 
            'custom:isMaua': 'true'}

        user_dto = UserApiGatewayDTO.from_api_gateway(user_data)

        expected_user_dto = UserApiGatewayDTO(
            user_id = "d61dbf66-a10f-11ed-a8fc-0242ac120002",
            name = "Vitor Soller",
            is_maua = True,
            email = "vitor.soller@gmail.com")
        
        assert user_dto == expected_user_dto
    