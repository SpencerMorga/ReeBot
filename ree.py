import discord
import random
import sys
import os

class MyClient(discord.Client):
    async def on_ready(self):
        print('Mother give me tendies')

    async def on_message(self, message):
        if message.mention_everyone:
            images = os.listdir("""./pics""")
            imagePath = './pics/' + str(random.choice(images))
            await client.send_file(message.channel, imagePath)
        if 'https://www.twitch.tv/' in message.content: #shameless promo
            await client.send_message(message.channel, 'shameless self promo')
        if message.mentions[0].id == '170383347497959425': #nerdwords
            await client.send_message(message.channel, 'papa 🖐👁👄👁🖐')
        if message.mentions[0].id == '178682430566170624': #wspitfire
            await client.send_message(message.channel, 'mama 🖐👁👄👁🖐')

token = sys.argv[1]
client = MyClient()
client.run(token)