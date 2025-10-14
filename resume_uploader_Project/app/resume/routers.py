from typing import List, Union, Annotated
from fastapi import APIRouter, Form, UploadFile, File, Depends, HTTPException, status
from app.db.config import DbSession
from app.resume.service import create_resume, get_all_resume
from app.resume.schemas import ResumeCreate, ResumeOut, GenderEnum
from pydantic import EmailStr
from datetime import date
router = APIRouter(prefix='/resumes', tags=["Resume"])

@router.post('/upload', response_model=ResumeOut )
async def upload_resume(
    *,
    name: str = Form(...),
    email: EmailStr = Form(...),
    dob: date = Form(...),
    state: str = Form(...),
    gender: GenderEnum = Form(...),
    preferred_locations: str = Form(...),    image : UploadFile = File(),
    resume_file : UploadFile = File(),
    session : DbSession
):
    data = ResumeCreate(
        name=name,
        email=email,
        dob=dob,
        state=state,
        gender=gender,
        preferred_locations=preferred_locations
    )
    return await create_resume(session,data, image, resume_file)

@router.get('/get', response_model=List[ResumeOut])
async def get_resume(session : DbSession):
    try:
        resume = await get_all_resume(session)
        return resume
    except Exception as e:
        raise HTTPException(500, f"Error: {e}")
    
