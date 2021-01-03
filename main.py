import discord
import asyncio
import ffmpeg
from discord.ext import commands
from discord.voice_client import VoiceClient

bot = discord.Client()
bot = commands.Bot(command_prefix = '$')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has logged into discord.')

@bot.command(name = 'hello', help = 'Tells the bot hello!')
async def hello(ctx):
    await ctx.send('Hello!')

@bot.command(name = 'join', help = 'Tells the bot to join the current voice channel.')
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@bot.command(name = 'leave', help = 'Tells the bot to leave the current voice channel.')
async def leave(ctx):
    await ctx.voice_client.disconnect()

@bot.command(name = 'clap', help = 'Tells the bot to play an audience clap sound track.')
async def clap(ctx):
    source = r'C:\Users\Johnn\Downloads\Eric_Andre_Clap.mp3'
    VoiceClient.play(source, after = None)
   

bot.run('Nzk0MzkzMjg4OTEyMjczNDE4.X-6KZw.bGjvpqATKCUxEhVWP-6HjD-DT_Y')