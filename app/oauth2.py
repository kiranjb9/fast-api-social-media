from datetime import datetime, timedelta
from jose import JWSError, jwt

from . import models
from . import database, schemas
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def create_access_token(data : dict):
    print(data)
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp" : expire, "user_id": str(data.get("user_id"))})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt

def verify_access_token(token : str, credential_exception):
    try :
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        id  = str(payload.get("user_id"))
        print("Vwrifybg token : "+ id)

        if id is None:
            raise credential_exception
        
        token_data = schemas.TokenData(id=id)

        return token_data

    except JWSError as err:
        raise credential_exception
    
def get_current_user(token : str = Depends(oauth2_scheme),  db : Session = Depends(database.get_db)):
    credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                                         detail="Could not Validate credentials", headers={"www-Authenticate" : "Bearer"})

    token = verify_access_token(token, credential_exception)
    user = db.query(models.User).filter(models.User.id == token.id).first()
    return user