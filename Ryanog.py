import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random

Client = discord.Client()
bot_prefix= ">"
client = commands.Bot(command_prefix=bot_prefix)

@client.command(pass_context=True)
async def Ryanog(ctx):
    
    meme = ['ryan1.jpg','ryan2.jpg','ryan3.jpg','ryan4.jpg','ryan5.jpg','ryan6.jpg','ryan7.jpg','ryan8.jpg','ryan9.jpg','ryan10.png','ryan11.png','ryan12.png','ryan13.jpg','ryan14.jpg']
    await client.send_file(client.get_channel('326622983789608960'), random.choice(meme))

client.run("MzM2MjU1OTI0NzMxNzcyOTI4.DE1qVQ.6HedKTgcOfJRZShItG-7jBCIbF8")
