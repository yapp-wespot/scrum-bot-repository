import discord
import holidays
import os
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext import commands
from datetime import datetime
from apscheduler.triggers.cron import CronTrigger
import pytz

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='./',intents=intents)
TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = int(os.getenv('DISCORD_CHANNEL_ID'))

messages = [
    "고통의 월요일 ♥️\n"+
    "데일리 스크럼 시간이에요 BFF ⏰\n"+
    "주말에 한 일과 오늘 할 일을 공유해보아요 🔥\n"+
    "레 츠 고 우 🚀",
    "절망의 화요일 ♥️\n"+
    "데일리 스크럼 시간이에요 BFF ⏰\n"+
    "어제 한 일과 오늘 할 일을 공유해보아요 🔥\n"+
    "레 츠 고 우 🚀",
    "인내의 수요일 ♥️\n"+
    "데일리 스크럼 시간이에요 BFF ⏰\n"+
    "어제 한 일과 오늘 할 일을 공유해보아요 🔥\n"+
    "9:30 회의도 잊지 말기 🚀",
    "희망의 목요일 ♥️\n"+
    "데일리 스크럼 시간이에요 BFF ⏰\n"+
    "어제 한 일과 오늘 할 일을 공유해보아요 🔥\n"+
    "레 츠 고 우 🚀",
    "환희의 금요일 ♥️\n"+
    "데일리 스크럼 시간이에요 BFF ⏰\n"+
    "어제 한 일과 오늘 할 일을 공유해보아요 🔥\n"+
    "내일 만나욤 🚀",
]

async def send_daily_message():
    await client.wait_until_ready()
    channel = client.get_channel(CHANNEL_ID)
    now = datetime.now()
    month = str(now.month)
    day = str(now.day)

    weekday= now.weekday()
    kr_holidays = holidays.KR(years=now.year)
    if now.date() in kr_holidays or 5 <= weekday:
        return;

    if channel:
        createMessage = await channel.send(month+"/"+day+" "+messages[weekday])
        await createMessage.create_thread(name=month+"/"+day)
    else:
        print(f"Cannot find channel with ID {str(CHANNEL_ID)}")

async def startScheduler():
    KST = pytz.timezone('Asia/Seoul')
    scheduler = AsyncIOScheduler(timezone=KST)
    scheduler.add_job(send_daily_message, CronTrigger(hour=3, minute=0))
    scheduler.start()

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('스크럼 봇 가동'))
    await startScheduler()

client.run(TOKEN)
