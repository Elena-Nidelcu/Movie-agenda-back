from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from datetime import datetime, timedelta
from jose.exceptions import ExpiredSignatureError

SECRET_KEY = "secret"  # Replace with a secure key in production
ALGORITHM = "HS256"

# This tells Swagger to show a simple Bearer token input field
oauth2_scheme = HTTPBearer()

def create_token(data: dict, expires_delta=timedelta(minutes=1)):
    to_encode = data.copy()
    to_encode.update({"exp": datetime.utcnow() + expires_delta})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_token(credentials: HTTPAuthorizationCredentials = Depends(oauth2_scheme)):
    token = credentials.credentials
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return decoded
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

def check_permission(decoded, required: str):
    if "permissions" in decoded and required in decoded["permissions"]:
        return True
    if decoded.get("role") == "ADMIN":
        return True
    raise HTTPException(status_code=403, detail="Forbidden")
