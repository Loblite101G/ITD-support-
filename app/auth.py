from fastapi import APIRouter, Depends, HTTPException, status
from app import models, schemas, utils
from sqlalchemy.orm import Session
from .database import get_db

router = APIRouter(tags=['Authentication'])

@router.post("/login")
def login(user_credentials: schemas.UserLogin, db: Session = Depends(get_db)):
    
    # Query database using email OR employee_id
    user = db.query(models.User).filter(
        (models.User.email == user_credentials.identifier) | 
        (models.User.employee_id == user_credentials.identifier)
    ).first()

    # Verify user exists and password matches
    if not user or not utils.verify(user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail="Invalid Credentials"
        )

    return {"message": "Login successful", "user_id": user.id}