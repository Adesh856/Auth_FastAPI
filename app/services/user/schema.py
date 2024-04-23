from pydantic import BaseModel
from typing import Optional, Union
class UserCreate(BaseModel):
    """
    Schema payload for create user """
    email:str
    password:str
    role:str
    user_name:str
    full_name: Optional[str]=None

class JWT(BaseModel):
    """Schema for verification of JWT data"""
    email:Optional[str]=None
    user_name:Optional[str]=None
    
    
    
class UserLogin(JWT):
    """Schema payload for login user"""
    password:str
       
