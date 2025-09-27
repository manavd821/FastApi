from sqlalchemy import Table, Column, Integer, String, MetaData, UniqueConstraint, DateTime, Boolean, ForeignKey,text
from datetime import datetime, timezone
from app.db.metadata import metadata

users = Table(
    "user",
    metadata,
    Column("user_id", Integer, primary_key=True),
    Column("email", String, unique=True, nullable=False),
    Column("name", String, nullable=False),
    Column("is_active", Boolean, server_default=text("TRUE")),
    Column("is_admin", Boolean, server_default=text("FALSE")),
    Column("hashed_password", String, nullable=False),
    Column("is_verified", Boolean, server_default=text("FALSE")),
    Column("created_at", DateTime(timezone=True), server_default=text("CURRENT_TIMESTAMP")),
    Column("updated_at", DateTime(timezone=True), server_default=text("CURRENT_TIMESTAMP"), onupdate=text("CURRENT_TIMESTAMP")),
)

refresh_tokens = Table(
    "refresh_token",
    metadata,
    Column("refresh_token_id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("user.user_id")),
    Column("token", String, nullable=False),
    Column("created_at", DateTime(timezone=True), server_default=text("CURRENT_TIMESTAMP")),
    Column("expires_at", DateTime(timezone=True), nullable=False),
    Column("revoked", Boolean, server_default=text("FALSE")),
)