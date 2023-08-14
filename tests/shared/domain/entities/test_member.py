import pytest
from src.shared.domain.entities.member import Member
from src.shared.domain.entities.project import Project
from src.shared.domain.enums.active_enum import ACTIVE
from src.shared.domain.enums.course_enum import COURSE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.enums.stack_enum import STACK
from src.shared.helpers.errors.domain_errors import EntityError


class Test_Member:
    
    def test_member(self):
        member = Member(
            name="Vitor Guirão MPNTM",
            email_dev="vsoller.devmaua@gmail.com",
            email="vsoller@airubio.com",
            ra="21017310",
            role=ROLE.DIRECTOR,
            stack=STACK.INFRA,
            year=1,
            cellphone="11991758098",
            course=COURSE.ECA,
            hired_date=1614567601000,
            active=ACTIVE.FREEZE
        )
        
        assert member.name == "Vitor Guirão MPNTM"
        assert member.email_dev == "vsoller.devmaua@gmail.com"
        assert member.email == "vsoller@airubio.com"
        assert member.ra == "21017310"
        assert member.role == ROLE.DIRECTOR
        assert member.stack == STACK.INFRA
        assert member.year == 1
        assert member.cellphone == "11991758098"
        assert member.course == COURSE.ECA
        assert member.hired_date == 1614567601000
        assert member.active == ACTIVE.FREEZE

            
    def test_member_name_not_str(self): 
        with pytest.raises(EntityError):
            Member(
            name=1,
            email_dev="vsoller.devmaua@gmail.com",
            email="vsoller@airubio.com",
            ra="21017310",
            role=ROLE.DIRECTOR,
            stack=STACK.INFRA,
            year=1,
            cellphone="11991758098",
            course=COURSE.ECA,
            hired_date=1671728165,
            active=ACTIVE.FREEZE
        )
            
    def test_member_name_smaller_than_minimum(self): 
        with pytest.raises(EntityError):
            Member(
            name="V",
            email_dev="vsoller.devmaua@gmail.com",
            email="vsoller@airubio.com",
            ra="21017310",
            role=ROLE.DIRECTOR,
            stack=STACK.INFRA,
            year=1,
            cellphone="11991758098",
            course=COURSE.ECA,
            hired_date=1671728165,
            active=ACTIVE.FREEZE
        )

    def test_member_ra_not_str(self): 
        with pytest.raises(EntityError):
            Member(
            name="Vitor Guirão MPNTM",
            email_dev="vsoller.devmaua@gmail.com",
            email="vsoller@airubio.com",
            ra=21017310,
            role=ROLE.DIRECTOR,
            stack=STACK.INFRA,
            year=1,
            cellphone="11991758098",
            course=COURSE.ECA,
            hired_date=1671728165,
            active=ACTIVE.FREEZE
        )

    def test_member_ra_not_decimal(self): 
        with pytest.raises(EntityError):
            Member(
            name="Vitor Guirão MPNTM",
            email_dev="vsoller.devmaua@gmail.com",
            email="vsoller@airubio.com",
            ra="210173A0",
            role=ROLE.DIRECTOR,
            stack=STACK.INFRA,
            year=1,
            cellphone="11991758098",
            course=COURSE.ECA,
            hired_date=1671728165,
            active=ACTIVE.FREEZE
        )

    def test_member_lenght_ra_not_8(self): 
        with pytest.raises(EntityError):
            Member(
            name="Vitor Guirão MPNTM",
            email_dev="vsoller.devmaua@gmail.com",
            email="vsoller@airubio.com",
            ra="221017310",
            role=ROLE.DIRECTOR,
            stack=STACK.INFRA,
            year=1,
            cellphone="11991758098",
            course=COURSE.ECA,
            hired_date=1671728165,
            active=ACTIVE.FREEZE
        )


    def test_member_email_dev_is_not_str(self): 
        with pytest.raises(EntityError):
            Member(
            name="Vitor Guirão MPNTM",
            email_dev=1,
            email="vsoller@airubio.com",
            ra="21017310",
            role=ROLE.DIRECTOR,
            stack=STACK.INFRA,
            year=1,
            cellphone="11991758098",
            course=COURSE.ECA,
            hired_date=1671728165,
            active=ACTIVE.FREEZE
        )
            
    def test_member_email_dev_is_not_in_right_format(self): 
        with pytest.raises(EntityError):
            Member(
            name="Vitor Guirão MPNTM",
            email_dev="vsollerdevmaua@gmail.com",
            email="vsoller@airubio.com",
            ra="21017310",
            role=ROLE.DIRECTOR,
            stack=STACK.INFRA,
            year=1,
            cellphone="11991758098",
            course=COURSE.ECA,
            hired_date=1671728165,
            active=ACTIVE.FREEZE
        )
            
    
    def test_member_email_dev_not_dev(self): 
        with pytest.raises(EntityError):
            Member(
            name="Vitor Guirão MPNTM",
            email_dev="vitor.guirao@gmail.com",
            email="vsoller@airubio.com",
            ra="21017310",
            role=ROLE.DIRECTOR,
            stack=STACK.INFRA,
            year=1,
            cellphone="11991758098",
            course=COURSE.ECA,
            hired_date=1671728165,
            active=ACTIVE.FREEZE
        )

    def test_member_email_is_not_str(self):
        with pytest.raises(EntityError):
            Member(
            name="Vitor Guirão MPNTM",
            email_dev="vsoller.devmaua@gmail.com",
            email=1,
            ra="21017310",
            role=ROLE.DIRECTOR,
            stack=STACK.INFRA,
            year=1,
            cellphone="11991758098",
            course="COURSE.ECA",
            hired_date=1671728165,
            active=ACTIVE.FREEZE
            )

    def test_member_email_is_not_in_right_format(self):
        with pytest.raises(EntityError):
            Member(
            name="Vitor Guirão MPNTM",
            email_dev="vsoller.devmaua@gmail.com",
            email="vsollerairubio.com",
            ra="21017310",
            role=ROLE.DIRECTOR,
            stack=STACK.INFRA,
            year=1,
            cellphone="11991758098",
            course="COURSE.ECA",
            hired_date=1671728165,
            active=ACTIVE.FREEZE
            )    

    def test_member_email_is_the_same_as_email_dev(self):
        with pytest.raises(EntityError):
            Member(
            name="Vitor Guirão MPNTM",
            email_dev="vsoller.devmaua@gmail.com",
            email="vsoller.devmaua@gmail.com",
            ra="21017310",
            role=ROLE.DIRECTOR,
            stack=STACK.INFRA,
            year=1,
            cellphone="11991758098",
            course="COURSE.ECA",
            hired_date=1671728165,
            active=ACTIVE.FREEZE
            )
    
    def test_member_role_not_enum(self): 
        with pytest.raises(EntityError):
            Member(
            name="Vitor Guirão MPNTM",
            email_dev="vsoller.devmaua@gmail.com",
            email="vsoller@airubio.com",
            ra="21017310",
            role="ROLE.DIRECTOR",
            stack=STACK.INFRA,
            year=1,
            cellphone="11991758098",
            course=COURSE.ECA,
            hired_date=1671728165,
            active=ACTIVE.FREEZE
        )

    def test_member_stack_not_enum(self): 
        with pytest.raises(EntityError):
            Member(
            name="Vitor Guirão MPNTM",
            email_dev="vsoller.devmaua@gmail.com",
            email="vsoller@airubio.com",
            ra="21017310",
            role=ROLE.DIRECTOR,
            stack="STACK.INFRA",
            year=1,
            cellphone="11991758098",
            course=COURSE.ECA,
            hired_date=1671728165,
            active=ACTIVE.FREEZE
        )

    def test_member_year_not_int(self): 
        with pytest.raises(EntityError):
            Member(
            name="Vitor Guirão MPNTM",
            email_dev="vsoller.devmaua@gmail.com",
            email="vsoller@airubio.com",
            ra="21017310",
            role=ROLE.DIRECTOR,
            stack=STACK.INFRA,
            year="2021",
            cellphone="11991758098",
            course=COURSE.ECA,
            hired_date=1671728165,
            active=ACTIVE.FREEZE
        )
            
    def test_member_year_bigger_than_6(self): 
        with pytest.raises(EntityError):
            Member(
            name="Vitor Guirão MPNTM",
            email_dev="vsoller.devmaua@gmail.com",
            email="vsoller@airubio.com",
            ra="21017310",
            role=ROLE.DIRECTOR,
            stack=STACK.INFRA,
            year=10,
            cellphone="11991758098",
            course=COURSE.ECA,
            hired_date=1671728165,
            active=ACTIVE.FREEZE
        )
            
    def test_member_year_smaller_than_0(self): 
        with pytest.raises(EntityError):
            Member(
            name="Vitor Guirão MPNTM",
            email_dev="vsoller.devmaua@gmail.com",
            email="vsoller@airubio.com",
            ra="21017310",
            role=ROLE.DIRECTOR,
            stack=STACK.INFRA,
            year=-2,
            cellphone="11991758098",
            course=COURSE.ECA,
            hired_date=1671728165,
            active=ACTIVE.FREEZE
        )

    def test_member_cellphone_not_str(self): 
        with pytest.raises(EntityError):
            Member(
            name="Vitor Guirão MPNTM",
            email_dev="vsoller.devmaua@gmail.com",
            email="vsoller@airubio.com",
            ra="21017310",
            role=ROLE.DIRECTOR,
            stack=STACK.INFRA,
            year=1,
            cellphone=11991758098,
            course=COURSE.ECA,
            hired_date=1671728165,
            active=ACTIVE.FREEZE
        )

    def test_member_cellphone_not_in_right_format(self): 
        with pytest.raises(EntityError):
            Member(
            name="Vitor Guirão MPNTM",
            email_dev="vsoller.devmaua@gmail.com",
            email="vsoller@airubio.com",
            ra="21017310",
            role=ROLE.DIRECTOR,
            stack=STACK.INFRA,
            year=1,
            cellphone="551991758098",
            course=COURSE.ECA,
            hired_date=1671728165,
            active=ACTIVE.FREEZE
        )


    def test_member_course_not_enum(self): 
        with pytest.raises(EntityError):
            Member(
            name="Vitor Guirão MPNTM",
            email_dev="vsoller.devmaua@gmail.com",
            email="vsoller@airubio.com",
            ra="21017310",
            role=ROLE.DIRECTOR,
            stack=STACK.INFRA,
            year=1,
            cellphone="11991758098",
            course="COURSE.ECA",
            hired_date=1671728165,
            active=ACTIVE.FREEZE
        )


    def test_member_hired_date_not_int(self): 
        with pytest.raises(EntityError):
            Member(
            name="Vitor Guirão MPNTM",
            email_dev="vsoller.devmaua@gmail.com",
            email="vsoller@airubio.com",
            ra="21017310",
            role=ROLE.DIRECTOR,
            stack=STACK.INFRA,
            year=1,
            cellphone="11991758098",
            course=COURSE.ECA,
            hired_date="10/10/2002",
            active=ACTIVE.FREEZE
        )
            
    def test_member_hired_date_less_than_zero(self): 
        with pytest.raises(EntityError):
            Member(
            name="Vitor Guirão MPNTM",
            email_dev="vsoller.devmaua@gmail.com",
            email="vsoller@airubio.com",
            ra="21017310",
            role=ROLE.DIRECTOR,
            stack=STACK.INFRA,
            year=1,
            cellphone="11991758098",
            course=COURSE.ECA,
            hired_date=-1671728165,
            active=ACTIVE.FREEZE
        )
            
    def test_member_active_not_enum(self): 
        with pytest.raises(EntityError):
            Member(
            name="Vitor Guirão MPNTM",
            email_dev="vsoller.devmaua@gmail.com",
            email="vsoller@airubio.com",
            ra="21017310",
            role=ROLE.DIRECTOR,
            stack=STACK.INFRA,
            year=1,
            cellphone="11991758098",
            course=COURSE.ECA,
            hired_date=1671728165,
            active="ACTIVE.FREEZE"
        )
            
    def test_member_active_with_deactivated_date(self): 
        with pytest.raises(EntityError):
            Member(
            name="Vitor Guirão MPNTM",
            email_dev="vsoller.devmaua@gmail.com",
            email="vsoller@airubio.com",
            ra="21017310",
            role=ROLE.DIRECTOR,
            stack=STACK.INFRA,
            year=1,
            cellphone="11991758098",
            course=COURSE.ECA,
            hired_date=1671728165,
            deactivated_date=1671728165,
            active=ACTIVE.ACTIVE
        )
                 
    def test_member_deactivated_date_smaller_than_hired_date(self): 
        with pytest.raises(EntityError):
            Member(
                name="Vitor Guirão MPNTM",
                email_dev="vsoller.devmaua@gmail.com",
                email="vsoller@airubio.com",
                ra="21017310",
                role=ROLE.DIRECTOR,
                stack=STACK.INFRA,
                year=1,
                cellphone="11991758098",
                course=COURSE.ECA,
                hired_date=1671728165,
                active=ACTIVE.DISCONNECTED,
                deactivated_date=1640192165
            )          