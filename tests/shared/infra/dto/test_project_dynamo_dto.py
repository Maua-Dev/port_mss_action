from src.shared.domain.entities.project import Project
from src.shared.infra.dto.project_dynamo_dto import ProjectDynamoDTO


class Test_ProjectDynamoDTO:

    def test_project_dynamo_dto_from_entity(self):
        project = Project(
            code="PT",
            name="Portfólio",
            description="É um site",
            po_RA="22011020",
            scrum_RA="21010757",
            start_date=1673535600000,
            photos=["https://i.imgur.com/gHoRKJU.png"],
            members=["10017310", "21010757", "22011020"],
            members_user_ids=["51ah5jaj-c9jm-1345-666ab-e12341c14a3","6f5g4h7J-876j-0098-123hb-hgb567fy4hb", "93bc6ada-c0d1-7054-66ab-e17414c48ae3" ]
        )

        project_dto = ProjectDynamoDTO.from_entity(project)
        assert project_dto.members_user_ids == ["51ah5jaj-c9jm-1345-666ab-e12341c14a3","6f5g4h7J-876j-0098-123hb-hgb567fy4hb", "93bc6ada-c0d1-7054-66ab-e17414c48ae3" ]
        assert project_dto == ProjectDynamoDTO(code="PT", name="Portfólio", description="É um site", po_RA="22011020", scrum_RA="21010757", start_date=1673535600000, photos=["https://i.imgur.com/gHoRKJU.png"], members=["10017310", "21010757", "22011020"], members_user_ids=["51ah5jaj-c9jm-1345-666ab-e12341c14a3","6f5g4h7J-876j-0098-123hb-hgb567fy4hb", "93bc6ada-c0d1-7054-66ab-e17414c48ae3" ])
        
    def test_project_dynamo_dto_to_dynamo(self):       
        project_dto = ProjectDynamoDTO(code="PT", name="Portfólio", description="É um site", po_RA="22011020", scrum_RA="21010757", start_date=1673535600000, photos=["https://i.imgur.com/gHoRKJU.png"], members=["10017310", "21010757", "22011020"], members_user_ids=["51ah5jaj-c9jm-1345-666ab-e12341c14a3","6f5g4h7J-876j-0098-123hb-hgb567fy4hb", "93bc6ada-c0d1-7054-66ab-e17414c48ae3" ])
        
        project_dynamo = project_dto.to_dynamo()
        
        assert project_dynamo == {"entity": "project", "code": "PT", "name": "Portfólio", "description": "É um site", "po_RA": "22011020", "scrum_RA": "21010757", "start_date": 1673535600000, "members": ["10017310", "21010757", "22011020"], "photos": ["https://i.imgur.com/gHoRKJU.png"], "members_user_ids": ["51ah5jaj-c9jm-1345-666ab-e12341c14a3","6f5g4h7J-876j-0098-123hb-hgb567fy4hb", "93bc6ada-c0d1-7054-66ab-e17414c48ae3" ]}

    def test_project_dynamo_dto_from_dynamo(self):      
        project_dynamo = {"entity": "project", "code": "PT", "name": "Portfólio", "description": "É um site", "po_RA": "22011020", "scrum_RA": "21010757", "start_date": 1673535600000, "members": ["10017310", "21010757", "22011020"], "photos": ["https://i.imgur.com/gHoRKJU.png"], "members_user_ids": ["51ah5jaj-c9jm-1345-666ab-e12341c14a3","6f5g4h7J-876j-0098-123hb-hgb567fy4hb", "93bc6ada-c0d1-7054-66ab-e17414c48ae3" ]}
        
        project_dto = ProjectDynamoDTO.from_dynamo(project_dynamo)
        
        assert project_dto == ProjectDynamoDTO(code="PT", name="Portfólio", description="É um site", po_RA="22011020", scrum_RA="21010757", start_date=1673535600000, photos=["https://i.imgur.com/gHoRKJU.png"], members=["10017310", "21010757", "22011020"], members_user_ids=["51ah5jaj-c9jm-1345-666ab-e12341c14a3","6f5g4h7J-876j-0098-123hb-hgb567fy4hb", "93bc6ada-c0d1-7054-66ab-e17414c48ae3" ])
        
    def test_project_dynamo_dto_to_entity(self):      
        project_dto = ProjectDynamoDTO(code="PT", name="Portfólio", description="É um site", po_RA="22011020", scrum_RA="21010757", start_date=1673535600000, photos=["https://i.imgur.com/gHoRKJU.png"], members=["10017310", "21010757", "22011020"], members_user_ids=["51ah5jaj-c9jm-1345-666ab-e12341c14a3","6f5g4h7J-876j-0098-123hb-hgb567fy4hb", "93bc6ada-c0d1-7054-66ab-e17414c48ae3" ])
        
        project = project_dto.to_entity()
        
        assert project == Project(
            code="PT",
            name="Portfólio",
            description="É um site",
            po_RA="22011020",
            scrum_RA="21010757",
            start_date=1673535600000,
            photos=["https://i.imgur.com/gHoRKJU.png"],
            members=["10017310", "21010757", "22011020"],
            members_user_ids=["51ah5jaj-c9jm-1345-666ab-e12341c14a3","6f5g4h7J-876j-0098-123hb-hgb567fy4hb", "93bc6ada-c0d1-7054-66ab-e17414c48ae3" ]
        )
        
    def test_project_dynamo_dto_from_entity_to_dynamo(self):
        project = Project(
            code="PT",
            name="Portfólio",
            description="É um site",
            po_RA="22011020",
            scrum_RA="21010757",
            start_date=1673535600000,
            photos=["https://i.imgur.com/gHoRKJU.png"],
            members=["10017310", "21010757", "22011020"],
            members_user_ids=["51ah5jaj-c9jm-1345-666ab-e12341c14a3","6f5g4h7J-876j-0098-123hb-hgb567fy4hb", "93bc6ada-c0d1-7054-66ab-e17414c48ae3" ]
        )
        
        project_dto = ProjectDynamoDTO.from_entity(project)
        project_dynamo = project_dto.to_dynamo()
        
        assert project_dynamo == {"entity": "project", "code": "PT", "name": "Portfólio", "description": "É um site", "po_RA": "22011020", "scrum_RA": "21010757", "start_date": 1673535600000, "members": ["10017310", "21010757", "22011020"], "photos": ["https://i.imgur.com/gHoRKJU.png"], "members_user_ids": ["51ah5jaj-c9jm-1345-666ab-e12341c14a3","6f5g4h7J-876j-0098-123hb-hgb567fy4hb", "93bc6ada-c0d1-7054-66ab-e17414c48ae3" ]}
        
    def test_project_dynamo_dto_from_dynamo_to_entity(self):
        project_dynamo = {"entity": "project", "code": "PT", "name": "Portfólio", "description": "É um site", "po_RA": "22011020", "scrum_RA": "21010757", "start_date": 1673535600000, "members": ["10017310", "21010757", "22011020"], "photos": ["https://i.imgur.com/gHoRKJU.png"], "members_user_ids": ["51ah5jaj-c9jm-1345-666ab-e12341c14a3","6f5g4h7J-876j-0098-123hb-hgb567fy4hb", "93bc6ada-c0d1-7054-66ab-e17414c48ae3" ]}
        
        project_dto = ProjectDynamoDTO.from_dynamo(project_dynamo)
        project = project_dto.to_entity()
        
        assert project == Project(
            code="PT",
            name="Portfólio",
            description="É um site",
            po_RA="22011020",
            scrum_RA="21010757",
            start_date=1673535600000,
            photos=["https://i.imgur.com/gHoRKJU.png"],
            members=["10017310", "21010757", "22011020"],
            members_user_ids=["51ah5jaj-c9jm-1345-666ab-e12341c14a3","6f5g4h7J-876j-0098-123hb-hgb567fy4hb", "93bc6ada-c0d1-7054-66ab-e17414c48ae3" ]
        )