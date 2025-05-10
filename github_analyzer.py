# github_analyzer.py

import requests
from collections import Counter


username = 'tebogomonamodi08'
def fetch_user_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError("User not found or API error.")
    return response.json()

def extract_languages(repos):
    language_counter = Counter()
    for repo in repos:
        if repo["language"]:
            language_counter[repo["language"]] += 1
    return language_counter
