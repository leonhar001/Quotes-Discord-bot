import discord
import config
from quotes import Quotes

TOKEN = config.token
quotes = Quotes()

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_read():
    print('User {0.user}'.format(client))

@client.event
async def on_message(message):
    targetUser = str(message.author).split('#')[0]
    userMessage = str(message.content)
    channel = str(message.channel.name)
    print(f'{targetUser}: {userMessage} ({channel})')

    if message.author == client.user:
        return
    if userMessage.lower() == '!fact':
        await message.channel.send(quotes.getQuote())

client.run(TOKEN)