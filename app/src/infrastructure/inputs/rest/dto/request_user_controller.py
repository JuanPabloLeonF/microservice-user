from pydantic import BaseModel, Field, field_validator, conlist, EmailStr

class RequestUserController(BaseModel):

    name: str = Field(min_length=2, max_length=50)
    email: EmailStr = Field(min_length=2, max_length=50)
    password: str = Field(min_length=2, max_length=50)
    roles: conlist(str, min_length=1, max_length=2)

    @field_validator("roles")
    def validateFieldRoles(cls, value: list[str]) -> list[str]:
        allowedRoles: set[str] = {"admin", "user"}
        if not all(role in allowedRoles for role in value):
            raise ValueError("Lo siento, los roles solo se le pueden asignar admin o user")
        return value