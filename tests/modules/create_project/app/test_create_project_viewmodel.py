from src.modules.create_project.app.create_project_viewmodel import CreateProjectViewmodel
from src.shared.domain.entities.project import Project


class Test_CreateProjectViewmodel:
    def test_create_project_viewmodel(self):
        project = Project(
            code='DM', 
            name='DevMedias', 
            description='Projeto que calcula a média de notas e quanto um aluno precisa tirar para passar de ano', 
            po_user_id='93bc6ada-c0d1-7054-66ab-e17414c48ae3', 
            scrum_user_id='7465hvnb-143g-1675-86HnG-75hgnFbcg36', 
            start_date=1649955600000,
            members_user_ids=['93bc6ada-c0d1-7054-66ab-e17414c48ae3', '7465hvnb-143g-1675-86HnG-75hgnFbcg36'],
            photo='https://i.imgur.com/7QF7uCk.png'
            )
        viewmodel = CreateProjectViewmodel(project).to_dict()
        expected = {
            'project':{
                'code':'DM',
                'name':'DevMedias',
                'description':'Projeto que calcula a média de notas e quanto um aluno precisa tirar para passar de ano',
                'po_user_id':'93bc6ada-c0d1-7054-66ab-e17414c48ae3',
                'scrum_user_id':'7465hvnb-143g-1675-86HnG-75hgnFbcg36',
                'start_date':1649955600000,
                'members_user_ids':['7465hvnb-143g-1675-86HnG-75hgnFbcg36','93bc6ada-c0d1-7054-66ab-e17414c48ae3'],
                'photo':'https://i.imgur.com/7QF7uCk.png'
            },
            'message':'the project was created'
            }
        
        assert viewmodel == expected
        
    def test_create_project_viewmodel_without_photo(self):
        project = Project(
            code='DM', 
            name='DevMedias', 
            description='Projeto que calcula a média de notas e quanto um aluno precisa tirar para passar de ano', 
            po_user_id='93bc6ada-c0d1-7054-66ab-e17414c48ae3', 
            scrum_user_id='7465hvnb-143g-1675-86HnG-75hgnFbcg36', 
            start_date=1649955600000,
            members_user_ids=['93bc6ada-c0d1-7054-66ab-e17414c48ae3', '7465hvnb-143g-1675-86HnG-75hgnFbcg36']
            )
        viewmodel = CreateProjectViewmodel(project).to_dict()
        expected = {
            'project':{
                'code':'DM',
                'name':'DevMedias',
                'description':'Projeto que calcula a média de notas e quanto um aluno precisa tirar para passar de ano',
                'po_user_id':'93bc6ada-c0d1-7054-66ab-e17414c48ae3',
                'scrum_user_id':'7465hvnb-143g-1675-86HnG-75hgnFbcg36',
                'start_date':1649955600000,
                'members_user_ids':['7465hvnb-143g-1675-86HnG-75hgnFbcg36','93bc6ada-c0d1-7054-66ab-e17414c48ae3'],
                'photo':None
            },
            'message':'the project was created'
            }
        
        assert viewmodel == expected