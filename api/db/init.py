from db.models import Base
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()
engine = create_engine(os.environ.get('DB_CONNECTION_STRING'))
Base.metadata.create_all(engine)