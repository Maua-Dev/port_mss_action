from src.shared.domain.entities.project import Project
from src.shared.helpers.errors.domain_errors import EntityError, EntityParameterTypeError
import pytest

class Test_Project():
    def test_project(self):
        project = Project(
            code = 'PQ',
            name='test_project',
            description='test_description'
        )
        assert type(project) == Project

    def test_project_code_must_be_str(self):
        with pytest.raises(EntityError):
            Project(
                code = 123,
                name='test_project',
                description='test_description'
                         )

    def test_project_code_must_be_2_characters(self):
        with pytest.raises(EntityError):
            Project(
                code = 'PQP',
                name='test_project',
                description='test_description'
                         )
    
    def test_project_code_must_be_alphabetical(self):
        with pytest.raises(EntityError):
            Project(
                code = 'PQ1',
                name='test_project',
                description='test_description'
                         )
     
    def test_project_code_must_be_uppercase(self):
        with pytest.raises(EntityError):
            Project(
                code = 'Qqp',
                name='test_project',
                description='test_description'
                         )
            
    def test_project_name_must_be_str(self):
        with pytest.raises(EntityError):
            Project(
                code = 'MFD',
                name=1,
                description='test_description'
                         )
            
    def test_project_code_must_be_uppercase(self):
        with pytest.raises(EntityError):
            Project(
                code = 'MFD',
                name='test_project',
                description=1
                         )
        