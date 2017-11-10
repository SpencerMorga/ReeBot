import discord
import random

class MyClient(discord.Client):
    async def on_ready(self):
        print('Mother give me tendies')

    async def on_message(self, message):
        if(message.mention_everyone):
            await client.send_file(client.get_channel('301575084630343681'), random.choice(['a.jpg','b.jpg','c.jpg','d.jpg','e.jpg','f.jpg','g.gif']))

client = MyClient()
client.run('Mzc4NDI3MTQ3MzkzNTY0Njgz.DObZeA.A03xbIdbAKHMovgMxYsYoc6EILk')