from pydantic import BaseModel

class MainlogingBase(BaseModel):
    name: str
    description: str

class MainlogingCreate(MainlogingBase):
    pass

class Mainloging(MainlogingBase):
    id: int

    class Config:
        from_attributes = True
