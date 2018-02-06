import sys
import random
import os
import discord

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

        if len(message.mentions) > 0:
            if message.mentions[0].id == '170383347497959425': #nerdwords
                if random.randint(0, 100) < 7: #im too lazy to make it a float for 6.9%
                    await client.send_message(message.channel, 'papa 🖐👁👄👁🖐')
            if message.mentions[0].id == '178682430566170624': #wspitfire
                if random.randint(0, 100) < 7:
                    await client.send_message(message.channel, 'mama 🖐👁👄👁🖐')

        if 'why are you sad' in message.content:
            await client.send_message(message.channel, 'because my parents never loved me')

        if '~df' in message.content:
            tokens = message.content.split(" ")
            if (len(tokens) == 2):
                dannyRole = message.server.get_member('183709274579533825').top_role
                if (dannyRole):
                    count = int(tokens[-1])
                    value = min(count, 100) #dont know how much we can spam chat before discord says no

                    fullMessage = ""
                    for _ in range(0, value):
                        fullMessage += (dannyRole.mention + "\n")

                    await client.send_message(message.channel, fullMessage)
                else:
                    await client.send_message(message.channel, 'He cannot be found...')

token = sys.argv[1]
client = MyClient()
client.run(token)
