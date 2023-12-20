import os
import sys
import discord
from dotenv import load_dotenv

load_dotenv(verbose=True)

# tokenがstr型でない場合は終了させる
def getToken() -> str:
  token = os.environ.get("TOKEN")
  if token is None:
    print("TOKENが不正です。.envを確認してください。")
    sys.exit(-1)
  else: 
    return token

TOKEN = getToken()

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
  print("ログインしました。")

@client.event
async def on_message(message):
  # ユーザがbotの場合は実行しない
  if message.author.bot:
    return
  
  # Helloメッセージ
  if message.content == "/kururi":
    await message.channel.send(
      "Kururiコマンドを使ってくれてありがとう！　ぼくはくるりんだよ！　よろしくね！",
      reference = message,
    )
  
  # TwitterのURLを埋め込める形に変更する
  if "x.com" in message.content:
    output = message.content.replace("x.com", "vxtwitter.com")
    await message.channel.send(
      output,
      reference = message,
    )

client.run(TOKEN)