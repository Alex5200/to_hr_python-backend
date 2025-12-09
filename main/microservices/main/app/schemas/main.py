from pydantic import BaseModel

class MainBase(BaseModel):
    name: str
    description: str

class MainCreate(MainBase):
    pass

class Main(MainBase):
    id: int

    class Config:
        from_attributes = True
