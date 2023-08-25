import asyncio
import discord
import random
import os
from github import Github
from discord import ui, app_commands
from datetime import datetime
from modules import push_modal, update_modal, delete_modal, random_problem, retrieve, fortune_teller, help_
from termcolor import colored
from dotenv import load_dotenv

load_dotenv()



class aClient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.all())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild=discord.Object(id=1144327924875542548))
            # await tree.sync()
            self.synced = True
        print(f"We have logged in as {self.user}")

guilds=[discord.Object(id=1144327924875542548)]
client = aClient()
tree = app_commands.CommandTree(client)
intents = discord.Intents.all()

sad_word = ['sad', 'tired', 'depressed']
motivational = ['hang on', 'come on', 'you can do it!']




@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if message.content.startswith('\hello'):
        await message.channel.send('Hello')

    if any(word in sad_word for word in msg.split()):
        await message.channel.send(random.choice(motivational))
# @tree.command(name="test", description="test", guilds= guilds)
@tree.command(name="test", description="sanity check if the leetxiv is here", guild=discord.Object(id = 1144327924875542548))
async def self(interaction: discord.Interaction, name:str):
    await interaction.response.send_message(f"Hello {name}! I was made with Discord.py", ephemeral=True)

@tree.command(name="push", description="push new solution to github archive", guild=discord.Object(id=1144327924875542548))
async def self(interaction: discord.Interaction):
    await interaction.response.send_modal(push_modal())

@tree.command(name="update", description="edit available solution or create a new one", guild=discord.Object(id=1144327924875542548))
async def self(interaction: discord.Interaction):
    await interaction.response.send_modal(update_modal())

@tree.command(name="delete", description="edit available solution or create a new one", guild=discord.Object(id=1144327924875542548))
async def self(interaction: discord.Interaction):
    await interaction.response.send_modal(delete_modal())

@tree.command(name="retrieve", description="retrieve an existing solution", guild=discord.Object(id=1144327924875542548))
async def self(interaction: discord.Interaction, problem:str, language:str):
    await interaction.response.send_message(f"{retrieve(problem=problem, language=language)}")

@tree.command(name="gimme", description="get random problem from leetcode list", guild=discord.Object(id=1144327924875542548))
async def self(interaction: discord.Interaction, difficulty:str):
    random_prob, difficulty = random_problem(difficulty)
    description=f"Total Submitted:   {random_prob['total_submitted']} \n Total Accepted:    {random_prob['total_acs']} \n Difficulty:    {difficulty}"
    random_url = f'https://leetcode.com/problems/{random_prob["question__title_slug"]}/'
    embed = discord.Embed(title=random_prob['question__title'], description=description, url=random_url)
    embed.set_thumbnail(url="https://leetcode.com/static/images/LeetCode_logo_rvs.png")
    await interaction.response.send_message(embed=embed)

@tree.command(name="timer", description="get disciplined!", guild=discord.Object(id=1144327924875542548))
async def self(interaction: discord.Interaction, name:str, hours:int=0, minutes:int=0):
    time = hours*3600 + minutes*60
    await interaction.response.send_message(f'Timer {name} set for {hours} hours and {minutes} minutes')
    await asyncio.sleep(time)
    await interaction.followup.send(f'Time is up for task name {name}')


@tree.command(name="help", description="i'm here to help", guild=discord.Object(id=1144327924875542548))
async def self(interaction: discord.Interaction):
    await interaction.response.send_message(f'{help_()}')


@tree.command(name="fortune", description="guess what? I'm a fortune teller too 🫣", guild=discord.Object(id=1144327924875542548))
async def self(interaction: discord.Interaction):
    await interaction.response.send_message(f'of all Fortune 500 companies you matched with: {fortune_teller()}')



client.run(os.getenv("DISCORD_TOKEN"))
