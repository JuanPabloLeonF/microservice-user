from abc import ABC, abstractmethod

from app.src.application.dto.request_user import RequestUser
from app.src.application.dto.response_user import ResponseUser

class IHandlerUser(ABC):

    @abstractmethod
    async def create(self, requestUser: RequestUser) -> ResponseUser:
        pass

    @abstractmethod
    async def getAll(self, page: int, limit: int) -> list[ResponseUser]:
        pass

    @abstractmethod
    async def getById(self, id: str) -> ResponseUser:
        pass

    @abstractmethod
    async def getByEmail(self, email: str) -> ResponseUser:
        pass

    @abstractmethod
    async def updateById(self, id: str, requestUser: RequestUser) -> ResponseUser:
        pass

    @abstractmethod
    async def deleteById(self, id: str) -> str:
        pass