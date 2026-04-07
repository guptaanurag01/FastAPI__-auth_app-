auth_app/
│
├── main.py
├── db.py
├── models.py
├── schemas.py
├── auth.py
├── routes/
│   └── auth_routes.py
├── utils/
│   ├── hashing.py
│   └── token.py
└── config.py




pip install fastapi uvicorn sqlalchemy psycopg2-binary passlib[bcrypt] python-jose