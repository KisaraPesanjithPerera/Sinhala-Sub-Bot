import re
from typing import Text
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, InlineQuery, InlineQueryResultArticle, \
InputTextMessageContent



def nospace(s):

    s = re.sub(r"\s+", '%20', s)

    return s

@Client.on_message(filters.command("onlinev"))
async def movie(_, message):
    name = nospace(message.text.strip().split(None, 1)[1].lower())
    m = await message.reply_text("**Searching๐ฟ**")
    await m.edit("๐๐ ๐๐๐จ๐ช๐ก๐ฉ ๐๐ค๐ง ๐๐ค๐ช๐ง ๐๐ช๐๐ง๐ฎ ๐๐")
    try:
        await message.reply_chat_action("typing")
        await message.reply_text(
            text=f"Result for your requested query `{name}` \n\n็ฟโโโโโโโโโโโโโโโ็ฟ\n\n**๐ View It Online :** [Link Here](https://www.2embed.ru/embed/imdb/movie?id={name})\n**โญ๏ธ IMDB Link : [View Movie Details On imdb](https://www.imdb.com/title/{name}/) \n\n๐ฅท ๐ฃ๐ผ๐๐ฒ๐ฟ๐ฒ๐ฑ ๐๐ ๐ฅท : @AnonymousBotsInfinity \n\n็ฟโโโโโโโโโโโโโโโ็ฟ\n\n๐Brought to You : {message.chat.title}\n\n`โ โ โ โ โ โ โ โ โ โ โ โ โ โ โ โ โ โ โ โ โ โ โ โ โ โ โ โ โ โ โ โ โ โ โ โ `",
            parse_mode="Markdown",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("View Movie ๐ป", url=f"https://www.2embed.ru/embed/imdb/movie?id={name}")
                    ]
                ]
            )
        )
    except Exception as e:
        await message.reply_text(str(e))
