import os

API_ID = os.environ.get("API_ID", "28526237")

API_HASH = os.environ.get("API_HASH", "936db76a74f9a52cfb2cea8a62e4c20e")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7397842341:AAFIioQE_xJKcfoLVCMtUjf04_2ZT7SFpns")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", "6486192717"))

LOG = -1002204974717

# UPDATE_GRP = , # bot sat group

# auth_chats = []

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6486192717").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


