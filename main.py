from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import Contact
from schemas import ContactCreate

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/contacts/")
def create_contact(contact: ContactCreate, db: Session = Depends(get_db)):
    db_contact = Contact(**contact.dict())
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact


@app.get("/contacts/")
def read_contacts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    contacts = db.query(Contact).offset(skip).limit(limit).all()
    return contacts


@app.get("/contacts/search/")
def search_contacts(query: str, db: Session = Depends(get_db)):
    contacts = db.query(Contact).filter(
        (Contact.full_name.ilike(f"%{query}%")) |
        (Contact.phone_number.ilike(f"%{query}%")) |
        (Contact.comment.ilike(f"%{query}%"))
    ).all()

    if not contacts:
        raise HTTPException(status_code=404, detail="Contacts not found")

    return contacts