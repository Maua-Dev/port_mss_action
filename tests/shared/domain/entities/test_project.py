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
            po_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
            scrum_user_id="76h35dg4-h76v-1875-987hn-h67gfv45Gt4",
            start_date=1672585200000,
            photo='https://i.imgur.com/gHoRKJU.png',
            members_user_ids=['76h35dg4-h76v-1875-987hn-h67gfv45Gt4', '93bc6ada-c0d1-7054-66ab-e17414c48ae3']
        )
        assert type(project) == Project
        assert project.photos != None

    def test_project_code_must_be_str(self):
        with pytest.raises(EntityError):
            Project(
                code=123,
                name='test_project',
                description='test_description',
                po_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                scrum_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                start_date=1672585200000,
                photo='https://i.imgur.com/gHoRKJU.png',
                members_user_ids=['76h35dg4-h76v-1875-987hn-h67gfv45Gt4']
            )

    def test_project_code_must_be_2_characters(self):
        with pytest.raises(EntityError):
            Project(
                code='PQP',
                name='test_project',
                description='test_description',
                po_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                scrum_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                start_date=1672585200000,
                photo='https://i.imgur.com/gHoRKJU.png',
                members_user_ids=['76h35dg4-h76v-1875-987hn-h67gfv45Gt4']
            )

    def test_project_code_must_be_alphabetical(self):
        with pytest.raises(EntityError):
            Project(
                code='P1',
                name='test_project',
                description='test_description',
                po_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                scrum_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                start_date=1672585200000,
                photo='https://i.imgur.com/gHoRKJU.png',
                members_user_ids=['76h35dg4-h76v-1875-987hn-h67gfv45Gt4']
            )

    def test_project_code_must_be_uppercase(self):
        with pytest.raises(EntityError):
            Project(
                code='Qp',
                name='test_project',
                description='test_description',
                po_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                scrum_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                start_date=1672585200000,
                photo='https://i.imgur.com/gHoRKJU.png',
                members_user_ids=['76h35dg4-h76v-1875-987hn-h67gfv45Gt4']
            )

    def test_project_name_must_be_str(self):
        with pytest.raises(EntityError):
            Project(
                code='MF',
                name=1,
                description='test_description',
                po_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                scrum_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                start_date=1672585200000,
                photo='https://i.imgur.com/gHoRKJU.png',
                members_user_ids=['76h35dg4-h76v-1875-987hn-h67gfv45Gt4']
            )

    def test_project_description_must_be_str(self):
        with pytest.raises(EntityError):
            Project(
                code='MF',
                name='test_project',
                description=1,
                po_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                scrum_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                start_date=1672585200000,
                photo='https://i.imgur.com/gHoRKJU.png',
                members_user_ids=['76h35dg4-h76v-1875-987hn-h67gfv45Gt4']
            )

    def test_project_po_user_id_must_be_str(self):
        with pytest.raises(EntityError):
            Project(
                code='MF',
                name='test_project',
                description='test_description',
                po_user_id=1,
                scrum_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                start_date=1672585200000,
                photo='https://i.imgur.com/gHoRKJU.png',
                members_user_ids=['76h35dg4-h76v-1875-987hn-h67gfv45Gt4']
            )

    def test_project_po_user_id_must_be_36_characters(self):
        with pytest.raises(EntityError):
            Project(
                code='MF',
                name='test_project',
                description='test_description',
                po_user_id="51ah5jaj",
                scrum_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                start_date=1672585200000,
                photo='https://i.imgur.com/gHoRKJU.png',
                members_user_ids=['76h35dg4-h76v-1875-987hn-h67gfv45Gt4']
            )

    def test_project_scrum_user_id_must_be_str(self):
        with pytest.raises(EntityError):
            Project(
                code='MF',
                name='test_project',
                description='test_description',
                po_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                scrum_user_id=1,
                start_date=1672585200000,
                photo='https://i.imgur.com/gHoRKJU.png',
                members_user_ids=['76h35dg4-h76v-1875-987hn-h67gfv45Gt4']
            )
            
    def test_project_scrum_user_id_must_be_36_characters(self):
        with pytest.raises(EntityError):
            Project(
                code='MF',
                name='test_project',
                description='test_description',
                po_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                scrum_user_id="51ah5jaj",
                start_date=1672585200000,
                photo='https://i.imgur.com/gHoRKJU.png',
                members_user_ids=['76h35dg4-h76v-1875-987hn-h67gfv45Gt4']
            )
            
    def test_project_start_date_must_be_int(self):
        with pytest.raises(EntityError):
            Project(
                code='MF',
                name='test_project',
                description='test_description',
                po_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                scrum_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                start_date="1672585200000",
                photo='https://i.imgur.com/gHoRKJU.png',
                members_user_ids=['76h35dg4-h76v-1875-987hn-h67gfv45Gt4']
            )
            
    def test_project_start_date_must_be_greater_than_0(self):
        with pytest.raises(EntityError):
            Project(
                code='MF',
                name='test_project',
                description='test_description',
                po_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                scrum_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                start_date=-362,
                photo='https://i.imgur.com/gHoRKJU.png', 
                members_user_ids=['76h35dg4-h76v-1875-987hn-h67gfv45Gt4']
            )
            
    def test_project_start_date_must_be_smaller_than_now(self):
        now = int(datetime.now().timestamp() * 1000)
        with pytest.raises(EntityError):
            Project(
                code='MF',
                name='test_project',
                description='test_description',
                po_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                scrum_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                start_date=now + 3000,
                photo='https://i.imgur.com/gHoRKJU.png',
                members_user_ids=['76h35dg4-h76v-1875-987hn-h67gfv45Gt4']
            )
            
    def test_project_photos_can_be_none(self):
        project = Project(
            code='MF',
            name='test_project',
            description='test_description',
            po_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
            scrum_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
            start_date=1672585200000,
            members_user_ids=['93bc6ada-c0d1-7054-66ab-e17414c48ae3']
        )
        assert project.photo == None
        
    def test_project_membersuser_ids_must_be_list(self):
        with pytest.raises(EntityError):
            Project(
                code='MF',
                name='test_project',
                description='test_description',
                po_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                scrum_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                start_date=1672585200000,
                photo='https://i.imgur.com/gHoRKJU.png',
                members_user_ids='76h35dg4-h76v-1875-987hn-h67gfv45Gt4'
            )

    def test_project_members_less_than_one(self):
        with pytest.raises(EntityError):
            Project(
                code='MF',
                name='test_project',
                description='test_description',
                po_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                scrum_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                start_date=1672585200000,
                photo='https://i.imgur.com/gHoRKJU.png',
                members_user_ids=[]
            )

    def test_project_members_duplicated_member(self):
        project = Project(
            code='PQ',
            name='test_project',
            description='test_description',
            po_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
            scrum_user_id="51ah5jaj-c9jm-1345-666ab-e12341c14a3",
            start_date=1672585200000,
            photo='https://i.imgur.com/gHoRKJU.png',
            members_user_ids=['93bc6ada-c0d1-7054-66ab-e17414c48ae3', '93bc6ada-c0d1-7054-66ab-e17414c48ae3', "51ah5jaj-c9jm-1345-666ab-e12341c14a3"]
        )

        assert project.members_user_ids == ['51ah5jaj-c9jm-1345-666ab-e12341c14a3','93bc6ada-c0d1-7054-66ab-e17414c48ae3']

    def test_project_po_user_id_not_in_members_user_id(self):
        with pytest.raises(EntityError):
            Project(
                code='PQ',
                name='test_project',
                description='test_description',
                po_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                scrum_user_id="51ah5jaj-c9jm-1345-666ab-e12341c14a3",
                start_date=1672585200000,
                photo='https://i.imgur.com/gHoRKJU.png',
                members_user_ids=['76h35dg4-h76v-1875-987hn-h67gfv45Gt4']
            )

    def test_project_change_po_user_id(self):
        project = Project(
            code='PQ',
            name='test_project',
            description='test_description',
            po_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
            scrum_user_id="51ah5jaj-c9jm-1345-666ab-e12341c14a3",
            start_date=1672585200000,
            photo='https://i.imgur.com/gHoRKJU.png',
            members_user_ids=['93bc6ada-c0d1-7054-66ab-e17414c48ae3', "51ah5jaj-c9jm-1345-666ab-e12341c14a3"]
        )

        project.change_po_user_id('7gh5yf5H-857H-1234-75hng-94832hvng1s')

        assert project.po_user_id == '7gh5yf5H-857H-1234-75hng-94832hvng1s'
        assert project.members_user_ids == ['51ah5jaj-c9jm-1345-666ab-e12341c14a3','7gh5yf5H-857H-1234-75hng-94832hvng1s']

    def test_project_change_scrum_user_id(self):
        project = Project(
            code='PQ',
            name='test_project',
            description='test_description',
            po_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
            scrum_user_id="51ah5jaj-c9jm-1345-666ab-e12341c14a3",
            start_date=1672585200000,
            photo='https://i.imgur.com/gHoRKJU.png',
            members_user_ids=['93bc6ada-c0d1-7054-66ab-e17414c48ae3', "51ah5jaj-c9jm-1345-666ab-e12341c14a3"]
        )

        project.change_scrum_user_id('7gh5yf5H-857H-1234-75hng-94832hvng1s')

        assert project.scrum_user_id == '7gh5yf5H-857H-1234-75hng-94832hvng1s'
        assert project.members_user_ids == ['7gh5yf5H-857H-1234-75hng-94832hvng1s','93bc6ada-c0d1-7054-66ab-e17414c48ae3']

    def test_project_members_user_ids_must_be_list(self):
        with pytest.raises(EntityError):
            Project(
                code='MF',
                name='test_project',
                description='test_description',
                po_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                scrum_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                start_date=1672585200000,
                photo='https://i.imgur.com/gHoRKJU.png',
                members_user_ids='76h35dg4-h76v-1875-987hn-h67gfv45Gt4'
            )

    def test_project_members_user_ids_must_be_valid_user_ids(self):
        with pytest.raises(EntityError):
            Project(
                code='MF',
                name='test_project',
                description='test_description',
                po_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                scrum_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                start_date=1672585200000,
                photo='https://i.imgur.com/gHoRKJU.png',
                members_user_ids=['76']
            )