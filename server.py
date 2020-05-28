import requests
import discord
from datetime import datetime
import random
from discord.utils import get
from discord.ext import commands
bot = commands.Bot(command_prefix="!!!")
messagedate = {}
messaged = {}

token = "TOKEN" #(str)
channel_log = ID_CHANNEL #(int)

@bot.event
async def on_message_edit(before, after):
    print(str(before.id))
    try:
      messageinfos = messagedate.get(str(before.id))
      messagegot = messaged.get(str(before.id))
      differencein = messageinfos - datetime.utcnow()
      ct = differencein.total_seconds()
      if ct < 315:
          tc = bot.get_channel(channel_log)
          if tc is not None:
              if before.author.bot:
                  return
              for splitter in before.content.split(" "):
                for splitter2 in after.content.split(" "):
                  if splitter == splitter2:
                    return
              await tc.send(content=None, embed=discord.Embed(title="Ghostping detection (EDIT)", description=f"Ghostping détécté pour <@{before.author.id}>\n\n**Message (new)**\n{after.content}\n**Message (old)**\n{messagegot  }", color=discord.Color.red()))
              role = get(before.author.guild.roles, name="Muted")
              await before.author.add_roles(role)
    except:
      pass
@bot.event
async def on_message_delete(message):
    try:
      messageinfos = messagedate.get(str(message.id))
      messagegot = messaged.get(str(message.id))
      differencein = messageinfos - datetime.utcnow()
      ct = differencein.total_seconds()
      if ct < 315:
          tc = bot.get_channel(channel_log)
          if tc is not None:
              if message.author.bot:
                  return
              await tc.send(content=None, embed=discord.Embed(title="Ghostping detection", description=f"Ghostping détécté pour <@{message.author.id}>\n\n**Message**\n{messagegot}", color=discord.Color.green()))
              role = get(message.author.guild.roles, name="Muted")
              await message.author.add_roles(role)
    except:
      pass
@bot.event
async def on_message(message):
    global messagedate
    if "<@" not in message.content:
        return
    messagedate[str(message.id)] = datetime.utcnow()
    messaged[str(message.id)] = message.content

bot.run(token)
