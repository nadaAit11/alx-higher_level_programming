#!/usr/bin/python3
"""
This script retrieves the 10 most recent commits from a specified GitHub
repository using the GitHub API. The commits are printed in the format:
'<sha>: <author name>'
"""
import requests
from sys import argv


def main():
    repo_name = argv[1]
    owner_name = argv[2]
    url = (f'https://api.github.com/repos/{owner_name}/{repo_name}/commits')

    response = requests.get(url)
    commits = response.json()

    sorted_commits = sorted(
        commits,
        key=lambda commit: commit['commit']['author']['date'],
        reverse=True
    )

    for i, commit in enumerate(sorted_commits):
        if i == 10:
            break
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")


if __name__ == "__main__":
    main()
