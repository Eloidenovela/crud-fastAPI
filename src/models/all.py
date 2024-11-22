from sqlalchemy import create_engine
from configurations.settings import Settings

engine = create_engine(Settings().DATABASE_URL)