from fastapi import APIRouter, status

from app.controllers.health_controller import get_health_status

router = APIRouter(tags=["health"])


@router.get("/health", status_code=status.HTTP_200_OK)
def health_check():
    """Simple health check endpoint."""
    return get_health_status()
