from src.modules.create_project.app.create_project_controller import CreateProjectController
from src.modules.create_project.app.create_project_usecase import CreateProjectUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock


class Test_CreateProjectController:
    def test_create_project_controller(self):
        
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = CreateProjectUsecase(repo=repo, repo_member=repo_member)
        controller = CreateProjectController(usecase=usecase)
        request = HttpRequest(body = {
            "requester_user": {
                "sub": repo_member.members[0].user_id,
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            },
            'code':'DM',
            'name':'DevMedias',
            'description':'Projeto que calcula a média de notas e quanto um aluno precisa tirar para passar de ano',
            'po_user_id':'5f55f6a5-a66e-4fff-9faf-72cd478bd5a0',
            'scrum_user_id':'5f55f6a5-a66e-4fff-9faf-72cd478bd5a0',
            'start_date':1649955600000,
            'members_user_ids':['9183jBnh-997H-1010-10god-914gHy46tBh','51ah5jaj-c9jm-1345-666ab-e12341c14a3','5f55f6a5-a66e-4fff-9faf-72cd478bd5a0'],
            'photos':['https://i.imgur.com/7QF7uCk.png']
        })
        response = controller(request)
        assert response.status_code == 201
        assert response.body['message'] == 'the project was created'
        assert response.body['project']['code'] == 'DM'
        assert response.body['project']['name'] == 'DevMedias'
        assert response.body['project']['description'] == 'Projeto que calcula a média de notas e quanto um aluno precisa tirar para passar de ano'
        assert response.body['project']['po_user_id'] == '5f55f6a5-a66e-4fff-9faf-72cd478bd5a0'
        assert response.body['project']['scrum_user_id'] == '5f55f6a5-a66e-4fff-9faf-72cd478bd5a0'
        assert response.body['project']['start_date'] == 1649955600000
        assert response.body['project']['members_user_ids'] == ['51ah5jaj-c9jm-1345-666ab-e12341c14a3','5f55f6a5-a66e-4fff-9faf-72cd478bd5a0','9183jBnh-997H-1010-10god-914gHy46tBh']
        assert response.body['project']['photos'] == ['https://i.imgur.com/7QF7uCk.png']
        
    def test_create_project_controller_missing_photos(self):
            
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = CreateProjectUsecase(repo=repo, repo_member=repo_member)
        controller = CreateProjectController(usecase=usecase)
        request = HttpRequest(body = {
            "requester_user": {
                "sub": repo_member.members[0].user_id,
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            },
            'code':'DM',
            'name':'DevMedias',
            'description':'Projeto que calcula a média de notas e quanto um aluno precisa tirar para passar de ano',
            'po_user_id':'5f55f6a5-a66e-4fff-9faf-72cd478bd5a0',
            'scrum_user_id':'5f55f6a5-a66e-4fff-9faf-72cd478bd5a0',
            'start_date':1649955600000,
            'members_user_ids':['93bc6ada-c0d1-7054-66ab-e17414c48ae3', '7465hvnb-143g-1675-86HnG-75hgnFbcg36','5f55f6a5-a66e-4fff-9faf-72cd478bd5a0']
        })
        response = controller(request)
        assert response.status_code == 201
        assert response.body['project']['photos'] == []
        
    def test_create_project_controller_missing_code(self):
        
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = CreateProjectUsecase(repo=repo, repo_member=repo_member)
        controller = CreateProjectController(usecase=usecase)
        request = HttpRequest(body = {
            "requester_user": {
                "sub": repo_member.members[0].user_id,
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            },
            'name':'DevMedias',
            'description':'Projeto que calcula a média de notas e quanto um aluno precisa tirar para passar de ano',
            'po_user_id':'5f55f6a5-a66e-4fff-9faf-72cd478bd5a0',
            'scrum_user_id':'5f55f6a5-a66e-4fff-9faf-72cd478bd5a0',
            'start_date':1649955600000,
            'members_user_ids':['93bc6ada-c0d1-7054-66ab-e17414c48ae3', '7465hvnb-143g-1675-86HnG-75hgnFbcg36','5f55f6a5-a66e-4fff-9faf-72cd478bd5a0']
        })
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field code is missing'
        
    def test_create_project_controller_missing_name(self):
        
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = CreateProjectUsecase(repo=repo, repo_member=repo_member)
        controller = CreateProjectController(usecase=usecase)
        request = HttpRequest(body = {
            "requester_user": {
                "sub": repo_member.members[0].user_id,
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            },
            'code':'DM',
            'description':'Projeto que calcula a média de notas e quanto um aluno precisa tirar para passar de ano',
            'po_user_id':'5f55f6a5-a66e-4fff-9faf-72cd478bd5a0',
            'scrum_user_id':'5f55f6a5-a66e-4fff-9faf-72cd478bd5a0',
            'start_date':1649955600000,
            'members_user_ids':['93bc6ada-c0d1-7054-66ab-e17414c48ae3', '7465hvnb-143g-1675-86HnG-75hgnFbcg36','5f55f6a5-a66e-4fff-9faf-72cd478bd5a0']
        })

        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field name is missing'
        
    def test_create_project_controller_missing_description(self):
        
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = CreateProjectUsecase(repo=repo, repo_member=repo_member)
        controller = CreateProjectController(usecase=usecase)
        request = HttpRequest(body = {
            "requester_user": {
                "sub": repo_member.members[0].user_id,
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            },
            'code':'DM',
            'name':'DevMedias',
            'po_user_id':'5f55f6a5-a66e-4fff-9faf-72cd478bd5a0',
            'scrum_user_id':'5f55f6a5-a66e-4fff-9faf-72cd478bd5a0',
            'start_date':1649955600000,
            'members_user_ids':['93bc6ada-c0d1-7054-66ab-e17414c48ae3', '7465hvnb-143g-1675-86HnG-75hgnFbcg36','5f55f6a5-a66e-4fff-9faf-72cd478bd5a0']
        })

        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field description is missing'
        
    def test_create_project_controller_missing_po_user_id(self):
        
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = CreateProjectUsecase(repo=repo, repo_member=repo_member)
        controller = CreateProjectController(usecase=usecase)
        request = HttpRequest(body = {
            "requester_user": {
                "sub": repo_member.members[0].user_id,
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            },
            'code':'DM',
            'name':'DevMedias',
            'description':'Projeto que calcula a média de notas e quanto um aluno precisa tirar para passar de ano',
            'scrum_user_id':'5f55f6a5-a66e-4fff-9faf-72cd478bd5a0',
            'start_date':1649955600000,
            'members_user_ids':['7465hvnb-143g-1675-86HnG-75hgnFbcg36','5f55f6a5-a66e-4fff-9faf-72cd478bd5a0']
        })

        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field po_user_id is missing'
        
    def test_create_project_controller_missing_scrum_user_id(self):
        
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = CreateProjectUsecase(repo=repo, repo_member=repo_member)
        controller = CreateProjectController(usecase=usecase)
        request = HttpRequest(body = {
            "requester_user": {
                "sub": repo_member.members[0].user_id,
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            },
            'code':'DM',
            'name':'DevMedias',
            'description':'Projeto que calcula a média de notas e quanto um aluno precisa tirar para passar de ano',
            'po_user_id':'5f55f6a5-a66e-4fff-9faf-72cd478bd5a0',
            'start_date':1649955600000,
            'members_user_ids':['93bc6ada-c0d1-7054-66ab-e17414c48ae3','5f55f6a5-a66e-4fff-9faf-72cd478bd5a0']
        })

        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field scrum_user_id is missing'
        
    def test_create_project_controller_missing_start_date(self):
        
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = CreateProjectUsecase(repo=repo, repo_member=repo_member)
        controller = CreateProjectController(usecase=usecase)
        request = HttpRequest(body = {
            "requester_user": {
                "sub": repo_member.members[0].user_id,
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            },
            'code':'DM',
            'name':'DevMedias',
            'description':'Projeto que calcula a média de notas e quanto um aluno precisa tirar para passar de ano',
            'po_user_id':'5f55f6a5-a66e-4fff-9faf-72cd478bd5a0',
            'scrum_user_id':'5f55f6a5-a66e-4fff-9faf-72cd478bd5a0',
            'members_user_ids':['93bc6ada-c0d1-7054-66ab-e17414c48ae3', '7465hvnb-143g-1675-86HnG-75hgnFbcg36','5f55f6a5-a66e-4fff-9faf-72cd478bd5a0']
        })

        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field start_date is missing'
        
    def test_create_project_controller_wrong_type_photos(self):
            
            repo = ActionRepositoryMock()
            repo_member = MemberRepositoryMock()
            usecase = CreateProjectUsecase(repo=repo, repo_member=repo_member)
            controller = CreateProjectController(usecase=usecase)
    
            request = HttpRequest(body = {
                "requester_user": {
                "sub": repo_member.members[0].user_id,
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
                },
                'code':'DM',
                'name':'DevMedias',
                'description':'Projeto que calcula a média de notas e quanto um aluno precisa tirar para passar de ano',
                'po_user_id':'5f55f6a5-a66e-4fff-9faf-72cd478bd5a0',
                'scrum_user_id':'5f55f6a5-a66e-4fff-9faf-72cd478bd5a0',
                'start_date':1649955600000,
                'members_user_ids':['93bc6ada-c0d1-7054-66ab-e17414c48ae3', '7465hvnb-143g-1675-86HnG-75hgnFbcg36','5f55f6a5-a66e-4fff-9faf-72cd478bd5a0'],
                'photos':'https://i.imgur.com/7QF7uCk.png'
            })
    
            response = controller(request)
            assert response.status_code == 400
            assert response.body == 'Field photos is not valid'
            
    def test_create_project_controller_photos_not_list_of_str(self):
                
                repo = ActionRepositoryMock()
                repo_member = MemberRepositoryMock()
                usecase = CreateProjectUsecase(repo=repo, repo_member=repo_member)
                controller = CreateProjectController(usecase=usecase)
        
                request = HttpRequest(body = {
                    "requester_user": {
                        "sub": repo_member.members[0].user_id,
                        "name": repo_member.members[0].name,
                        "email": repo_member.members[0].email,
                        "custom:isMaua": True
                    },
                    'code':'DM',
                    'name':'DevMedias',
                    'description':'Projeto que calcula a média de notas e quanto um aluno precisa tirar para passar de ano',
                    'po_user_id':'5f55f6a5-a66e-4fff-9faf-72cd478bd5a0',
                    'scrum_user_id':'5f55f6a5-a66e-4fff-9faf-72cd478bd5a0',
                    'start_date':1649955600000,
                    'members_user_ids':['93bc6ada-c0d1-7054-66ab-e17414c48ae3', '7465hvnb-143g-1675-86HnG-75hgnFbcg36','5f55f6a5-a66e-4fff-9faf-72cd478bd5a0'],
                    'photos':[1,2,3]
                })
        
                response = controller(request)
                assert response.status_code == 400
                assert response.body == 'Field photos is not valid'

    def test_create_project_controller_missing_members_user_ids(self):
        
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = CreateProjectUsecase(repo=repo, repo_member=repo_member)
        controller = CreateProjectController(usecase=usecase)
        request = HttpRequest(body = {
            "requester_user": {
                "sub": repo_member.members[0].user_id,
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            },
            'code':'DM',
            'name':'DevMedias',
            'description':'Projeto que calcula a média de notas e quanto um aluno precisa tirar para passar de ano',
            'po_user_id':'5f55f6a5-a66e-4fff-9faf-72cd478bd5a0',
            'scrum_user_id':'5f55f6a5-a66e-4fff-9faf-72cd478bd5a0',
            'start_date':1649955600000,
        })

        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field members_user_ids is missing'

    def test_create_project_controller_wrong_type_members_user_ids(self):
            
            repo = ActionRepositoryMock()
            repo_member = MemberRepositoryMock()
            usecase = CreateProjectUsecase(repo=repo, repo_member=repo_member)
            controller = CreateProjectController(usecase=usecase)
            request = HttpRequest(body = {
                "requester_user": {
                        "sub": repo_member.members[0].user_id,
                        "name": repo_member.members[0].name,
                        "email": repo_member.members[0].email,
                        "custom:isMaua": True
                },
                'code':'DM',
                'name':'DevMedias',
                'description':'Projeto que calcula a média de notas e quanto um aluno precisa tirar para passar de ano',
                'po_user_id':'5f55f6a5-a66e-4fff-9faf-72cd478bd5a0',
                'scrum_user_id':'5f55f6a5-a66e-4fff-9faf-72cd478bd5a0',
                'start_date':1649955600000,
                'members_user_ids':1
            })
    
            response = controller(request)
            assert response.status_code == 400
            assert response.body == 'Field members_user_ids is not valid'

    def test_create_project_controller_members_user_ids_not_list_of_str(self):
                
                repo = ActionRepositoryMock()
                repo_member = MemberRepositoryMock()
                usecase = CreateProjectUsecase(repo=repo, repo_member=repo_member)
                controller = CreateProjectController(usecase=usecase)
                request = HttpRequest(body = {
                    "requester_user": {
                        "sub": repo_member.members[0].user_id,
                        "name": repo_member.members[0].name,
                        "email": repo_member.members[0].email,
                        "custom:isMaua": True
                    },
                    'code':'DM',
                    'name':'DevMedias',
                    'description':'Projeto que calcula a média de notas e quanto um aluno precisa tirar para passar de ano',
                    'po_user_id':'5f55f6a5-a66e-4fff-9faf-72cd478bd5a0',
                    'scrum_user_id':'5f55f6a5-a66e-4fff-9faf-72cd478bd5a0',
                    'start_date':1649955600000,
                    'members_user_ids':[1,2,3]
                })
        
                response = controller(request)
                assert response.status_code == 400
                assert response.body == 'Field members_user_ids is not valid'
    
    def test_create_project_controller_requester_user_missing(self):
                
                repo = ActionRepositoryMock()
                repo_member = MemberRepositoryMock()
                usecase = CreateProjectUsecase(repo=repo, repo_member=repo_member)
                controller = CreateProjectController(usecase=usecase)
                request = HttpRequest(body = {
                    'code':'DM',
                    'name':'DevMedias',
                    'description':'Projeto que calcula a média de notas e quanto um aluno precisa tirar para passar de ano',
                    'po_user_id':'5f55f6a5-a66e-4fff-9faf-72cd478bd5a0',
                    'scrum_user_id':'5f55f6a5-a66e-4fff-9faf-72cd478bd5a0',
                    'start_date':1649955600000,
                    'members_user_ids':['93bc6ada-c0d1-7054-66ab-e17414c48ae3', '7465hvnb-143g-1675-86HnG-75hgnFbcg36','5f55f6a5-a66e-4fff-9faf-72cd478bd5a0']
                })
        
                response = controller(request)
                assert response.status_code == 400
                assert response.body == 'Field requester_user is missing'

    def test_create_project_controller_po_user_id_is_not_from_business_stack(self):
                repo = ActionRepositoryMock()
                repo_member = MemberRepositoryMock()
                usecase = CreateProjectUsecase(repo=repo, repo_member=repo_member)
                controller = CreateProjectController(usecase=usecase)
                request = HttpRequest(body = {
                    "requester_user": {
                        "sub": repo_member.members[0].user_id,
                        "name": repo_member.members[0].name,
                        "email": repo_member.members[0].email,
                        "custom:isMaua": True
                    },
                    'code':'DM',
                    'name':'DevMedias',
                    'description':'Projeto que calcula a média de notas e quanto um aluno precisa tirar para passar de ano',
                    'po_user_id':'76h35dg4-h76v-1875-987hn-h67gfv45Gt4',
                    'scrum_user_id':'5f55f6a5-a66e-4fff-9faf-72cd478bd5a0',
                    'start_date':1649955600000,
                    'members_user_ids':['76h35dg4-h76v-1875-987hn-h67gfv45Gt4', '7465hvnb-143g-1675-86HnG-75hgnFbcg36']
                })
        
                response = controller(request)
                assert response.status_code == 400
                assert response.body == 'That user is not a member of the Business Stack'

    def test_create_project_controller_scrum_user_id_is_not_from_business_stack(self):
                repo = ActionRepositoryMock()
                repo_member = MemberRepositoryMock()
                usecase = CreateProjectUsecase(repo=repo, repo_member=repo_member)
                controller = CreateProjectController(usecase=usecase)
                request = HttpRequest(body = {
                    "requester_user": {
                        "sub": repo_member.members[0].user_id,
                        "name": repo_member.members[0].name,
                        "email": repo_member.members[0].email,
                        "custom:isMaua": True
                    },
                    'code':'DM',
                    'name':'DevMedias',
                    'description':'Projeto que calcula a média de notas e quanto um aluno precisa tirar para passar de ano',
                    'po_user_id':'5f55f6a5-a66e-4fff-9faf-72cd478bd5a0',
                    'scrum_user_id':'76h35dg4-h76v-1875-987hn-h67gfv45Gt4',
                    'start_date':1649955600000,
                    'members_user_ids':['76h35dg4-h76v-1875-987hn-h67gfv45Gt4', '7465hvnb-143g-1675-86HnG-75hgnFbcg36']
                })
        
                response = controller(request)
                assert response.status_code == 400
                assert response.body == 'That user is not a member of the Business Stack'