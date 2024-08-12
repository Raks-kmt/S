import os

API_ID = 28526237

API_HASH = os.environ.get("28526237", "")

BOT_TOKEN = os.environ.get("7495845718:AAFWpgMI97godgsuwAxx8mK_YySWGeRMz6I", "")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER"6486192717 ))

LOG = 6486192717

# UPDATE_GRP = , # bot sat group

# auth_chats = []

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1923922961").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


