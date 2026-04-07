from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import SessionLocal
import schemas
import auth

router = APIRouter(prefix="/auth", tags=["Auth"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    try:
        auth.register_user(db, user.email, user.password)
        return {"message": "User created"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/login", response_model=schemas.TokenResponse)
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    try:
        token = auth.login_user(db, user.email, user.password)
        return {"access_token": token}
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid credentials")
