class UserModel:

    def __init__(self, id: str, name: str, email: str, password: str, roles: list[str]):
        self.__id: str = id
        self.__name: str = name
        self.__email: str = email
        self.__password: str = password
        self.__roles: list[str] = roles


    def getId(self) -> str:
        return self.__id

    def setId(self, id: str) -> None:
        self.__id = id

    def getName(self) -> str:
        return self.__name

    def setName(self, name: str) -> None:
        self.__name = name

    def getEmail(self) -> str:
        return self.__email

    def setEmail(self, email: str) -> None:
        self.__email = email

    def getPassword(self) -> str:
        return self.__password

    def setPassword(self, password: str) -> None:
        self.__password = password

    def getRoles(self) -> list[str]:
        return self.__roles

    def setRoles(self, roles: list[str]) -> None:
        self.__roles = roles

    def getJSON(self):
        return {
            "id": self.__id,
            "name": self.__name,
            "email": self.__email,
            "password": self.__password,
            "roles": self.__roles
        }