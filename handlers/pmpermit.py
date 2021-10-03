from callsmusic.callsmusic import client as USER

from pyrogram import filters

from pyrogram.types import Chat, Message, User

@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)

async def pmPermit(client: USER, message: Message):

  await USER.send_message(message.chat.id,"Hello, I'm lovely official **music assistant of @LOVELYR_OBOT.**\n\n❗️ **notes:**\n\n⫸ don't spam message.\n⫸ don't send me anything confidential\n\n⨀ Join to @ABOUTVEDMAT \n⨀ Join to @LOVELYAPPEAL\n\n🤴 Dev: @TUSHAR204\n\n👩🏻‍🔧 If you want me join to your group, send here your group link, I will joined as soon as possible.\n\n")
   
  return                        

