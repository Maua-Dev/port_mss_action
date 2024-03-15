from src.modules.create_project.app.create_project_viewmodel import CreateProjectViewmodel
from src.shared.domain.entities.project import Project


class Test_CreateProjectViewmodel:
    def test_create_project_viewmodel(self):
        project = Project(
            code='DM', 
            name='DevMedias', 
            description='Projeto que calcula a média de notas e quanto um aluno precisa tirar para passar de ano', 
            po_user_id='21021031', 
            scrum_user_id='17033730', 
            start_date=1649955600000,
            members=['21021031', '17033730'],
            photos=['https://i.imgur.com/7QF7uCk.png']
            )
        viewmodel = CreateProjectViewmodel(project).to_dict()
        expected = {
            'project':{
                'code':'DM',
                'name':'DevMedias',
                'description':'Projeto que calcula a média de notas e quanto um aluno precisa tirar para passar de ano',
                'po_user_id':'21021031',
                'scrum_user_id':'17033730',
                'start_date':1649955600000,
                'members':['17033730','21021031'],
                'photos':[
                    'https://i.imgur.com/7QF7uCk.png'
                ]
            },
            'message':'the project was created'
            }
        
        assert viewmodel == expected
        
    def test_create_project_viewmodel_without_photos(self):
        project = Project(
            code='DM', 
            name='DevMedias', 
            description='Projeto que calcula a média de notas e quanto um aluno precisa tirar para passar de ano', 
            po_user_id='21021031', 
            scrum_user_id='17033730', 
            start_date=1649955600000,
            members=['21021031', '17033730']
            )
        viewmodel = CreateProjectViewmodel(project).to_dict()
        expected = {
            'project':{
                'code':'DM',
                'name':'DevMedias',
                'description':'Projeto que calcula a média de notas e quanto um aluno precisa tirar para passar de ano',
                'po_user_id':'21021031',
                'scrum_user_id':'17033730',
                'start_date':1649955600000,
                'members':['17033730','21021031'],
                'photos':[]
            },
            'message':'the project was created'
            }
        
        assert viewmodel == expected