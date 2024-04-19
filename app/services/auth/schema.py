from pydantic import BaseModel
from typing import Optional, Union
class UserCreate(BaseModel):
    """
    Data model for creating a user 
    """
    email:str
    password:str
    role:str
    user_name:str
    full_name: Optional[Union[str, None]]


class UserCreateResponseData(UserCreate):
    """Response data"""
    id:int    
    
    
class UserCreateResponse(BaseModel):
    """User create response"""
    message:str
    user:Optional[Union[UserCreateResponseData,None]]   