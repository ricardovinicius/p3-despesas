from sqlmodel import Field, Relationship, SQLModel

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str 
    email: str = Field(unique=True)
    password: bytes
    
    transactions: list["Transaction"] = Relationship(back_populates="user") # type: ignore
    goals: list["Goal"] = Relationship(back_populates="user")