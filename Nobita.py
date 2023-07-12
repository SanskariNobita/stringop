import os
import pyrogram
from pyrogram import Client

api_id = 24942521
api_hash = "d5d51b5b6951550229c8d29f028558f5"

try:
   os.remove("Nobita.session")
except:
     pass
with Client("Nobita", api_id=api_id, api_hash=api_hash) as app:
    session = f"💥 𝐏ʏʀᴏɢʀᴀᴍ » 𝐒ᴛʀɪɴɢ 𝐒ᴇssɪᴏɴ 💘\n\n{app.export_session_string()}\n\n🥀 𝐏ᴏᴡᴇʀᴇᴅ 𝐁ʏ: [𝐒ᴀɴsᴋᴀʀɪ_𝐗ᴅ](https://t.me/ABOUT_NOBITA_XD) 🍁"
    app.send_message("me", session, disable_web_page_preview=True)
    try:
        app.join_chat("ABOUT_NOBITA_XD")
        app.join_chat("Best_friends_chatting_01")
        app.join_chat("Best_friends_chatting_01")
        app.join_chat("ABOUT_NOBITA_XD")
    except:
        pass
    print(f"✅ String Session Has 🌟 Been Sent\nTo Your 🔥 Saved Message ✨ ...")
    os.remove("Nobita.session")
