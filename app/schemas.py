from pydantic import BaseModel, EmailStr
from typing import Optional

# 1. Registration Input Schema
class UserCreate(BaseModel):
    first_name: str
    last_name: str
    company_name: str
    employee_id: str
    email: EmailStr
    department: str
    password: str

# 2. User Response Schema (Hides password)
class UserOut(BaseModel):
    id: int 
    first_name: str
    last_name: str
    employee_id: str
    email: EmailStr
    department: str

    class Config:
        from_attributes = True
# 3. Login Input (Supports corporate email OR employee ID)
class UserLogin(BaseModel):
    identifier: str  # Can be email OR employee_id
    password: str

# 4. Token Response & Token Payload Schemas
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None

# 5. Password Reset Verification Request
class PasswordResetRequest(BaseModel):
    identifier: str  # Email or employee_id