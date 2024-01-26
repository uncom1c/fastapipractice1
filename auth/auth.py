# from fastapi_users.authentication import CookieTransport
# from fastapi_users.authentication import JWTStrategy
import time
from typing import Dict

import jwt
from config import JWT_ALGORITHM, JWT_SECRET
# from fastapi_users.authentication import AuthenticationBackend

# cookie_transport = CookieTransport(cookie_name="Bonds" ,cookie_max_age=3600)


# SECRET = JWT_SECRET

# SECRET = "SECRET"

# def get_jwt_strategy() -> JWTStrategy:
#     return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


# auth_backend = AuthenticationBackend(
#     name="jwt",
#     transport=cookie_transport,
#     get_strategy=get_jwt_strategy,
# )


secret = JWT_SECRET
algorithm = JWT_ALGORITHM

def signJWT(user_id: str) -> Dict[str, str]:
    payload = {
        "user_id": user_id,
        "expires": time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token

def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}
