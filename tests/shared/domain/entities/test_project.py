from datetime import datetime
from src.shared.domain.entities.project import Project
from src.shared.helpers.errors.domain_errors import EntityError, EntityParameterTypeError
import pytest


class Test_Project():
    def test_project(self):
        project = Project(
            code='PQ',
            name='test_project',
            description='test_description',
            po_RA="22011020",
            scrum_RA="22011020",
            start_date=1672585200000,
            photos=['https://i.imgur.com/gHoRKJU.png',
                    'https://i.imgur.com/gHoRKJU.png'],
            members=['22011020']
        )
        assert type(project) == Project
        assert project.photos != []

    def test_project_code_must_be_str(self):
        with pytest.raises(EntityError):
            Project(
                code=123,
                name='test_project',
                description='test_description',
                po_RA="22011020",
                scrum_RA="22011020",
                start_date=1672585200000,
                photos=['https://i.imgur.com/gHoRKJU.png',
                        'https://i.imgur.com/gHoRKJU.png'],
                members=['22011020']
            )

    def test_project_code_must_be_2_characters(self):
        with pytest.raises(EntityError):
            Project(
                code='PQP',
                name='test_project',
                description='test_description',
                po_RA="22011020",
                scrum_RA="22011020",
                start_date=1672585200000,
                photos=['https://i.imgur.com/gHoRKJU.png',
                        'https://i.imgur.com/gHoRKJU.png'],
                members=['22011020']
            )

    def test_project_code_must_be_alphabetical(self):
        with pytest.raises(EntityError):
            Project(
                code='P1',
                name='test_project',
                description='test_description',
                po_RA="22011020",
                scrum_RA="22011020",
                start_date=1672585200000,
                photos=['https://i.imgur.com/gHoRKJU.png',
                        'https://i.imgur.com/gHoRKJU.png'],
                members=['22011020']
            )

    def test_project_code_must_be_uppercase(self):
        with pytest.raises(EntityError):
            Project(
                code='Qp',
                name='test_project',
                description='test_description',
                po_RA="22011020",
                scrum_RA="22011020",
                start_date=1672585200000,
                photos=['https://i.imgur.com/gHoRKJU.png',
                        'https://i.imgur.com/gHoRKJU.png'],
                members=['22011020']
            )

    def test_project_name_must_be_str(self):
        with pytest.raises(EntityError):
            Project(
                code='MF',
                name=1,
                description='test_description',
                po_RA="22011020",
                scrum_RA="22011020",
                start_date=1672585200000,
                photos=['https://i.imgur.com/gHoRKJU.png',
                        'https://i.imgur.com/gHoRKJU.png'],
                members=['22011020']
            )

    def test_project_description_must_be_str(self):
        with pytest.raises(EntityError):
            Project(
                code='MF',
                name='test_project',
                description=1,
                po_RA="22011020",
                scrum_RA="22011020",
                start_date=1672585200000,
                photos=['https://i.imgur.com/gHoRKJU.png',
                        'https://i.imgur.com/gHoRKJU.png'],
                members=['22011020']
            )

    def test_project_po_RA_must_be_str(self):
        with pytest.raises(EntityError):
            Project(
                code='MF',
                name='test_project',
                description='test_description',
                po_RA=1,
                scrum_RA="22011020",
                start_date=1672585200000,
                photos=['https://i.imgur.com/gHoRKJU.png',
                        'https://i.imgur.com/gHoRKJU.png'],
                members=['22011020']
            )

    def test_project_po_ra_must_be_8_characters(self):
        with pytest.raises(EntityError):
            Project(
                code='MF',
                name='test_project',
                description='test_description',
                po_RA="2201102",
                scrum_RA="22011020",
                start_date=1672585200000,
                photos=['https://i.imgur.com/gHoRKJU.png',
                        'https://i.imgur.com/gHoRKJU.png'],
                members=['22011020']
            )

    def test_project_po_ra_must_be_decimal(self):
        with pytest.raises(EntityError):
            Project(
                code='MF',
                name='test_project',
                description='test_description',
                po_RA="2201102a",
                scrum_RA="22011020",
                start_date=1672585200000,
                photos=['https://i.imgur.com/gHoRKJU.png',
                        'https://i.imgur.com/gHoRKJU.png'],
                members=['22011020']
            )
    
    def test_project_scrum_RA_must_be_str(self):
        with pytest.raises(EntityError):
            Project(
                code='MF',
                name='test_project',
                description='test_description',
                po_RA="22011020",
                scrum_RA=1,
                start_date=1672585200000,
                photos=['https://i.imgur.com/gHoRKJU.png',
                        'https://i.imgur.com/gHoRKJU.png'],
                members=['22011020']
            )
            
    def test_project_scrum_ra_must_be_8_characters(self):
        with pytest.raises(EntityError):
            Project(
                code='MF',
                name='test_project',
                description='test_description',
                po_RA="22011020",
                scrum_RA="2201102",
                start_date=1672585200000,
                photos=['https://i.imgur.com/gHoRKJU.png',
                        'https://i.imgur.com/gHoRKJU.png'],
                members=['22011020']
            )
            
    def test_project_scrum_ra_must_be_decimal(self):
        with pytest.raises(EntityError):
            Project(
                code='MF',
                name='test_project',
                description='test_description',
                po_RA="22011020",
                scrum_RA="2201102a",
                start_date=1672585200000,
                photos=['https://i.imgur.com/gHoRKJU.png',
                        'https://i.imgur.com/gHoRKJU.png'],
                members=['22011020']
            )
            
    def test_project_start_date_must_be_int(self):
        with pytest.raises(EntityError):
            Project(
                code='MF',
                name='test_project',
                description='test_description',
                po_RA="22011020",
                scrum_RA="22011020",
                start_date="1672585200000",
                photos=['https://i.imgur.com/gHoRKJU.png',
                        'https://i.imgur.com/gHoRKJU.png'],
                members=['22011020'] 
            )
            
    def test_project_start_date_must_be_greater_than_0(self):
        with pytest.raises(EntityError):
            Project(
                code='MF',
                name='test_project',
                description='test_description',
                po_RA="22011020",
                scrum_RA="22011020",
                start_date=-362,
                photos=['https://i.imgur.com/gHoRKJU.png',
                        'https://i.imgur.com/gHoRKJU.png'], 
                members=['22011020']
            )
            
    def test_project_start_date_must_be_smaller_than_now(self):
        now = int(datetime.now().timestamp() * 1000)
        with pytest.raises(EntityError):
            Project(
                code='MF',
                name='test_project',
                description='test_description',
                po_RA="22011020",
                scrum_RA="22011020",
                start_date=now + 3000,
                photos=['https://i.imgur.com/gHoRKJU.png',
                        'https://i.imgur.com/gHoRKJU.png'],
                members=['22011020']
            )
            
    def test_project_photos_can_be_none(self):
        project = Project(
            code='MF',
            name='test_project',
            description='test_description',
            po_RA="22011020",
            scrum_RA="22011020",
            start_date=1672585200000,
            members=['22011020']
        )
        assert project.photos == []
        
    def test_project_photos_must_be_list(self):
        with pytest.raises(EntityError):
            Project(
                code='MF',
                name='test_project',
                description='test_description',
                po_RA="22011020",
                scrum_RA="22011020",
                start_date=1672585200000,
                photos='https://i.imgur.com/gHoRKJU.png',
                members=['22011020']
            )

    def test_project_members_must_be_list(self):
        with pytest.raises(EntityError):
            Project(
                code='MF',
                name='test_project',
                description='test_description',
                po_RA="22011020",
                scrum_RA="22011020",
                start_date=1672585200000,
                photos=['https://i.imgur.com/gHoRKJU.png'],
                members='22011020'
            )

    def test_project_members_less_than_one(self):
        with pytest.raises(EntityError):
            Project(
                code='MF',
                name='test_project',
                description='test_description',
                po_RA="22011020",
                scrum_RA="22011020",
                start_date=1672585200000,
                photos=['https://i.imgur.com/gHoRKJU.png'],
                members=[]
            )

    def test_project_members_invalid_ra(self):
        with pytest.raises(EntityError):
            Project(
                code='MF',
                name='test_project',
                description='test_description',
                po_RA="22011020",
                scrum_RA="22011020",
                start_date=1672585200000,
                photos=['https://i.imgur.com/gHoRKJU.png'],
                members=['22011020', '2201102a']
            )

    def test_project_members_duplicated_member(self):
        project = Project(
            code='PQ',
            name='test_project',
            description='test_description',
            po_RA="22011020",
            scrum_RA="22011121",
            start_date=1672585200000,
            photos=['https://i.imgur.com/gHoRKJU.png'],
            members=['22011020', '22011020', '22011121']
        )

        assert project.members == ['22011020','22011121']

    def test_project_po_RA_not_in_members(self):
        with pytest.raises(EntityError):
            Project(
                code='PQ',
                name='test_project',
                description='test_description',
                po_RA="22011020",
                scrum_RA="22011121",
                start_date=1672585200000,
                photos=['https://i.imgur.com/gHoRKJU.png'],
                members=['22011022', '22011121']
            )