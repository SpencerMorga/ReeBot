import discord
import random
import sys
import os

class MyClient(discord.Client):
    async def on_ready(self):
        print('Mother give me tendies')

    async def on_message(self, message):
        if message.mention_everyone:
            await client.send_file(message.channel, str(random.choice(os.listdir("""./pics"""))))
        if message.mentions[0].id == '170383347497959425':
            await client.send_message(message.channel, 'papa 🖐👁👄👁🖐')
        if message.mentions[0].id == '178682430566170624':
            await client.send_message(message.channel, 'mama 🖐👁👄👁🖐')

token = sys.argv[1]
client = MyClient()
client.run(token)