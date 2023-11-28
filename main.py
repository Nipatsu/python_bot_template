from discord.ext import commands
import os
import discord

from keep_alive import keep_alive

keep_alive()

token = os.getenv("token")

intents = discord.Intents.all()
intents.members = True
intents.messages = True
client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    activity = discord.Activity(
        type=discord.ActivityType.watching,
        name="test"
    )
    await client.change_presence(activity=activity)
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')

client.run(token)
