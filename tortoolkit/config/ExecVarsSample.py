try:
    from .ExecVars import ExecVars
except:
    class ExecVars:
        # Set true if its VPS
        IS_VPS = False
        
        API_HASH = "c3938398e16d852d6dd2728010adc67e"
        API_ID = 7295027
        BOT_TOKEN = "2085575909:AAGeEHsGtABjb90VJ2m8Q29Smt8qWi_y1TM"
        BASE_URL_OF_BOT = "https://awsultrabot.herokuapp.com"

        # Edit the server port if you want to keep it default though.
        SERVPORT = 80

        # ALLOWED USERS [ids of user or supergroup] seperate by commas
        ALD_USR = [-1001522829507,-1001290201765,-1001534004319,-1001530013795,-351960915]
        OWNER_ID = 1909533856
        
        # Google Drive Index Link should include the base dir also See readme for more info
        GD_INDEX_URL = https://aws.cmd-server.workers.dev/0:

        # Time to wait before edit message
        EDIT_SLEEP_SECS = 40

        # Telegram Upload Limit (in bytes)
        TG_UP_LIMIT = 109900000000

        # Should force evething uploaded into Document
        FORCE_DOCUMENTS = True

        # Chracter to use as a completed progress 
        COMPLETED_STR = "🟩"

        # Chracter to use as a incomplete progress
        REMAINING_STR = "🟨"

        # DB URI for access
        DB_URI = ""
        
        # UNCOMMENT THE BELOW LINE WHEN USING CONTAINER AND COMMENT THE UPPER LINE
        #DB_URI = "dbname=tortk user=postgres password=your-pass host=db port=5432"

        # Use the central update (everything will be updated in one msg)
        CENTRAL_UPDATE = True

        # MEGA CONFIG
        MEGA_ENABLE = True
        MEGA_API = "jqA3EIKQ"
        MEGA_UNAME = rootg999@gmail.com
        MEGA_PASS = rootgamer@1
        ALLOW_MEGA_FOLDER = True
        ALLOW_MEGA_FILES = True
        MAX_MEGA_LIMIT = 

        # qBittorrent Config
        # TODO add port, retry to ints
        QBIT_HOST = "localhost"
        QBIT_PORT = 8090
        QBIT_UNAME = "admin"
        QBIT_PASS = "adminadmin"
        QBIT_MAX_RETRIES = 2
        ADD_CUSTOM_TRACKERS = True
        TRACKER_SOURCE = "https://raw.githubusercontent.com/XIU2/TrackersListCollection/master/all.txt"

        # Gdrive Config
        GDRIVE_BASE_DIR = "/"

        # Onedrive Config
        ONEDRIVE_BASE_DIR = "/"
        ONEDRIVE_BASE_FOLDER_URL = ""
        ONEDRIVE_INDEX_URL = ""

        # The base direcory to which the files will be upload if using RCLONE for other engine than GDRIVE/ONEDRIVE
        RCLONE_BASE_DIR = "/"
        
        # Set this value to show all the remotes while leeching
        SHOW_REMOTE_LIST = False
        
        # This value will be considered only if Rclone is True - this may be defied now ;)
        # Cuz at least one needs to be Ture at a time either RCLONE or Leech.
        LEECH_ENABLED = True

        # Will be enabled once its set
        # For vps change it to True if config loaded
        RCLONE_ENABLED = False

        # If the user fails to select whether to use rclone or telegram to upload this will be the deafult.
        DEFAULT_TIMEOUT = "leech"

        # For vps set path here or you can use runtime too
        RCLONE_CONFIG = False
        
        # If set then you can view the downloaded files which are currently on the server
        ENABLE_WEB_FILES_VIEW = False

        # Try beta ytdl download if errored turn this off
        ENABLE_BETA_YOUTUBE_DL = True

        # Max size direct link
        MAX_DL_LINK_SIZE = 20

        # SA Account Enable/Disable. Read the readme.md before using this feature.
        ENABLE_SA_SUPPORT_FOR_GDRIVE = True
        SA_FOLDER_ID = "0ABoOyit4qjaaUk9PVA"
        SA_TD_ID = "0ABoOyit4qjaaUk9PVA"
        SA_ACCOUNTS_FOLDER = "###AWS-MIRROR-ZONE-BOT v1"
        SA_ZIP_FILE = False

        SA_ACCOUNT_NUMBER = 100

        UPTOBOX_TOKEN = "ddd37eea3b0fd8000c98a07123ba15696q6uk"

        USE_RAR_SPLIT = False

        # Name of the RCLONE drive from the config
        DEF_RCLONE_DRIVE = ""

        # Max size of a playlist that is allowed (Number of videos)
        MAX_YTPLAYLIST_SIZE = 100
        
        # Max size of the torrent allowed
        MAX_TORRENT_SIZE = 20

        # Set this to your bot username if you want to add the username of your bot at the end of the commands like
        # /leech@TorToolkitBot so the value will be @TorToolkitBot
        BOT_CMD_POSTFIX = "" 

        # Time out for the status Delete.
        STATUS_DEL_TOUT = 20

        # Allow the user settings to be accessed in private
        USETTINGS_IN_PRIVATE = False

        # Torrent max time to collect metadata in seconds
        TOR_MAX_TOUT = 180

        # This is to stop someone from abusing the system by imposing the limit
        # [<GBs of total torrent sapce>, <Number of youtube videos allowed to download>, <Number of youtube playlists allowed to download>]
        USER_CAP_ENABLE = False
        USER_CAP_LIMIT = [50,10,2]

        # No need to worry about these
        # CHANGE THESE AT YOUR RISK
        LOCKED_USERS = False
        RSTUFF = False
        FORCE_DOCS_USER = False
        FAST_UPLOAD = True
        METAINFO_BOT = False
        EXPRESS_UPLOAD = True
        





