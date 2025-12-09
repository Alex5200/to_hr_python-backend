from pydantic import BaseModel

class AdmindataBase(BaseModel):
    name: str
    description: str

class AdmindataCreate(AdmindataBase):
    pass

class Admindata(AdmindataBase):
    id: int

    class Config:
        from_attributes = True
