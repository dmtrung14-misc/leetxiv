from github import Github
from discord import ui, app_commands
from datetime import datetime
import github
import requests
import random
import discord
import os
import pathlib
from dotenv import load_dotenv

# Get parent folder path
parent_path = pathlib.Path(__file__).parent.parent

# Load .env file from parent folder
dotenv_path = parent_path / ".env"
load_dotenv(dotenv_path)
g = Github(os.getenv("GITHUB_TOKEN"))
repo = g.get_organization("LeetXiv").get_repo("archive")

def github_path_exists(object_path: str) -> bool:
    try:
        repo.get_contents(object_path)
        return True
    except github.UnknownObjectException:
        return False

def help_():
    header = "LeetXiv Bot - Your LeetCode co-pilot on Discord"
    commands = "**Commands**\n1.`\push`:Push a new solution\n2.`update`: update existsing solution\n3.`delete`:delete existing solution\n4.`retrieve`: retrieve existing solution\n5.`gimme`: suggest a random Leetcode problem\n6.`timer`:set timer for problem solving\n"
    personal = "LeetXiv is created by Trung Dang @dmtrung14. Please visit the code at github.com/dmtrung14/leetxiv"
    contribution = "Contributions are welcomed. Please submit contributions and feature requests as outlined in CONTRIBUTION.md"
    footer = "© Trung Dang 2023. Made with love ❤️"
    return "\n".join([header, commands, personal, contribution, footer])