import sys
import random
import os
import discord
import re
import asyncio
import config
import atexit
import datetime
now = datetime.datetime.now()

def on_exit():
    log_file.close()

def is_me(m):
        return m.author == client.user

class MyClient(discord.Client):
    async def on_ready(self):
        print('Mother give me tendies')

    async def on_message(self, message):

        #everyone tagged
        if message.mention_everyone:
            print('everyone was tagged, sending pic')
            images = os.listdir("""./pics""")
            imagePath = './pics/' + str(random.choice(images))
            await client.send_file(message.channel, imagePath)

        #twitch link
        if 'twitch.tv/' in message.content: #shameless promo
            print('twitch was tagged')
            await client.send_message(message.channel, 'shameless self promo')

        if len(message.mentions) > 0:
            print(message.mentions[0].name + ' was mentioned')
            if message.mentions[0].id == config.user_nerdwords:
                if random.randint(0, 100) < 7: #im too lazy to make it a float for 6.9%
                    await client.send_message(message.channel, 'papa 🖐👁👄👁🖐')
            if message.mentions[0].id == config.user_spitfire:
                if random.randint(0, 100) < 7:
                    await client.send_message(message.channel, 'mama 🖐👁👄👁🖐')
            if message.mentions[0].id == config.user_krissi:
                if random.randint(0, 1000) < 10:
                    await client.send_message(message.channel, 'fuck u')

        #debug response
        if 'why are you sad' in message.content:
            print('ree is sad')
            await client.send_message(message.channel, 'because my parents never loved me')
        
        if 'reddit.com/r/' in message.content
            await client.send_message(message.channel, 'Thats my fave subreedit 😎')
        
        #ree commands
        if message.content.startswith('~'):
            print('command entered')
            tokens = message.content.split(" ")

            #spam command
            if(tokens[0] == "~spam"):
                if (len(tokens) == 3 and re.match(r"^<@(\d+)>$",tokens[1]) and tokens[2].isdigit()):
                    user = await client.get_user_info(tokens[1][2:-1])
                    if(user):
                        count = abs(int(tokens[2]))
                        value = min(count, 25)
                        for _ in range(0, value):
                            await client.send_message(message.channel, user.mention)
                    else:
                        await client.send_message(message.channel, 'error: user not found')
                else:
                    await client.send_message(message.channel, 'usage: ~spam @User tagCount')
            
            #clear command
            if(tokens[0] == "~clear" and len(tokens) == 1):
                async for x in client.logs_from(message.channel, limit=1000):
                    if is_me(x):
                        await client.delete_message(x)
                        await asyncio.sleep(1.2)

token = sys.argv[1]
log_file = open(now.strftime("%Y-%m-%d"), "a")
sys.stdout = log_file
atexit.register(on_exit)
client = MyClient()
client.run(token)
