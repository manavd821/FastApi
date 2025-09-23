from fastapi import APIRouter

router = APIRouter(prefix='/users',tags = ["users"])

@router.get('/users', tags = ["users"])
async def user_data():
    return "I'm User router brother."

# products
router2 = APIRouter()
@router2.get('/')
async def products_data():
    return "I'm Products router brother."