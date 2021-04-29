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
        await message.channel.send("-note _ that must be behind all of the commands in order for them to be noticed by Howard_bot\n-leave, will disconnect the bot\n-play, will be a 1-2 guessing game")

    if "retard" in message.content.lower():
        await message.channel.send("not nice :(")

    if "_leave" in message.content.lower():
        await message.channel.send("bye!!")
        await client.close()

    if str(message.author) == "" and "" in message.content.lower():
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

    def check(m):
        return m.content == number2 and m.channel == channel 

    msg2 != await client.wait_for('message', check=False) #waits for the check function to return true
    await channel.send("wrong {.author}" .format(msg2)) #sends the correct answer message



client.run("")
