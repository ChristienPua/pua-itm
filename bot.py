# Hi sir, it appears I can not upload my token on the internet otherwise discord will automatically renew it. So for now, this code is not connected to my bot
import discord, datetime, asyncio, apscheduler, youtube_dl, os
from discord.ext import tasks, commands
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from datetime import datetime

bot = commands.Bot(command_prefix='.') # states bot prefix to be a period
token = 'OTk2NDQ2NTE3NDM3MTU3NDM2.GsNpla.cG4e2IR5fGQPtM28yGwyRmgJ3mMMzS0lee9CR4' # the bots token so it knows to run which code on which file

async def goodmorning(): 
    channel = bot.get_channel(996447915549655154)
    await channel.send('Good morning @everyone!') # bot sends this message when called

async def lunch():
    channel = bot.get_channel(996447915549655154)
    await channel.send('Lunch break @everyone!') # bot sends this message when called

async def end():
    channel = bot.get_channel(996447915549655154)
    await channel.send('Good work @everyone! See you tomorrow!') # bot sends this message when called

@bot.event
async def on_ready(): # clauses for trigger
    scheduler = AsyncIOScheduler() # note that discord server times may be delayed from computer time (good morning may appear as 8:59am on discord)
    scheduler.add_job(goodmorning, CronTrigger(hour=8, minute=0),) # triggers the goodmorning function when it is 9am
    scheduler.add_job(lunch, CronTrigger(hour=12, minute=0)) # triggers the lunch function when it is 12pm
    scheduler.add_job(end, CronTrigger(hour=17, minute=0)) # triggers the end function when it is 5pm
    scheduler.start()

@bot.command()
async def meeting(ctx, user : str, timevar : int): # defines command ".meeting" followed by a user/role and a fixed time (in hours)
    await asyncio.sleep(timevar * 3600) # bot waits timevar * 3600 seconds to send message below, 3600s just means timevar is in hours
    await ctx.reply('Meeting happening now,' + ' ' + user) # sends this message

@bot.command()
async def time(ctx): # simply returns the current time
    now = datetime.now()
    current_time = now.strftime('%H:%M')
    await ctx.send(current_time)

@bot.command()
async def play(ctx, url : str): # plays the youtube url included in the message
    song = os.path.isfile("song.mp3") # song is equated to the file "song.mp3"
    try:
        if song:
            os.remove("song.mp3") # if the file already exists, remove it
    except PermissionError:
        await ctx.send("Use .stop or .leave") # bot will send this message if a song is already playing
        return

    vc = discord.utils.get(ctx.guild.voice_channels, name='General') # gets the voice channel named "General"
    await vc.connect() # joins general
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild) # voice clients, it grants our bot permissions while in the voice channel

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl: # ydl_opts holds the key values for specifications in downloading the url with youtube_dl
        ydl.cache.remove() # resets cache, i had problems with cache after multiple usage with the bpt
        ydl.download([url]) # downloads the url according to the specifications in ydl_opts
    for file in os.listdir("./"): # directory for downloading
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3") # renames audio file to "song.mp3"
    voice.play(discord.FFmpegPCMAudio("song.mp3")) # plays "song.mp3" with voice granting it permission with voice_clients

@bot.command()
async def leave(ctx): # makes the bot leave the voice channel
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild) # voice clients
    if voice.is_connected():
        await voice.disconnect() # disconnects bot

@bot.command()
async def stop(ctx): # stops current song playing
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild) # voice clients
    voice.stop() # stops audio

bot.run(token) # runs the bot in the specified server token
