class script(object):
    START_TXT = """๐ท๐ด๐ป๐พ {},
๐ผ๐ ๐ฝ๐ฐ๐ผ๐ด ๐ธ๐ <a href=https://t.me/{}>{}</a>, ๐ธ ๐ฒ๐ฐ๐ฝ ๐ฟ๐๐พ๐๐ธ๐ณ๐ด ๐ผ๐พ๐๐ธ๐ด๐, ๐น๐๐๐ ๐ฐ๐ณ๐ณ ๐ผ๐ด ๐๐พ ๐๐พ๐๐ ๐ถ๐๐พ๐๐ฟ ๐ฐ๐ฝ๐ณ ๐ด๐ฝ๐น๐พ๐ ๐"""
    HELP_TXT = """๐ท๐ด๐ {}
๐ท๐ด๐๐ด ๐ธ๐ ๐๐ท๐ด ๐ท๐ด๐ป๐ฟ ๐ต๐พ๐ ๐ผ๐ ๐ฒ๐พ๐ผ๐ผ๐ฐ๐ฝ๐ณ๐."""
    ABOUT_TXT = """<b>๐ฅฑ My Name : {}
๐ตโโ Developer : เดเดฐเตเดคเตเดคเตป 
๐ Library : ๐ฟ๐๐๐พ๐ถ๐๐ฐ๐ผ
๐ฅ Language : ๐ฟ๐๐๐ท๐พ๐ฝ ๐น
๐ช Data Base : ๐ผ๐พ๐ฝ๐ถ๐พ ๐ณ๐ฑ
๐ Server : Koyeb </b>"""
    SOURCE_TXT = """<b>NOTE:</b>
<b>๐ณ๐๐๐ ๐ก๐๐ ๐ถ๐บ๐ ๐ฌ๐บ๐๐พ๐ฝ ๐ณ๐บ๐๐๐๐ ๐ฒ๐๐๐บ๐๐ ๐ฑ๐พ๐๐๐ ๐ฎ๐ฟ ๐ฎ๐๐๐พ๐ ๐ช๐๐๐ฝ ๐ก๐๐๐
๐ฒ๐ฎ๐ด๐ฑ๐ข๐ค ๐ข๐ฎ๐ฃ๐ค ~ ๐ญ๐ฎ๐ณ ๐ ๐ต๐ ๐จ๐ซ๐ ๐ก๐ซ๐ค ๐ฑ๐จ๐ฆ๐ง๐ณ ๐ญ๐ฎ๐ถ</b>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. eva maria should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
โข /filter - <code>add a filter in chat</code>
โข /filters - <code>list all the filters of a chat</code>
โข /del - <code>delete a specific filter in chat</code>
โข /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Eva Maria Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Eva Maria supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/M4MHD)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
โข /connect  - <code>connect a particular chat to your PM</code>
โข /disconnect  - <code>disconnect from a chat</code>
โข /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
โข /id - <code>get id of a specified user.</code>
โข /info  - <code>get information about a user.</code>
โข /imdb  - <code>get the film information from IMDb source.</code>
โข /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
โข /logs - <code>to get the rescent errors</code>
โข /stats - <code>to get status of files in db.</code>
โข /delete - <code>to delete a specific file from db.</code>
โข /users - <code>to get list of my users and ids.</code>
โข /chats - <code>to get list of the my chats and ids </code>
โข /leave  - <code>to leave from a chat.</code>
โข /disable  -  <code>do disable a chat.</code>
โข /ban  - <code>to ban a user.</code>
โข /unban  - <code>to unban a user.</code>
โข /channel - <code>to get list of total connected channels</code>
โข /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """โ ๐๐พ๐๐ฐ๐ป ๐ต๐ธ๐ป๐ด๐: <code>{}</code>
โ ๐๐พ๐๐ฐ๐ป ๐๐๐ด๐๐: <code>{}</code>
โ ๐๐พ๐๐ฐ๐ป ๐ฒ๐ท๐ฐ๐๐: <code>{}</code>
โ ๐๐๐ด๐ณ ๐๐๐พ๐๐ฐ๐ถ๐ด: <code>{}</code> ๐ผ๐๐ฑ
โ ๐ต๐๐ด๐ด ๐๐๐พ๐๐ฐ๐ถ๐ด: <code>{}</code> ๐ผ๐๐ฑ"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
