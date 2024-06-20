from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID" "14411702"))
API_HASH = getenv("API_HASH" "6f8aaf5bd4f6538f06bc31ee67460f99")

BOT_TOKEN = getenv("BOT_TOKEN" "5964460738:AAHAQGJzZQZlcjFmGc_g_CAR7U7rwzydfsQ")
#OWNER_ID = int(getenv("6664582540"))
OWNER_ID = int(getenv("OWNER_ID", "6664582540"))
MONGO_DB_URI = getenv("MONGO_DB_URI" "mongodb+srv://hnyx:wywyw2@cluster0.9dxlslv.mongodb.net/?retryWrites=true&w=majority")
MUST_JOIN = getenv("MUST_JOIN", None)
