import uuid
from sqlmodel import Field, SQLModel


class Base(SQLModel):
    # id: BigInteger | None = Field(sa_type=BigInteger, default=None, primary_key=True, index=True)
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

