class ResponseUser:

    def __init__(self, id: str, name: str, email: str, password: str, roles: list[str]):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.roles = roles

    def getJSON(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "roles": self.roles
        }