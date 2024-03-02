#!/usr/bin/python3
"""
Uses the Github API to list the 10 most recent commits
"""
import sys
import requests


if __name__ == "__main__":
    address = 'https://api.github.com/repos/{}/{}/commits'
    req = requests.get(address.format(sys.argv[2], sys.argv[1]))
    reqs = req.json()

    for commit in reqs[:10]:
        sha = commit['sha']
        com = commit['commit']['author']['name']
        print("{}: {}".format(sha, com))
