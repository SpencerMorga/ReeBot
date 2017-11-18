import discord
import random
import sys
import os

class MyClient(discord.Client):
    async def on_ready(self):
        print('Mother give me tendies')

    async def on_message(self, message):
        if message.mention_everyone:
            await client.send_file(message.channel, random.choice(os.listdir("""./pics""")))
        if message.content.startswith('@NerdWords#9998'):
            await client.send_message(message.channel, 'papa 🖐👁👄👁🖐')
        if message.content.startswith('@wSpitfire#0344'):
            await client.send_message(message.channel, 'mama 🖐👁👄👁🖐')

token = sys.argv[1]
client = MyClient()
client.run(token)