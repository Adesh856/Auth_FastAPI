from fastapi import APIRouter, Depends, HTTPException, status
from  ...db.database import get_db
from sqlalchemy.orm import Session
from . import schema
from ...models import User
from . import helpers        
router = APIRouter(prefix="/auth",tags=["Auth"])


@router.post("/register",status_code=status.HTTP_201_CREATED,response_model=schema.BaseModel)
async def create_user(create_user:schema.UserCreate,db:Session=Depends(get_db)):
    try:
        print(create_user)
        is_already_registered = db.query(User).filter(User.email==create_user.email).first()
        print(is_already_registered)
        
        if is_already_registered:
            raise HTTPException(status_code=400,detail="Email registered already")
        
        hashed_pass = await helpers.get_hashed_password(create_user.password)   
        print({hashed_pass})
        
        register_user = {
            "email":create_user.email,
            "password":hashed_pass,
            "role":create_user.role,
            "user_name":create_user.user_name,
            }
        print({register_user})
        if(create_user.full_name):
            register_user["full_name"]= create_user.full_name 
             
            
        register_user=User(**register_user)    
        db.add(register_user)
        db.commit()
        db.refresh(register_user)
        return {"message":"User registered successfully","user":register_user}         
    except Exception as e:
        # print(e)
        raise HTTPException(status_code=500,detail=f"Error :{e}")
    
    
    
    
    

    
