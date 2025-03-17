from app.src.application.dto.request_user import RequestUser
from app.src.application.dto.response_user import ResponseUser
from app.src.domain.models.user_model import UserModel
from app.src.domain.services.i_services_port_user import IServicesPortUser
from app.src.application.handlers.i_handler_user import IHandlerUser
from app.src.application.mappers.i_mapper_handler import IMapperHandler

class ImplementationHandlerUser(IHandlerUser):

    def __init__(self, iServicesPortUser: IServicesPortUser, iMapperHandler: IMapperHandler):
        self.iServicesPortUser: IServicesPortUser = iServicesPortUser
        self.iMapperHandler: IMapperHandler = iMapperHandler

    async def create(self, requestUser: RequestUser) -> ResponseUser:
        userModelResponse: UserModel = await self.iServicesPortUser.create(
            userModel=self.iMapperHandler.mapperRequestUserToUserModel(request=requestUser)
        )

        response: ResponseUser = self.iMapperHandler.mapperUserModelToResponseUser(
            userModel=userModelResponse
        )
        return response.getJSON()

    async def getByEmail(self, email: str) -> ResponseUser:
        userModelResponse: UserModel = await self.iServicesPortUser.getByEmail(email=email)
        response: ResponseUser = self.iMapperHandler.mapperUserModelToResponseUser(userModel=userModelResponse)
        return response.getJSON()

    async def getAll(self) -> list[ResponseUser]:
        listUsersModels: list[UserModel] = await self.iServicesPortUser.getAll()
        listResponseUsers: list[ResponseUser] = [self.iMapperHandler.mapperUserModelToResponseUser(userModel=userModel) for userModel in listUsersModels]
        response: list[ResponseUser] = [userModel.getJSON() for userModel in listResponseUsers]
        return response

    async def getById(self, id: str) -> ResponseUser:
        userModelResponse: UserModel = await self.iServicesPortUser.getById(id=id)
        response: ResponseUser = self.iMapperHandler.mapperUserModelToResponseUser(userModel=userModelResponse)
        return response.getJSON()

    async def updateById(self, id: str, requestUser: RequestUser) -> ResponseUser:
        userModelResponse: UserModel = await self.iServicesPortUser.updateById(
            id=id,
            userModel=self.iMapperHandler.mapperRequestUserToUserModel(request=requestUser)
        )
        response: ResponseUser = self.iMapperHandler.mapperUserModelToResponseUser(
            userModel=userModelResponse
        )
        return response.getJSON()

    async def deleteById(self, id: str) -> str:
        return await self.iServicesPortUser.deleteById(id=id)