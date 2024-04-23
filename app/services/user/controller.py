from fastapi import APIRouter, Depends, HTTPException, status
from  ...db.database import get_db
from sqlalchemy.orm import Session
from . import schema
from . import helpers  
from ...models import User    
from fastapi import HTTPException, Request
from . import auth

router = APIRouter(prefix="/auth",tags=["Auth"])

@router.post("/register",status_code=status.HTTP_201_CREATED)
async def create_user(register_user_body:schema.UserCreate,db:Session=Depends(get_db)):
    try:
        user=await helpers.register_user(register_user_body,db) 
        return{"message":"Registered successfully","user":user}    
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500,detail=f"Error :{e}")
    
    
@router.post("/login",status_code=status.HTTP_201_CREATED)
async def login_user(login_user_body:schema.UserLogin,db:Session=Depends(get_db)):
    try:
        print(login_user_body,",+>>>>>>")
        token=await helpers.login_user(login_user_body,db)
        return {"access_token":token,"token_type":"Bearer"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500,detail=f"Error :{e}")    
        
    
@router.get("/user-me",status_code=status.HTTP_200_OK,dependencies=[Depends(auth)])
async def get_me(request:Request,db:Session=Depends(get_db)):
    try:
        user:User = request.state.current_user
        print({"user":user})
        return {"user":user} 
    except HTTPException as e:
        # Catch and re-raise HTTPException (Unauthorized will be handled here)
        raise HTTPException(status_code=500,detail=f"Error :{e}")  
        
        
        

        
