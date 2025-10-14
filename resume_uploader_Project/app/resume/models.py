from app.db.config import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String, Text
from datetime import datetime, timedelta, timezone, date
from app.resume.schemas import GenderEnum
import enum

# class GenderEnum(str, enum.Enum):
#     male = "male"
#     female = "female"
#     other = "other"
    
class Resume(Base):
    __tablename__ = "resumes"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(255))
    email: Mapped[str] = mapped_column(String(255), unique=True)
    dob: Mapped[date]
    state: Mapped[str] = mapped_column(String(200))
    gender: Mapped[GenderEnum]
    preferred_locations: Mapped[str] = mapped_column(Text)
    image_path: Mapped[str] = mapped_column(String(255))
    resume_file_path: Mapped[str] = mapped_column(String(255))