import praw
import discord
from airtable import Airtable
from airtable.__version__ import __version__
from discord_webhook import DiscordWebhook, DiscordEmbed
import os
discord_key = os.getenv('discord_key')
reddit = praw.Reddit(client_id='1Y_dnEC6Xrlpbw', client_secret='c2kHQgaKNxdRkLorcRrcRzuk8YYaIw', user_agent='forhireScrape')
subreddit = reddit.subreddit('forhire+slavelabour+designjobs+hireawriter+jobbit')
hot_posts = subreddit.new(limit=10)
airtable = Airtable('appWlcYj2idOcJ30G', 'keys', 'keyWgEI0t7Z6TXkog')


client = discord.Client()
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print(client.get_channel(803027917512638485))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


    if message.content.lower().startswith("inv"):
        invite = await client.get_channel(803027917512638485).create_invite(max_uses=1)
        airtable.insert({'key': str(invite)})
        await client.get_channel(803027917512638485).send(f"Here's your invite: {invite}")




            


client.run(discord_key)


