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

async def reply_in_thread(message, content):
  """スレッドの中で返信する"""
  
  thread = None
  for t in message.channel.threads:
    if t.name == f"reply-to-{message.id}":
      thread = t
      break
  
  if thread is None:
    thread = await message.create_thread(name=f"reply-to-{message.id}")
  await thread.send(content)

@client.event
async def on_message(message):
  # ユーザがbotの場合は実行しない
  if message.author.bot:
    return
  
  # Helloメッセージ
  if message.content == "/kururi":
    print(f"Kururiコマンドを検知: {message.content}")
    await reply_in_thread(
      message,
      "Kururiコマンドを使ってくれてありがとう！　ぼくはくるりんだよ！　よろしくね！",
    )
  
  # TwitterのURLを埋め込める形に変更する
  if "x.com" in message.content:
    print(f"Twitterのリンクを検知: {message.content}")
    output = message.content.replace("x.com", "vxtwitter.com")
    # Twitterの場合は普通に投稿する
    await message.channel.send(
      output,
      reference = message,
    )

client.run(TOKEN)