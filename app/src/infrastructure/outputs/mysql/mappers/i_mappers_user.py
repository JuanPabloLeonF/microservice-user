from app.src.domain.models.user_model import UserModel
from app.src.infrastructure.outputs.mysql.entities.entity_user import UserEntity

class IMapperUser:

    @staticmethod
    def mapperUserEntityToUserModel(userEntity: UserEntity) -> UserModel:
        return UserModel(
            id=userEntity.getId(),
            name=userEntity.getName(),
            email=userEntity.getEmail(),
            roles=userEntity.getRoles(),
            password=userEntity.getPassword()
        )

    @staticmethod
    def mapperUserModelToUserEntity(userModel: UserModel) -> UserEntity:
        return UserEntity(
            name=userModel.getName(),
            email=userModel.getEmail(),
            password=userModel.getPassword(),
            roles=userModel.getRoles()
        )

    @staticmethod
    def mapperListUserModelToListUserEntity(userModelList: list[UserModel]) -> list[UserEntity]:
        return [IMapperUser.mapperUserModelToUserEntity(userModel) for userModel in userModelList]

    @staticmethod
    def mapperListUserEntityToListUserModel(userEntityList: list[UserEntity]) -> list[UserModel]:
        return [IMapperUser.mapperUserEntityToUserModel(userEntity) for userEntity in userEntityList]