from bs4 import BeautifulSoup as bs
from libs.Stats import BattingStats as bats
from libs.Stats import BattingStats as bowls
# from libs.DivisionInfo import

import requests
import argparse
import logging


logging.basicConfig(level=logging.INFO)

logging.info("Setting argparse")
parser = argparse.ArgumentParser()
parser.add_argument("--team", type=str, required=False, help="Team name to fetch info for.")
parser.add_argument("--player", type=str, required=False, help="Player name to fetch info for.")
parser.add_argument("--div", type=str, required=False, help="Division to get top 10 batsmen and bowlers for.")

args = parser.parse_args()

url = "https://arcl.org"
logging.info(f"Base URL is set to {url}")


def getTeamDetails(team):
    pass

def getDivisionDetails(div):
    pass

def getPlayerDetails(player):
    pass

def getTop100():
        pass



if args.team:
    getTeamDetails(args.team)
elif args.div:
    getDivisionDetails(args.div)
elif args.player:
    getPlayerDetails(args.player)
else:
    # Get top 100 players (100 bowlers and 100 batsmen) in the entire league
    getTop100()
