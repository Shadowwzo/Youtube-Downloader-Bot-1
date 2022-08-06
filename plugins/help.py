from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Just Send me Any YouTube link ans i will download it for your in your favourable size. Join @Anime_lifee for watching anime. @Shadow_10_YT is my owner"
    await message.reply_text(helptxt)
