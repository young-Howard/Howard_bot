# A id 829086651379875889
# public key 5776288308f096645768b39539c99285b34d98f7d8af1b6fbc8b8cf06f795a80
# Token ODI5MDg2NjUxMzc5ODc1ODg5.YGzBHQ.fbimYqbXqV3X5NWUIAQGLLOuKxw
# perms int 75840
# https://discordapp.com/oauth2/authorize?client_id=829086651379875889&scope=bot&permissions=75840

from discord.ext import commands
import random
import discord

client = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='out for your commands!'))
    print(f"We have logged in as {client.user}")
@client.event
async def on_message(message):
    print (f"{message.channel}:{message.author}:{message.author.name}:{message.content}")


    if "_help" in message.content.lower():
        await message.channel.send("-note that must be behind all of the commands in order for them to be noticed by Howard_bot\n-leave, will disconnect the bot\n-play, will be a 1-2 guessing game")

    if "retard" in message.content.lower():
        await message.channel.send("not nice :(")

    if "_leave" in message.content.lower():
        await message.channel.send("bye!!")
        await client.close()

    if str(message.author) == "Young_Howard#5726" and "" in message.content.lower():
        await message.channel.send('Hi howard!')

    if message.content.startswith("_play"): 
        channel = message.channel
        await channel.send("Choose a number between 1-2. Enter numerical values only.") 

    number1 = random.randint(1,2)        
    number2 = str(number1)


    def check(m):
        return m.content == number2 and m.channel == channel 
        
    msg = await client.wait_for('message', check=check) 
    await channel.send("Correct answer {.author}" .format(msg)) 


client.run("ODI5MDg2NjUxMzc5ODc1ODg5.YGzBHQ.fbimYqbXqV3X5NWUIAQGLLOuKxw")
