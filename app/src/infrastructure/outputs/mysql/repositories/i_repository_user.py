from abc import ABC, abstractmethod
from app.src.infrastructure.outputs.mysql.entities.entity_user import UserEntity

class IUserRepository(ABC):

    @abstractmethod
    async def create(self, userEntity: UserEntity) -> UserEntity:
        pass

    @abstractmethod
    async def getById(self, id: str) -> UserEntity:
        pass

    @abstractmethod
    async def getByEmail(self, email: str) -> UserEntity:
        pass

    @abstractmethod
    async def getAll(self, page: int, limit: int) -> list[UserEntity]:
        pass

    @abstractmethod
    async def updateById(self, userEntity: UserEntity, id: str) -> UserEntity:
        pass

    @abstractmethod
    async def deleteById(self, id: str) -> str:
        pass