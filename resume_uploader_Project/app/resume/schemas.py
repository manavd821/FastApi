from app.db.config import Base
from datetime import  date
from typing import List, Union
from pydantic import BaseModel, EmailStr
import enum

class GenderEnum(str, enum.Enum):
    male = "male"
    female = "female"
    other = "other"
    
class ResumeCreate(BaseModel):
    name : str
    email : EmailStr
    dob : date
    state : str
    gender : GenderEnum
    preferred_locations : Union[str, List[str]]
    
class ResumeOut(ResumeCreate,BaseModel):
    id : int
    image_path : str
    resume_file_path : str
    model_config = {
        "from_attributes": True
    }