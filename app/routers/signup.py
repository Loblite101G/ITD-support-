from .. import models, schemas, utils
from .. database import get_db
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

router = APIRouter(
    tags=["Signup"]
)


@router.post("/signup", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Check if email or employee_id already exists
    existing_user = db.query(models.User).filter(
        (models.User.employee_id == user.employee_id)
    ).first()
    
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="User with this Employee ID already exists."
        )

    # Hash password
    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    # Save to database
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user