import injector
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from app.src.application.dto.request_user import RequestUser
from app.src.infrastructure.inputs.rest.dto.request_user_controller import RequestUserController
from app.src.application.dto.response_user import ResponseUser
from app.src.application.handlers.i_handler_user import IHandlerUser
from app.configuration.module_injector_user import ModuleInjectorUser
from app.src.infrastructure.inputs.rest.mappers.mapper_user_controller import IMapperUserController

routerUser: APIRouter = APIRouter(prefix="/user")
iHandlerUser: IHandlerUser = injector.Injector([ModuleInjectorUser]).get(IHandlerUser)
iMapperUserController: IMapperUserController = IMapperUserController()

class ControllerUser:

    @staticmethod
    @routerUser.post(path="/create", status_code=201)
    async def create(request: RequestUserController) -> JSONResponse:
        requestUser: RequestUser = iMapperUserController.mapperRequestUserControllerToRequestUser(request)
        response: ResponseUser = await iHandlerUser.create(requestUser=requestUser)
        return JSONResponse(content=response, status_code=status.HTTP_201_CREATED)

    @staticmethod
    @routerUser.get(path="/all", status_code=200)
    async def getAll() -> JSONResponse:
        response: list[ResponseUser] = await iHandlerUser.getAll()
        return JSONResponse(content=response, status_code=status.HTTP_200_OK)

    @staticmethod
    @routerUser.get(path="/getById/{id}", status_code=200)
    async def getById(id: str) -> JSONResponse:
        response: ResponseUser = await iHandlerUser.getById(id)
        return JSONResponse(content=response, status_code=status.HTTP_200_OK)

    @staticmethod
    @routerUser.get(path="/getByEmail/{email}", status_code=200)
    async def getByEmail(email: str) -> JSONResponse:
        response: ResponseUser = await iHandlerUser.getByEmail(email)
        return JSONResponse(content=response, status_code=status.HTTP_200_OK)

    @staticmethod
    @routerUser.put(path="/update/{id}", status_code=200)
    async def update(id: str, request: RequestUserController) -> JSONResponse:
        requestUser: RequestUser = iMapperUserController.mapperRequestUserControllerToRequestUser(request=request)
        response: ResponseUser = await iHandlerUser.updateById(id=id, requestUser=requestUser)
        return JSONResponse(content=response, status_code=status.HTTP_200_OK)

    @staticmethod
    @routerUser.delete(path="/delete/{id}", status_code=200)
    async def delete(id: str) -> JSONResponse:
        response: str = await iHandlerUser.deleteById(id)
        return JSONResponse(content=response, status_code=status.HTTP_200_OK)