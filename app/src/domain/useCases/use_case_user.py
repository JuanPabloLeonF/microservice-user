from app.src.domain.models.user_model import UserModel
from app.src.domain.services.i_services_port_user import IServicesPortUser
from app.src.domain.persistence.i_persistence_port_user import IPersistencePortUser
from app.src.domain.utils.util_bcrypt import UtilsBcrypt

class UseCaseUser(IServicesPortUser):

    def __init__(self, iPersistencePortUser: IPersistencePortUser):
        self.iPersistencePortUser: IPersistencePortUser = iPersistencePortUser

    async def create(self, userModel: UserModel) -> UserModel:
        hast: str = UtilsBcrypt.hashPassword(password=userModel.getPassword())
        userModel.setPassword(password=hast)
        return await self.iPersistencePortUser.create(userModel=userModel)

    async def getAll(self, page: int, limit: int) -> list[UserModel]:
        return await self.iPersistencePortUser.getAll(page=page, limit=limit)

    async def getById(self, id: str) -> UserModel:
        return await self.iPersistencePortUser.getById(id)

    async def getByEmail(self, email: str) -> UserModel:
        return await self.iPersistencePortUser.getByEmail(email)

    async def updateById(self, id: str, userModel: UserModel) -> UserModel:
        hast: str = UtilsBcrypt.hashPassword(password=userModel.getPassword())
        userModel.setPassword(password=hast)
        return await self.iPersistencePortUser.updateById(id, userModel)

    async def deleteById(self, id: str) -> str:
        return await self.iPersistencePortUser.deleteById(id)