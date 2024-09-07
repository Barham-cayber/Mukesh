class Config(object):
    LOGGER = True
    API_ID =27442758
    API_HASH = "8288c5c54f568ee346b3227271700b52"
    TOKEN = "7104421875:AAHk0NmGYO3lMZI69CbZwuLDi6NJtCuchWw"  
    OWNER_ID=5576431780
    
    SUPPORT_CHAT = "-1002100221457" 
    START_IMG = "https://t.me/photosmyys/2"
    EVENT_LOGS = (-1002032682720)
    MONGO_DB_URI= "mongodb+srv://barham7726:Barham1234@cluster0.ll412.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
   
    DATABASE_URL = "postgres://avnadmin:AVNS_NusHYCfUDFlQ7kRdxri@joinbot-barhammhamad7726-593f.i.aivencloud.com:17809/defaultdb?sslmode=require"  # A sql database url from elephantsql.com
    CASH_API_KEY = (
        ""
    )
    TIME_API_KEY = "VT36FQYTDRFQ"

    
    BL_CHATS = [] 
    DRAGONS = []
    DEV_USERS = []  
    DEMONS = [] 
    TIGERS = []  
    WOLVES = [] 

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8
    

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
