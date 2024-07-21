import discord
import holidays
import yaml
from discord.ext import commands
from datetime import datetime

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='./',intents=intents)
with open("application.yml", "r") as file:
    config = yaml.safe_load(file)
TOKEN=config["discord"]["token"]
CHANNEL_ID=int(config["discord"]["channel_id"])

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

    # weekday= now.weekday()
    # kr_holidays = holidays.KR(years=now.year)
    # if now.date() in kr_holidays or 5 <= weekday:
    #     return;

    if channel:
        for message in messages:
            createMessage = await channel.send(month+"/"+day+" "+message)
            await createMessage.create_thread(name=month+"/"+day)
    else:
        print(f"Cannot find channel with ID {str(CHANNEL_ID)}")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('스크럼 봇 가동'))
    await send_daily_message()

client.run(TOKEN)