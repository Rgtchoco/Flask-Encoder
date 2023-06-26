# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

from .worker import *
from datetime import datetime

START_TIME = datetime.now()

async def up(event):
    if not event.is_private:
        return
    stt = dt.now()
    ed = dt.now()
    v = ts(int((ed - uptime).seconds) * 1000)
    ms = (ed - stt).microseconds / 1000
    p = f"Ping = {ms}ms"
    await event.reply(v + "\n" + p)


async def start(event):
    await event.reply(
        f"**Send me the video which you want to compress.**\n**Uptime: {str(datetime.now() - START_TIME).split('.')[0]}**",
        buttons=[
            [Button.inline("HELP", data="help")],
        ],
    )

async def zylern(event):
    await event.reply(
        f"""
**Available Commands 😉**

/start - __Check Bot is Working Or Not__
/help - __Get Detailed Help__
/setcode - __Set Custom FFMPEG Code__
/getcode - __Print Current FFMPEG Code__
/logs - __Get Bot Logs__
/ping - __Check Ping__
/sysinfo - __Get System Info__
/renew - __Clear Cached Downloads__
/clear - __Clear Queued Files__
/showthumb - __Show Current Thumbnail__
/cmds - __List Available Commands__
"""
    )


async def help(event):
    await event.edit(
        f"""**To check current ffmpeg code you can use** /getcode\n\n**You can change your ffmpeg code by executing following command.**\n\nx**265 Encoder**\n`-preset veryfast -c:v libx265 -s 854x480 -x265-params 'bframes=8:psy-rd=1:ref=3:aq-mode=3:aq-strength=0.8:deblock=1,1' -metadata 'title=Encoded By JAV STORE' -pix_fmt yuv420p -crf 24 -c:a libopus -b:a 32k -c:s copy -map 0 -ac 2 -ab 32k -vbr 2 -level 3.1 -threads 1`\n\n**Subtitles Mux**\n`/setcode -i "{SUB_LINK}" -map 0 -map 1 -c copy -c:s srt -metadata:s:s:0 language=eng`\n\n**To set custom thumbnail send me the image.**\n\n**Do /cmds For More**"""
     )   
     
async def ihelp(e):
    await e.reply(
        f"""**To check current ffmpeg code you can use** /getcode\n\n**You can change your ffmpeg code by executing following command.**\n\nx**265 Encoder**\n`-preset veryfast -c:v libx265 -s 854x480 -x265-params 'bframes=8:psy-rd=1:ref=3:aq-mode=3:aq-strength=0.8:deblock=1,1' -metadata 'title=Encoded By JAV STORE' -pix_fmt yuv420p -crf 24 -c:a libopus -b:a 32k -c:s copy -map 0 -ac 2 -ab 32k -vbr 2 -level 3.1 -threads 1`\n\n**Subtitles Mux**\n`/setcode -i "{SUB_LINK}" -map 0 -map 1 -c copy -c:s srt -metadata:s:s:0 language=eng`\n\n**To set custom thumbnail send me the image.**\n\n**Do /cmds For More**"""
    )
