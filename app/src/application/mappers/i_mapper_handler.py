from app.src.domain.models.user_model import UserModel
from app.src.application.dto.response_user import ResponseUser
from app.src.application.dto.request_user import RequestUser

class IMapperHandler:

    @staticmethod
    def mapperRequestUserToUserModel(request: RequestUser) -> UserModel:
        return UserModel(
            id="",
            name=request.name,
            email=request.email,
            password=request.password,
            roles=request.roles
        )

    @staticmethod
    def mapperUserModelToResponseUser(userModel: UserModel) -> ResponseUser:
        return ResponseUser(
            id=userModel.getId(),
            name=userModel.getName(),
            email=userModel.getEmail(),
            password=userModel.getPassword(),
            roles=userModel.getRoles()
        )

    @staticmethod
    def mapperListUserModelToListResponseUser(listUserModel: list[UserModel]) -> list[ResponseUser]:
        return [IMapperHandler.mapperUserModelToResponseUser(userModel=userModel) for userModel in listUserModel]