from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def healthCheck():
    """
    
    Endpoint for handling healthcheck

    """
    return "Voilla, I am alive!"

