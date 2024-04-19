from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")

async def get_hashed_password(password):
    """ Generate a hashed password """
    try:
        return pwd_context.hash(password)
    except Exception as e:
        raise e
    
    
async def verify_password(raw_password,hashed_password):
    """ Generate a hashed password """
    try:
        return pwd_context.verify(raw_password,hashed_password)
    except Exception as e:
        raise e
    
    
    