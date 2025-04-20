from sqlalchemy import Column, Integer, String, Text
from database import Base

class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    comment = Column(Text, nullable=True)