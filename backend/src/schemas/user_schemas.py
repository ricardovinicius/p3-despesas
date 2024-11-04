from pydantic import BaseModel


class UserLoginSchema(BaseModel):
    email_address: str
    password: str