from abc import ABC, abstractmethod

from app.src.domain.models.user_model import UserModel


class IPersistencePortUser(ABC):

    @abstractmethod
    async def create(self, userModel: UserModel) -> UserModel:
        pass

    @abstractmethod
    async def getAll(self) -> list[UserModel]:
        pass

    @abstractmethod
    async def getById(self, id: str) -> UserModel:
        pass

    @abstractmethod
    async def getByEmail(self, email: str) -> UserModel:
        pass

    @abstractmethod
    async def updateById(self, id: str, userModel: UserModel) -> UserModel:
        pass

    @abstractmethod
    async def deleteById(self, id: str) -> str:
        pass