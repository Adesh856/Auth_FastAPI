from datetime import datetime, timedelta
from fastapi import FastAPI, Depends
from jose import jwt
from typing import Optional
import time 
import app.services.user.schema as schema 
from .config import config   
import app
from .models import User  
from .db.database import get_db
from sqlalchemy.orm import Session 
from fastapi import HTTPException, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import pytz
# Secret key for JWT encoding and decoding. 
# NOTE: Keep this secure and don't expose it in your code.
SECRET_KEY=config["jwt"]["secret"]
ALGORITHM=config["jwt"]["algorithm"]
           
class JWTTokenAuthMiddleware:
    def __init__(self, required: bool = True):
        self.required = required
        self.auth_scheme = HTTPBearer()

    async def __call__(self, request: Request, db: Session = Depends(get_db)):
        credentials: HTTPAuthorizationCredentials = await self.auth_scheme(request)
        if not credentials:
            raise HTTPException(status_code=401, detail="Unauthorized")

        token = credentials.credentials
        verified_data = self.verify_token(token)
        if not verified_data:
            raise HTTPException(status_code=401, detail="Unauthorized")

        email = verified_data.get("email")
        username = verified_data.get("user_name")

        if email:
            user = db.query(User).filter(User.email == email).first()
        elif username:
            user = db.query(User).filter(User.user_name == username).first()
        else:
            raise HTTPException(status_code=401, detail="Unauthorized")

        if not user:
            raise HTTPException(status_code=401, detail="Unauthorized")

        request.state.current_user = user

    def verify_token(self, token: str) -> Optional[dict]:
        """Verify JWT token"""
        try:
            payload = jwt.decode(token, config["jwt"]["secret"], algorithms=[config["jwt"]["algorithm"]])
            # Validate token expiration
            exp = payload.get("exp")
            iat = payload.get("iat")
            print({"payload":payload})
            print(datetime.fromtimestamp(exp) , datetime.now())
            if exp and exp < time.time():
                raise HTTPException(status_code=401, detail="Token expired")
            return payload
        except jwt.JWTError:
            raise HTTPException(status_code=401, detail="Invalid token")
    
    
      
    def create_access_token(self,data:dict,expire:Optional[timedelta]=None): 
        """Create JWT token"""
        try:
            print({"data":data,"expire":expire})
            jwt_encode_data = data.copy()
            if expire:
                jwt_expire = datetime.utcnow()+expire
            else:
                jwt_expire = datetime.utcnow()+timedelta(minutes=20)
                    
            jwt_encode_data.update({"exp":jwt_expire,"iat":datetime.utcnow()})
            print(jwt_encode_data)
            token = jwt.encode(jwt_encode_data,SECRET_KEY,algorithm=ALGORITHM)        
            return token
        except Exception as e:
            raise e 
    
 
