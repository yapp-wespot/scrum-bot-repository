import discord
import holidays
import os
from discord.ext import commands
from datetime import datetime

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="./", intents=intents)
TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL_ID"))

messages = [
  """고통의 월요일 ♥️
  데일리 스크럼 시간이에요 BFF ⏰
  주말에 한 일과 오늘 할 일을 공유해보아요 🔥
  레 츠 고 우 🚀""",
  """절망의 화요일 ♥️
  데일리 스크럼 시간이에요 BFF ⏰
  어제 한 일과 오늘 할 일을 공유해보아요 🔥
  레 츠 고 우 🚀""",
  """스크럼 시간이에요 BFF🏋🏻
  위스팟 어디까지 왔나요! ☄️
  1) 주말 이후 새롭게 한 일과 2) 일요일까지의 목표를 공유해보아요 🚀""",
  """희망의 목요일 ♥️
  데일리 스크럼 시간이에요 BFF ⏰
  어제 한 일과 오늘 할 일을 공유해보아요 🔥
  레 츠 고 우 🚀""",
  """환희의 금요일 ♥️
  데일리 스크럼 시간이에요 BFF ⏰
  어제 한 일과 오늘 할 일을 공유해보아요 🔥
  어쩔 티비도 화이팅 🚀""",
  """위클리 스크럼 시간이에요 BFF🏋🏻
  시간이 너무 빠르다 빨라⏰
  이번주 한 일과 다음주에 할 일을 공유해보아요 🚀
  """,
  """스크럼 시간이에요 BFF🏋🏻
  목표 잘 지켜봅시다앙 ☄️
  1) 이번주 한 일과 2) 다음주 중 할 일을 공유해보아요 🚀🔫"""
]


# DATES=[datetime(2024, 7, 31, 23, 0), datetime(2024, 8, 21, 23, 0), datetime(2024, 8, 31, 23, 0), datetime(2024, 9, 14, 23, 0), datetime(2024, 9, 14, 23, 0)]
# MESSAGES_BY_DATES=["📢 2차 스프린트 마감 D-{} 📢", "📢 이제는 더 이상 물러날 곳이 없다 D-{} 📢", "📢 데모데이 두 과 자 🥰 D-{} 📢","📢 1등 두 과 자 🥰 D-{} 📢", "📢 홍보 두 과 자 🥰 📢"]

async def send_daily_message():
  await client.wait_until_ready()
  channel = client.get_channel(CHANNEL_ID)
  now = datetime.now()
  month = str(now.month)
  day = str(now.day)

  weekday = now.weekday()
  # kr_holidays = holidays.KR(years=now.year)

  if weekday not in [2, 6]:
    return

  # if weekday != 6 and (now.date() in kr_holidays or weekday % 2 != 0):
  #   return

  if channel:
    # dday_message = getDdayMessage(now)
    daily_message = f"{month}/{day} {messages[weekday]}"
    # createMessage = await channel.send(dday_message+"\n\n"+daily_message)
    created_message = await channel.send(daily_message)
    await created_message.create_thread(name=month + "/" + day)
  else:
    print(f"Cannot find channel with ID {str(CHANNEL_ID)}")


# def getDdayMessage(now):
#     index=0
#     dday=0
#     messageByDate=""

#     while index < len(DATES):
#         dday=(DATES[index]-now).days
#         messageByDate=MESSAGES_BY_DATES[index]
#         if 0<=dday:
#             break
#         index+=1

#     if dday<0:
#         return messageByDate

#     return messageByDate.format(dday)


@client.event
async def on_ready():
  await client.change_presence(
      status=discord.Status.online, activity=discord.Game("스크럼 봇 가동")
  )
  await send_daily_message()
  await client.close()


client.run(TOKEN)
