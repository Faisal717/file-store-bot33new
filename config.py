
import re
import os
from os import getenv, environ
from Script import script 
from dotenv import load_dotenv

load_dotenv()




id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


      
# Owner Information
API_ID = int(environ.get("API_ID", "26444821"))
API_HASH = environ.get("API_HASH", "a58efd1d6483e3f0d5b2757d9f665c24")
ADMINS = int(environ.get("ADMINS", "1581901379"))

# Database Information
CLONE_DB_URI = environ.get("CLONE_DB_URI", "mongodb+srv://abhay:store@store.nmvpb5w.mongodb.net/?retryWrites=true&w=majority&appName=STORE")
CDB_NAME = environ.get("CDB_NAME", "STORE")
DB_URI = environ.get("DB_URI", "mongodb+srv://faisal717890:6ubS66w0zjO3iQ9I@cluster0.e4kxk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = environ.get("DB_NAME", "Cluster0")


# Bot Information
BOT_TOKEN = environ.get("BOT_TOKEN", "7150728438:AAEy6w9m76PjsiogVrmGEeFgHBNFspDmwQM")
BOT_USERNAME = environ.get("BOT_USERNAME", "Eren_Yeager_007_Bot") # your bot username without @
PICS = (environ.get('PICS', 'https://te.legra.ph/file/66604e5911df5a0c43ffa.jpg https://graph.org/file/f5a26ac21b060d5787ea3.jpg https://graph.org/file/30539d8f1fc92423d6a19.jpg https://graph.org/file/701ff72fb43d85e073f03.jpg')).split() # Bot Start Picture

# Auto Delete Information
AUTO_DELETE = int(environ.get("AUTO_DELETE", "30")) # Time in Minutes
AUTO_DELETE_TIME = int(environ.get("AUTO_DELETE_TIME", "1800")) # Time in Seconds

# Channel Information
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002074725398"))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1002007551275')).split()]

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

# File Caption Information
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)

# Enable - True or Disable - False
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)



# File Stream Config
class Var(object):
    MULTI_CLIENT = True
    name = str(getenv('name', 'filetolinkvjbot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1002104141224'))
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
        URL = ""
    else:
        URL = ""




    
