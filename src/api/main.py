from fastapi import FastAPI
from src.db.database import engine
from src.db.models.base import Base
from src.api.routes.auth import auth_router
from src.api.routes.query import query_router
from src.api.routes.history import query_history_router




app = FastAPI()


Base.metadata.create_all(engine)

app.include_router(auth_router , prefix='/api/v1')
app.include_router(query_router , prefix='/api/v1')
app.include_router(query_history_router , prefix='/api/v1')