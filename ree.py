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
            if random.randint(0,100) < 7: #im too lazy to make it a float for 6.9%
                await client.send_message(message.channel, 'papa 🖐👁👄👁🖐')
        if message.mentions[0].id == '178682430566170624': #wspitfire
            if random.randint(0,100) < 7:
                await client.send_message(message.channel, 'mama 🖐👁👄👁🖐')
        if 'why are you sad' in message.content:
            await client.send_message(message.channel, 'because my parents never loved me')
        if '~df -n' in message.content:
            tokens = message.content.split(" ")
            if (len(tokens) == 3):
                count = int(tokens[-1])
                value = min(count, 100) #dont know how much we can spam chat before discord says no
                for i in range(0, value):
                    await client.send_message(message.channel, '@Daniel Favela')

token = sys.argv[1]
client = MyClient()
client.run(token)