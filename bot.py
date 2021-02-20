from random import randint
import random
import discord 
import asyncio
import time
import string
import statistics
from discord.ext import commands

# A bot for use with Discord 
# Prefix and bot Description
bot = discord.Client()
bot = commands.Bot(command_prefix='!', description="A bot to handle Daniel's memes and dice rolls")


inGame = True
randNumb = 0
lst = []

#constants
def is_me(m):
    return m.author == bot.user

@bot.event
async def on_ready(): 
    print('Loading...')
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

#commands
@bot.command(aliases=['8ball'])
async def magic8ball(ctx, *, question):
    responses = [ 'As I see it, yes.',
                'Ask again later.',
                'Better not tell you now.',
                'Cannot predict now.',
                'Don’t count on it.',
                'It is certain.',
                'It is decidedly so.',
                'Most likely.',
                'My reply is no.',
                'My sources say no.',
                'Outlook not so good.',
                'Outlook good.',
                'Reply hazy, try again.',
                'Signs point to yes.',
                'Very doubtful.',
                'Without a doubt.',
                'Yes.',
                'Yes – definitely.',
                'You may rely on it' ]
    await ctx.send(f'{random.choice(responses)} :8ball:')

@bot.command(description='Deletes all messages the bot has made')
async def clear(ctx):
    await ctx.channel.purge(limit=100, check=is_me)

#reads all messages and finds the roll command
@bot.event
async def on_message(message):
    # this is the string text message of the Message
    content = message.content

    # this is the sender of the Message
    user = message.author
    
    # this is the channel of there the message is sent
    channel = message.channel

################################################################################################################################################################################################################    
    '''if inGame == True:
        if message.content.startswith("!stop"):
            closestNum = lst[min(range(len(lst)), key = lambda i: abs(lst[i]-randNumb))]
            await channel.send("Closest number is.....")
            time.sleep(1)
            await channel.send(closestNum)
            inGame = False
            return
        try:
            lst.append(int(message.content))
        except:
            return'''
    #check if message is an attatchment not sent to the memes channel 
    if message.attachments :
        if (message.channel.name.find('memes') == -1 and message.channel.name.find('stonks') == -1 and message.channel.name.find('create') == -1):
            await message.author.send("better not be a meme.",file=discord.File(r'./images/shooter.png'))
################################################################################################################################################################################################################    
    # check the omg and add to voice channel
    elif (message.content.find('omg') != -1 or message.content.find('OMG') != -1 or message.content.find('Omg') != -1):
        if(message.author.voice.channel is not None):
            vc = await message.author.voice.channel.connect()
            time.sleep(float(random.randrange(1, 300))/100)
            vc.play(discord.FFmpegPCMAudio(executable ='C:/FFmpeg/bin/ffmpeg.exe' ,source='C:/Users/adenr/Desktop/Cilia.a-main/sounds/ohmigot.mp3'))
            print(message.author.voice.channel)
        else:
            print("not")
        while vc.is_playing(): 
            time.sleep(.1)
        await vc.disconnect()

    elif message.content.startswith("!guess"):
        try:
            numb = int(message.content[7:])
        except:
            return
        randNum = random.randrange(1,numb)
        msg = "I'm thinkin of a number between 1 and" + str(numb)
        await channe.send(msg)
################################################################################################################################################################################################################      
    elif(message.content.startswith("!")) and message.content.startswith("!8ball") != True :
        tempString = message.content[1:] # Cuts off the exclamation point
        numbs = tempString.split("d", 1) # Splits the string into an array seperated by the d "1d4"
        try:                             
            S = int(numbs[1]) #sides of dice   #makes sure inputs are integers, otherwise omigot
            N = int(numbs[0]) #number of dice
        except:
            return
        print(S)
        print(N)
        if S != 0 and N != 0: #checks if inputs are 0, if so omigot
            rolls = []
            for x in range(N):    #generic dice rolling function
                roll = random.randrange(1,S)
                rolls.append(roll)
                
            msg = "Average = " + str(statistics.fmean(rolls))    
            await channel.send(rolls)
            await channel.send(msg)
        else:
            await channel.send("Ohmigot")
            return
    
################################################################################################################################################################################################################
    # if the user is the client user itself, ignore the message
    if user == bot.user:
        return

    # check if the message is a command 
    await bot.process_commands(message) 


    # DELETE LATER. JUST TO DEBUG SHIT   
    print(user, message.channel, content)


bot.run()
