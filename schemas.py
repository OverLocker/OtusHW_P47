from pydantic import BaseModel

class ContactBase(BaseModel):
    full_name: str
    phone_number: str
    comment: str = None

class ContactCreate(ContactBase):
    pass

class Contact(ContactBase):
    id: int

    class Config:
        orm_mode = True