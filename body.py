import discord
import os
import requests
import json
from discord.ext import commands
from keep_alive import keep_alive

my_secret = os.environ['TOKEN']

bot = commands.Bot(command_prefix='$')

client = discord.Client()

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)


@client.event
async def on_ready():
    print('we have logged in as{0.user}'.format(client))


@client.event
async def on_message(message):
    contents=message.content
    if message.author == client.user:
        return
      

    if message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)
    if message.content.startswith('$shiyana'):
        await message.channel.send(
            "Shiyana AKA Purple/MOJO JOJO.The Writer, The poet,The Free thinker!.Welcome shiyaaa!!"
        )
    if message.content.startswith("$alan"):
        await message.channel.send(
            "Alan. Aka the Creator. the Alpha and Omega of this bot. Welcome!!"
        )
    if message.content.startswith("$arun"):
        await message.channel.send(
            "Arun! AKA The banker/Hacker.Please dont hack me.Welcome!!"
        )
    if message.content.startswith("$ammu"):
        await message.channel.send(
            "Kommu!! Sorry, Ammu!!! aka Mrs udayipp/Mrs T. The Queen of all udayipps. Taliban is better than her wrath.Welcome!!!"
        )


keep_alive()
client.run(my_secret)
