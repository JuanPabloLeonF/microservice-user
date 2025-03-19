from app.src.domain.models.user_model import UserModel
from app.src.domain.persistence.i_persistence_port_user import IPersistencePortUser
from app.src.infrastructure.outputs.mysql.entities.entity_user import UserEntity
from app.src.infrastructure.outputs.mysql.repositories.i_repository_user import IUserRepository
from app.src.infrastructure.outputs.mysql.mappers.i_mappers_user import IMapperUser

class AdapterUser(IPersistencePortUser):

    def __init__(self, iUserRepository: IUserRepository, iMapperUser: IMapperUser):
        self.iUserRepository: IUserRepository = iUserRepository
        self.iMapperUser: IMapperUser = iMapperUser

    async def create(self, userModel: UserModel) -> UserModel:
        userEntity: UserEntity = self.iMapperUser.mapperUserModelToUserEntity(userModel=userModel)
        userEntitySave: UserEntity = await self.iUserRepository.create(userEntity=userEntity)
        return self.iMapperUser.mapperUserEntityToUserModel(userEntity=userEntitySave)

    async def getAll(self, page: int, limit: int) -> list[UserModel]:
        listUserEntity: list[UserEntity] = await self.iUserRepository.getAll(page=page, limit=limit)
        return self.iMapperUser.mapperListUserEntityToListUserModel(
            userEntityList=listUserEntity
        )

    async def getById(self, id: str) -> UserModel:
        userEntityFound: UserEntity = await self.iUserRepository.getById(id=id)
        return self.iMapperUser.mapperUserEntityToUserModel(userEntity=userEntityFound)

    async def getByEmail(self, email: str) -> UserModel:
        userEntityFound: UserEntity = await self.iUserRepository.getByEmail(email=email)
        return self.iMapperUser.mapperUserEntityToUserModel(userEntity=userEntityFound)

    async def updateById(self, id: str, userModel: UserModel) -> UserModel:
        userEntityMapper: UserEntity = self.iMapperUser.mapperUserModelToUserEntity(userModel=userModel)
        userEntityUpdate: UserEntity = await self.iUserRepository.updateById(id=id, userEntity=userEntityMapper)
        return self.iMapperUser.mapperUserEntityToUserModel(userEntity=userEntityUpdate)

    async def deleteById(self, id: str) -> str:
        return await self.iUserRepository.deleteById(id=id)