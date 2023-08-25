import random
import os
import discord
from github import Github
from discord import ui, app_commands
from datetime import datetime
import requests
import random

BASE_URL = "https://leetcode.com/api/problems/all/"

def random_problem(difficulty=None):
    diff_dict = {'easy' : 1, 'medium': 2, 'hard' : 3}
    response = requests.get(BASE_URL)
    data = response.json()
    problems = data['stat_status_pairs']

    if difficulty:
        problems = [p for p in problems if p['difficulty']["level"] == diff_dict[difficulty]]
    random_index = random.randint(0, len(problems)-1)

    difficulty = problems[random_index]["difficulty"]["level"]
    color = None
    if difficulty == 1:
        color == "easy"
    elif difficulty == 2:
        color == "medium"
    else:
        color == "hard"
    return problems[random_index]['stat'], color