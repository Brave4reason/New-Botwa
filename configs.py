import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "26190095"))
  API_HASH = os.environ.get("API_HASH", "5aa2f97407dbd5a32c9668a5e3a926ba")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "6853611135:AAGKDfpA157zr4LwHYleQPG442qSAmLBpRQ")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "MangaTalesbot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002087845070"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "ez4short.com")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "48ed7c689c8293e23dcfd7a9cd8b5476085d52d9")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "1179962433"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://bravebrowsersurface:0kvqPevUYtGifz3J@cluster0.jbx8dbw.mongodb.net/NewEra")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001362178944")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002056372468"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""
 ʜᴇʀᴇ ᴡᴇ ɢᴏ ᴄʜᴇᴄᴋᴏᴜᴛ ᴍʏ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ✔
  
 🚩 ʟᴏᴏᴋ ʙᴇʟᴏᴡ ᴍʏ ꜰʀɪᴇɴᴅ 🚩

▶ ᴍʏ ɴᴀᴍᴇ : ꜰɪʟᴇ ꜱᴛᴏʀᴇ
▶ ꜱᴇʀᴠᴇʀ : ʜᴇʀᴏᴋᴜ
▶ ᴏᴡɴᴇʀ : [ᴋʜᴀɴᴅᴜᴅᴏɴ](t.me/Xbhau)

🌿 ɴᴇᴠᴇʀꜰᴏʟᴅ ɴᴇᴠᴇʀ ʙᴀᴄᴋᴅᴏᴡɴ 🌿
"""
  ABOUT_DEV_TEXT = f"""
ᴍʏ ᴅᴇᴠ: [➡](https://telegram.me/Xbhau)
 
 I am Super noob Please Support My Hard Work. 🐸
"""
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **File Store Bot**.

📢 ꜱᴇɴᴅ ᴍᴇ ᴀɴʏ ꜰɪʟᴇ & ɪᴛ ᴡɪʟʟʙᴇ ᴜᴘʟᴏᴀᴅᴇᴅ ɪɴ ᴍʏ ᴅᴀᴛᴀʙᴀꜱᴇ & ʏᴏᴜ ᴡɪʟʟ ɢᴇᴛ ᴛʜᴇ (ꜱʜᴏʀᴛᴇɴᴇᴅ) ꜰɪʟᴇ ʟɪɴᴋ.
"""
