from dotenv import load_dotenv
import os
load_dotenv()

config={
   "jwt":{
       "algorithm":os.getenv("JWT_ALGORITHM"),
       "secret":os.getenv("SECRET_KEY")
   }
}
    

    