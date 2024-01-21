from fastapi_users.authentication import CookieTransport
from fastapi_users.authentication import JWTStrategy
from config import JWT_SECRET
from fastapi_users.authentication import AuthenticationBackend

cookie_transport = CookieTransport(cookie_name="Bonds" ,cookie_max_age=3600)


SECRET = JWT_SECRET

SECRET = "SECRET"

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)
