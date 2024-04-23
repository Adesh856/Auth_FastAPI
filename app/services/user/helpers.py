from passlib.context import CryptContext
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")
from . import schema
from ...models import User  
from . import auth
from datetime import datetime,timedelta



def get_hashed_password(password):
    """ Generate a hashed password """
    try:
        return pwd_context.hash(password)
    except Exception as e:
        raise e
    
    
def verify_password(raw_password,hashed_password):
    """ Generate a hashed password """
    print({"raw_password":raw_password,"hashed_password":hashed_password})
    try:
        return pwd_context.verify(raw_password,hashed_password)
    except Exception as e:
        raise e
    
    
async def register_user(register_user_body:schema.UserCreate,db:Session):
    print(register_user_body)
    is_already_registered = db.query(User).filter(User.email==register_user_body.email).first()
    print(is_already_registered)
    
    if is_already_registered:
        raise HTTPException(status_code=400,detail="Email registered already")
    
    hashed_pass =get_hashed_password(register_user_body.password)   
    print({hashed_pass})
    
    new_user = {
        "email":register_user_body.email,
        "password":hashed_pass,
        "role":register_user_body.role,
        "user_name":register_user_body.user_name,
        }
    print({"register_user_body":register_user_body})
    if(register_user_body.full_name):
        new_user["full_name"]= register_user_body.full_name 
            
        
    user_instance=User(**new_user)    
    db.add(user_instance)
    db.commit()
    db.refresh(user_instance)
    return user_instance


async def login_user(login_user_body:schema.UserCreate,db:Session):
    print({"login_user_body":login_user_body})   
    if(not login_user_body.email and not login_user_body.user_name):
        raise HTTPException(status_code=400,detail="Please provide either email or user_name")
        
    if(login_user_body.email):
        user = db.query(User).filter(User.email==login_user_body.email,User.is_deleted==False).first()
    elif(login_user_body.user_name):
        user=db.query(User).filter(User.user_name==login_user_body.user_name,User.is_deleted==False).first()
        
        print({"user":user})
    if not user:
        raise HTTPException(status_code=404,detail="Please register , your email or user_name not registered, if you are trying to login for admin its not admin email") 
    
    is_verified = verify_password(raw_password=login_user_body.password,hashed_password=user.password)
    print({"is_verified":is_verified})
    
    if is_verified == False:
        raise HTTPException(status_code=401, detail="Incorrect password")
    
    token_data = {
        "user_name": user.user_name,
        "full_name":user.full_name,
        "email": user.email,
        "type": "userLogin"
    }
    token:str = auth.create_access_token(data=token_data,expire=timedelta(minutes=1))
    print("token",token,",======> token")
    
    return token
    

    
    
    
    
        
   