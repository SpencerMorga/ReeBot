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

        if 'twitch.tv/' in message.content: #shameless promo
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

        if '~spam' in message.content:
            tokens = message.content.split(" ")
            if (len(tokens) == 3 and len(message.mentions) > 0):
                user = await client.get_user_info(tokens[1][2:-1])
                if(user):
                    count = int(tokens[2])
                    value = min(count, 25)
                    for _ in range(0, value):
                        await client.send_message(message.channel, user.mention)
                else:
                    await client.send_message(message.channel, 'error: user not found')
            else:
                await client.send_message(message.channel, 'usage: ~spam @User tagCount')

token = sys.argv[1]
client = MyClient()
client.run(token)
