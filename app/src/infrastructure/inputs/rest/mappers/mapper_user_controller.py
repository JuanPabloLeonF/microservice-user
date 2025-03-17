from app.src.application.dto.request_user import RequestUser
from app.src.infrastructure.inputs.rest.dto.request_user_controller import RequestUserController

class IMapperUserController:

    @staticmethod
    def mapperRequestUserControllerToRequestUser(request: RequestUserController) -> RequestUser:
        return RequestUser(
            name=request.name,
            email=request.email,
            password=request.password,
            roles=request.roles
        )

    @staticmethod
    def mapperRequestUserControllerListToRequestUserList(listRequestUserController: list[RequestUserController]) -> list[RequestUser]:
        return [IMapperUserController.mapperRequestUserControllerToRequestUser(request) for request in listRequestUserController]