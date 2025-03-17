import uuid
from sqlalchemy import Column, String, JSON
from app.src.infrastructure.outputs.mysql.settings.database_config import DatabaseConfiguration

class UserEntity(DatabaseConfiguration.BaseModels):

    __tablename__ = "user"

    id = Column(String(50), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    roles = Column(JSON, nullable=False)

    def __init__(self, name: str, email: str, password: str, roles: list[str]):
        self.name: str = name
        self.email: str = email
        self.password: str = password
        self.roles: list[str] = roles

    def getId(self) -> str:
        return self.id

    def setId(self, id: str) -> None:
        self.id = id

    def getName(self) -> str:
        return self.name

    def setName(self, name: str) -> None:
        self.name = name

    def getEmail(self) -> str:
        return self.email

    def setEmail(self, email: str) -> None:
        self.email = email

    def getPassword(self) -> str:
        return self.password

    def setPassword(self, password: str) -> None:
        self.password = password

    def getRoles(self) -> list[str]:
        return self.roles

    def setRoles(self, roles: list[str]) -> None:
        self.roles = roles

    def getJSON(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "roles": self.roles
        }