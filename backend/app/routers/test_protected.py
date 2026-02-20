from fastapi import APIRouter, Depends
from app.utils.dependencies import get_current_user, require_role
from app.models.user import User

router = APIRouter(prefix="/test", tags=["Protected Routes"])

@router.get("/me")
def get_me(current_user: User = Depends(get_current_user)):
    return {
        "email": current_user.email,
        "role": current_user.role
    }

@router.get("/admin-only")
def admin_route(current_user: User = Depends(require_role("admin"))):
    return {"message": "Welcome Admin"}
