from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_photo("https://telegra.ph/file/632730fba83716c858045.jpg")
    await message.reply_text(
        f"""**Hey, I'm LOVELY MUSIC BOT🎵

I can play ꬺᶙȿᶖɕ  in your group's voice CHAT Developed by [#ℓσvєℓyทєτωσrк](https://t.me/LOVELY_NETWORK)

Add me to your group and play music freely😆!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📠 Source Code 📠", url="https://github.com/TEAM-LOVELY/MUSIC")
                  ],[
                    InlineKeyboardButton(
                        "⚜ SUPPORT GROUP ⚜", url="https://t.me/LOVELY_5UPPORT"
                    ),
                    InlineKeyboardButton(
                        "🔷️ UPDATE CHANNEL 🔷️", url="https://t.me/LOVELY_NETWORK"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "GROUP ME LEJAO 😆", url="https://t.me/LOVELYR_OBOT?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**#ℓσvєℓyทєτωσrк**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔷️ UPDATE CHANNEL 🔷️", url="https://t.me/LOVELY_NETWORK")
                ]
            ]
        )
   )


