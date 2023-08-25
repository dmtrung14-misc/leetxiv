import asyncio
import discord
import random
import os
from github import Github
from discord import ui, app_commands
from datetime import datetime
from .helper import github_path_exists
from dotenv import load_dotenv
import pathlib

# Get parent folder path
parent_path = pathlib.Path(__file__).parent.parent

# Load .env file from parent folder
dotenv_path = parent_path / ".env"
load_dotenv(dotenv_path)


class push_modal(ui.Modal, title="Push your code here"):
    language = ui.TextInput(label="Language", style=discord.TextStyle.short, default="py", required=True)
    problem = ui.TextInput(label="Problem", style=discord.TextStyle.short, required=True)
    code = ui.TextInput(label="Code", style=discord.TextStyle.paragraph,placeholder="Write your code here", required=True)

    async def on_submit(self, interaction: discord.Interaction):
        g = Github(os.getenv("GITHUB_TOKEN"))
        repo = g.get_repo("dmtrung14/leetcode_arxiv")
        filename=f'{self.problem}.{self.language}'
        message= f"Created solution for {self.problem}"
        content=f"{self.code}"
        try:
            repo.create_file(path=filename, message=message, content=content, branch="main")
            embed = discord.Embed(title=self.title, description =f"File {self.problem}.{self.language} created successfully", timestamp = datetime.now(), color = discord.Colour.blue())
            embed.set_author(name = interaction.user, icon_url = interaction.user.avatar)
            await interaction.response.defer()
            await asyncio.sleep(10)
            await interaction.followup.send(embed = embed, ephemeral=True)
        except:
            embed = discord.Embed(title=self.title, description =f"Cannot commit {self.problem}.{self.language}. File either already exists or permission denied.", timestamp = datetime.now(), color = discord.Colour.blue())
            embed.set_author(name = interaction.user, icon_url = interaction.user.avatar)
            await interaction.response.send_message(embed=embed, ephemeral=True)

class update_modal(ui.Modal, title="Update your solution here"):
    language = ui.TextInput(label="Language", style=discord.TextStyle.short, default="py", required=True)
    problem = ui.TextInput(label="Problem", style=discord.TextStyle.short, required=True)
    code = ui.TextInput(label="Code", style=discord.TextStyle.paragraph,placeholder="Write your code here", required=True)

    async def on_submit(self, interaction: discord.Interaction):
        g = Github(os.getenv("GITHUB_TOKEN"))
        repo = g.get_repo("dmtrung14/leetcode_arxiv")
        filename = f"{self.problem}.{self.language}"
        content = f"{self.code}"
        # Check if file exists
        if github_path_exists(filename):
            message = f"Updated solution to {self.problem}"
            try:
                repo.update_file(path=filename, message=message, content=content, sha=repo.get_contents(filename).sha)
                embed = discord.Embed(description=f"File {filename} updated successfully")
                await interaction.response.defer()
                await asyncio.sleep(10)
                await interaction.followup.send(embed = embed, ephemeral=True)
            except:
                embed = discord.Embed(description=f"Error updating file {filename}")
                await interaction.response.send_message(embed=embed, ephemeral=True)
        else:
            message = f"Created solution to {self.problem}."
            try:
                repo.create_file(path=filename, message=message, content=content, branch="main")
                embed = discord.Embed(title=self.title, description =f"Solution to {self.problem} not found, created a new one instead!", timestamp = datetime.now(), color = discord.Colour.blue())
                embed.set_author(name = interaction.user, icon_url = interaction.user.avatar)
                await interaction.response.defer()
                await asyncio.sleep(10)
                await interaction.followup.send(embed = embed, ephemeral=True)
            except:
                embed = discord.Embed(title=self.title, description =f"Cannot commit {self.problem}.{self.language}. File either already exists or permission denied.", timestamp = datetime.now(), color = discord.Colour.blue())
                embed.set_author(name = interaction.user, icon_url = interaction.user.avatar)
                await interaction.response.send_message(embed=embed, ephemeral=True)

class delete_modal(ui.Modal, title="Remove a solution here!"):
    language = ui.TextInput(label="Language", style=discord.TextStyle.short, default="py", required=True)
    problem = ui.TextInput(label="Problem", style=discord.TextStyle.short, required=True)
    code = ui.TextInput(label="Code", style=discord.TextStyle.paragraph,placeholder="Write your code here", required=True)

    async def on_submit(self, interaction: discord.Interaction):
        g = Github(os.getenv("GITHUB_TOKEN"))
        repo = g.get_repo("dmtrung14/leetcode_arxiv")
        filename = f"{self.problem}.{self.language}"
        if github_path_exists(filename):
            message = f"Removed solution to {self.problem}"
            try:
                repo.update_file(path=filename, message=message, sha=repo.get_contents(filename).sha)
                embed = discord.Embed(description=f"File {filename} deleted successfully")
                await interaction.response.defer()
                await asyncio.sleep(10)
                await interaction.followup.send(embed = embed, ephemeral=True)
            except:
                embed = discord.Embed(description=f"Error deleting file {filename}")
                await interaction.response.send_message(embed=embed, ephemeral=True)
        else:
            embed = discord.Embed(title=self.title, description =f"File {self.problem}.{self.language} does not exists. Double check if this is the correct path to the solution", timestamp = datetime.now(), color = discord.Colour.blue())
            embed.set_author(name = interaction.user, icon_url = interaction.user.avatar)
            await interaction.response.send_message(embed=embed, ephemeral=True)

def retrieve(problem:str, language:str):

    g = Github(os.getenv("GITHUB_TOKEN"))
    repo = g.get_repo("dmtrung14/leetcode_arxiv")
    filename = f"{problem}.{language}"
    if github_path_exists(filename):
        return "```python\n" + repo.get_contents(filename).decoded_content.decode("utf-8") + "\n```"
    else:
        return "File not found"
