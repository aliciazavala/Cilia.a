from random import randint
import random
import discord 
import asyncio
from discord.ext import commands

# A bot for use with Discord 
# Prefix and bot Description
bot = discord.Client()
bot = commands.Bot(command_prefix='!', description="A bot to handle Daniel's memes and dice rolls")

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

    #check if message is an attatchment not sent to the memes channel 
    if message.attachments :
        if message.channel.name.find('memes') == -1:
            await message.author.send("better not be a meme.",file=discord.File(r'./images/shooter.png'))
    
    # check the omg and add to voice channel
    if (message.content.find('omg') != -1 or message.content.find('OMG') != -1):
        if(message.author.voice.channel is not None):
            vc = await message.author.voice.channel.connect()
            vc.play(discord.FFmpegPCMAudio(source='sounds/ohmygot.mp3'))
            print(message.author.voice.channel)
        else:
            print("not")
       
        #else:
           #print("You're not in a voice channel or you're connected to a channel which I can't access.")

        

    # if the user is the client user itself, ignore the message
    if user == bot.user:
        return

    # check if the message is a command 
    await bot.process_commands(message) 


    # DELETE LATER. JUST TO DEBUG SHIT   
    print(user, message.channel, content)


bot.run(inserToken)
