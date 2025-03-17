class RequestUser:

    def __init__(self, name: str, email: str, password: str, roles: list[str]):
        self.name: str = name
        self.email: str = email
        self.password: str = password
        self.roles: list[str] = roles

    def getJSON(self):
        return {
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "roles": self.roles
        }