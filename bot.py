import discord
import random
import simple_text_gen

token = open("token.txt", "r").read()

generator = simple_text_gen.SimpleTextGen("reddit_comments.txt", 50)

client = discord.Client()  # starts the discord client.

converse = False
channel = None


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    chance = random.randrange(100)
    global converse, channel
    if message.content.startswith("&reset"):
        print("resetting tf session")
        generator.reset()
        await message.channel.send("Session Reset")
    # responds by chance or by summon
    if (chance <= 5 or message.content.startswith("&talk")):
        if message.author.bot:
            return
        async with message.channel.typing():
            userinput = message.content.replace("&talk ", "")
            generator.talk(userinput[:50], 1.15)
            generator.fileFormat()
            response = open("bot_says.txt", "r").read()
            print(
                f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
            await message.reply(response, mention_author=False)
    if not converse and message.content.startswith("&say"):
        async with message.channel.typing():
            await message.channel.send(message.content.replace("&say ", ""))
    if message.content.startswith("&convo"):
        converse = True
        channel = message.channel.id
        return
    if converse and message.author != client.user and channel == message.channel.id:
        if message.content.startswith("&stop"):
            converse = False
            return
        async with message.channel.typing():
            generator.talk(message.content[:50])
            generator.fileFormat()
            response = open("bot_says.txt", "r").read()
            print(
                f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
            await message.reply(response, mention_author=False)

client.run(token)
