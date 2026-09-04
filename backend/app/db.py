from sqlalchemy import create_engine, text
from app.config import get_settings

engine = create_engine(get_settings().postgres_url, pool_pre_ping=True)

def database_is_ready() -> bool:
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return True
    except Exception:
        return False
