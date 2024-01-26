from dotenv import load_dotenv
import os

load_dotenv("docker.env")

DB_HOST = os.environ.get("POSTGRES_HOST")
DB_PORT = os.environ.get("POSTGRES_PORT")
DB_USER = os.environ.get("POSTGRES_USER")
DB_NAME = os.environ.get("POSTGRES_DB")
DB_PASS = os.environ.get("POSTGRES_PASSWORD")
JWT_SECRET = os.environ.get("JWT_SECRET")
JWT_ALGORITHM = os.environ.get("JWT_ALGORITHM")

# print(DB_HOST)
# print(DB_PORT)
# print(DB_USER)
# print(DB_NAME)
# print(DB_PASS)
# print(JWT_SECRET)
# print(JWT_ALGORITHM)