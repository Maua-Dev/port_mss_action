from .portfolio_export_projects_usecase import PortfolioExportProjectsUsecase
from .portfolio_export_projects_viewmodel import PortfolioExportProjectsViewModel
from src.shared.helpers.external_interfaces.external_interface import IRequest
from src.shared.helpers.external_interfaces.http_codes import OK, InternalServerError


class PortfolioExportProjectsController:
    def __init__(self, usecase: PortfolioExportProjectsUsecase):
        self.usecase = usecase

    def __call__(self, request: IRequest):
        try:
            projects = self.usecase()

            viewmodel = PortfolioExportProjectsViewModel(projects=projects)

            print("All projects retrieved and formatted successfully")

            return OK(viewmodel.to_dict())

        except Exception as err:
            print(f"Unexpected error: {str(err)}")
            return InternalServerError(body=err.args[0])
