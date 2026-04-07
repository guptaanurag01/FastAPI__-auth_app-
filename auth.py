from sqlalchemy.orm import Session
from models import User
from utils.hashing import hash_password, verify_password
from utils.token import create_access_token

def register_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()
    if user:
        raise Exception("User already exists")

    new_user = User(email=email, password=hash_password(password))

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def authenticate_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(password, user.password):
        return None
    return user


def login_user(db: Session, email: str, password: str):
    user = authenticate_user(db, email, password)
    print("==================",db, email, password)

    if not user:
        raise Exception("Invalid credentials")

    token = create_access_token({"sub": user.email})
    return token
