import os
import discord
from serverstatus import get_server_status
from patchnotes import most_recent_notes

my_secret = open("token.txt", 'r').readline()


client = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('New World | Type "!q" for server status'))
    print('Bot ready {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!help"):
        await message.channel.send("Type !q to get a list of stats for our server.\n Type !patch for latest patch notes")

    if message.content.startswith("!q"):
        status = get_server_status()
        await message.channel.send(status)

    if message.content.startswith("!patch"):
        options = ['url', 'title', 'desc', 'date', 'img']
        tupl = most_recent_notes(*options)
        # image = str(tupl[4])
        # print(image)
        embed = discord.Embed(
            title=f"{tupl[1].upper()}", description=f"", color=0x7030a0)
        embed.add_field(
            name=tupl[3], value=f"{tupl[2]}[Read More]({tupl[0]})", inline=True)
        embed.set_image(url=tupl[4])
        await message.channel.send(embed=embed)

client.run(my_secret)
