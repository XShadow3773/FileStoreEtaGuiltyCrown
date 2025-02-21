# Don't Remove Credit @CodeFlix_Bots, @rohit_1888
# Ask Doubt on telegram @CodeflixSupport


import os
from os import environ,getenv
import logging
from logging.handlers import RotatingFileHandler

#rohit_1888 on Tg

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7542241757:")
#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "25984365"))
#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "f16f22343566116e2319621b07ba5013")
#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002178943213"))
# NAMA OWNER
OWNER = os.environ.get("OWNER", "Kirito3009")
#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6673527661"))
#Port
PORT = os.environ.get("PORT", "8030")
#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://cidkagenou0195:dQfbyNG22SzGra99@cluster0.cd4yf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Kagenou")

#Time in seconds for message delete, put 0 to never delete
TIME = int(os.environ.get("TIME", "0"))


#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL1 = int(os.environ.get("FORCE_SUB_CHANNEL1", "-1001991235299"))
#put 0 to disable
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002203178713"))#put 0 to disable
FORCE_SUB_CHANNEL3 = int(os.environ.get("FORCE_SUB_CHANNEL3", "-1002346689386"))#put 0 to disable
FORCE_SUB_CHANNEL4 = int(os.environ.get("FORCE_SUB_CHANNEL4", "-1002424441673"))#put 0 to disable

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/ec17880d61180d3312d6a.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://telegra.ph/file/e292b12890b8b4b9dcbd1.jpg")

# Turn this feature on or off using True or False put value inside  ""
# TRUE for yes FALSE if no 
TOKEN = True if os.environ.get('TOKEN', "True") == "True" else False 
SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "gplinks.com")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "8e5f09dc005bfde7412c3b08a8a73e60a5d012c6")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 3600)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "True")
TUT_VID = os.environ.get("TUT_VID","https://t.me/hw_to_open_links/2")


HELP_TXT = "<b><blockquote>ᴛʜɪs ɪs ᴀɴ ғɪʟᴇ tᴏ ʟɪɴᴋ ʙᴏᴛ ᴡᴏʀᴋ ғᴏʀ @XShadow3773\n\n❏ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs\n├/start : sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ\n├/about : ᴏᴜʀ Iɴғᴏʀᴍᴀᴛɪᴏɴ\n└/help : ʜᴇʟᴘ ʀᴇʟᴀᴛᴇᴅ ʙᴏᴛ\n\n sɪᴍᴘʟʏ ᴄʟɪᴄᴋ ᴏɴ ʟɪɴᴋ ᴀɴᴅ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ᴊᴏɪɴ ᴀʟʟ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ ᴛʜᴀᴛs ɪᴛ.....!\n\n ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ <a href=https://t.me/Shadow_garden3773>ᴄɪᴅ ᴋᴀɢᴇɴᴏᴜ</a></blockquote></b>"


ABOUT_TXT = "<b><blockquote>◈ ᴄʀᴇᴀᴛᴏʀ: <a href=https://t.me/XShadow3773>ᴄɪᴅ ᴋᴀɢᴇɴᴏᴜ</a>\n◈ ꜰᴏᴜɴᴅᴇʀ ᴏꜰ : <a href=https://t.me/Shadow_Garden3773>ꜱʜᴀᴅᴏᴡ ɢᴀʀᴅᴇɴ</a>\n◈ ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/Shadow_Garden3773>ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ</a>\n◈ ᴍᴏᴅᴇᴅ ᴀᴘᴘꜱ : <a href=https://t.me/Shadow_Mods3773>ᴍᴏᴅᴇᴅ ᴀᴘᴘꜱ</a>\n◈ ɢᴜɪʟᴛʏ ᴄʀᴏᴡɴ : <a href=https://t.me/Guilty_Crown3773>ᴘᴀɪᴅ ᴄᴏᴜʀꜱᴇꜱ</a>\n◈ ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href=https://t.me/XShadow3773>ᴄɪᴅ ᴋᴀɢᴇɴᴏᴜ</a></blockquote></b>"


START_MSG = os.environ.get("START_MESSAGE", "<b><blockquote>ʜᴇʏ ᴛʜᴇʀᴇ {first}\n\n ɪ ᴀᴍ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ, ɪ ᴄᴀɴ sᴛᴏʀᴇ ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇs ɪɴ sᴘᴇᴄɪғɪᴇᴅ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴏᴛʜᴇʀ ᴜsᴇʀs ᴄᴀɴ ᴀᴄᴄᴇss ɪᴛ ғʀᴏᴍ sᴘᴇᴄɪᴀʟ ʟɪɴᴋ.</blockquote></b>")
try:
    ADMINS=[6376328008]
    for x in (os.environ.get("ADMINS", "5779295913").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʟʟᴏ {first}\n\n<b>ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ʀᴇʟᴏᴀᴅ button ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛᴇᴅ ꜰɪʟᴇ.</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>• ʙʏ @XShadow3773</b>")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b><blockquote>BOT UPTIME\n{uptime}</blockquote></b>"
USER_REPLY_TEXT = "ɪᴅɪᴏᴛ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ᴍᴀꜱᴛᴇʀ!"

ADMINS.append(OWNER_ID)
ADMINS.append(6497757690)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
