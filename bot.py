import discord

token = ""
text = []

with open ('token.txt', 'rt') as myfile:  # Open lorem.txt for reading
    for mytoken in myfile:
        text.append(mytoken)
        token = text[0]



client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('your token here')