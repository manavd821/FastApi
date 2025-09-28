from sqlalchemy import MetaData

metadata = MetaData()

# Import all table modules so their tables are registered with this metadata
from app.account import tables as account_tables