import requests
from fastapi import HTTPException, Header
from typing import Optional
from app.config import AUTH_SERVICE_URL
from app.dto.user import UserResponse

def get_user_from_auth(authorization: str) -> Optional[UserResponse]:
    if not authorization:
        raise HTTPException(status_code=401, detail="No authorization token")
    
    try:
        response = requests.get(
            f"{AUTH_SERVICE_URL}/auth/get_user",
            headers={"Content-Type": "application/json", "Authorization": authorization}
        )
        
        if response.status_code == 200:
            user = UserResponse.parse_obj(response.json())
            if not user:
                raise HTTPException(status_code=401, detail="Invalid token")
            print(f'user: {user}')
            return user
            
        raise HTTPException(
            status_code=401, 
            detail="Invalid token"
        )
    except requests.RequestException as e:
        raise HTTPException(
            status_code=503, 
            detail="Auth service unavailable"
        )
