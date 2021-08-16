import os # for importing env vars for the bot to use
from dotenv import load_dotenv
from twitchio.ext import commands
from keep_alive import keep_alive
from discord import Webhook, RequestsWebhookAdapter
webhook = Webhook.from_url("https://discord.com/api/webhooks/835720398963343460/bB3Ltwsn9gb57Qibp76c1oMJ7IDXWPClsxJybGR_9aW-tUBA0I_Y_24wIIWothbVZRiy", adapter=RequestsWebhookAdapter())
keep_alive()

load_dotenv()

bot = commands.Bot(
    # set up the bot
    irc_token=os.getenv('TMI_TOKEN'),
    client_id=os.getenv('CLIENT_ID'),
    nick=os.getenv('BOT_NICK'),
    prefix=os.getenv('BOT_PREFIX'),
    initial_channels=[os.getenv('CHANNEL')]
)

@bot.event
async def event_ready():
  print("Logged to Twitch successfully: ", bot.nick)

@bot.event
async def event_message(ctx):
  # print(f"[{ctx.author.name}] {ctx.content}")
  if ctx.content.startswith('[EN]') or ctx.content.startswith('[en]'):
    # print(f"[{ctx.author.name}] {ctx.content}")
    if ctx.author.name == 'kanbarukfp':
      # webhook.send(ctx.content, username = ctx.author.name, avatar_url = "https://static.miraheze.org/hololivewiki/thumb/0/00/Takanashi_Kiara_-_Portrait_Mini.png/290px-Takanashi_Kiara_-_Portrait_Mini.png")

#TO-DO LIST
#add webhook and keep_alive 
#to keep the bot running
#the stream start in 45m
#and i havent done anything


bot.run()