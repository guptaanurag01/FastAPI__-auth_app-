from fastapi import FastAPI
from db import Base, engine
from routes.auth_routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.on_event("startup")
def startup():
    try:
        with engine.connect() as conn:
            print("Database connected ✅")
    except Exception as e:
        print("Database connection failed ❌")
        raise e


app.include_router(router)
