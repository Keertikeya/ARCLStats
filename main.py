from bs4 import BeautifulSoup as bs

from libs.Batsman import Batsman
from libs.Bowler import Bowler
from libs.Stats import BattingStats as bats
from libs.Stats import BattingStats as bowls
# from libs.DivisionInfo import

import requests
import argparse
import logging
import time
import heapq


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
    logging.info("Getting top 100 batsmen and bowlers for current season")
    divisionLinks = []

    allBatsmen = []
    allBowlers = []

    # Getting homepage HTML content
    homePage = requests.get(url)
    logging.debug(f"Home retrieved:\n{homePage.text}")
    soup = bs(homePage.content, "html.parser")
    logging.debug(f"Soup has been made:\n {soup.text}")

    # Getting current season info
    seasonsPOS = soup.find("div", attrs={"id": "seasonspos"})
    currentSeason = seasonsPOS.find_all("option")[0].text.strip()
    logging.info(f"Season name: {currentSeason}")

    # Getting all division links
    poolHeaderMenu = soup.find("div", attrs={"id": "poolheadermenu"})
    for division in poolHeaderMenu.find_all("li"):
        if division.text.strip().startswith("Div"):
            divisionLinks.append(division.find("a").get("href"))

    logging.info("All division links have been retrieved.")
    logging.debug(f"All men's division links:\n{divisionLinks}")

    # Check if current season is invalid, i.e. doesn't have any data
    divLink = requests.get(url + divisionLinks[0])
    div0Soup = bs(divLink.content, "html.parser")
    if len(div0Soup.find_all("table")) == 0:
        currentSeasonId = int(divisionLinks[0].split("season_id=")[1])
        logging.info(f"Current season (id = {currentSeasonId}) has either not started yet or is invalid")
        logging.info(f"Getting info for previous season instead (season_id={currentSeasonId - 1}).")
        for i in range(len(divisionLinks)):
            divisionLinks[i] = divisionLinks[i].replace(str(currentSeasonId), str(currentSeasonId - 1))


    for divisionLink in divisionLinks:
        # 1. Go to each division's page
        logging.info(f"Getting division details: {url + divisionLink}")
        divPage = requests.get(url + divisionLink)
        divSoup = bs(divPage.content, "html.parser")
        try:
            teamsTable = divSoup.find_all("table")[0]
        except IndexError:
            logging.info("Division table has not been retrieved.")
            continue

        teamRows = teamsTable.find_all("tr")[1:]

        teamLinks = []
        for teamRow in teamRows:
            teamLinks.append(teamRow.find_all("td")[0].find("a").get("href"))

        # 2. Go to each team's page in the division
        for teamLink in teamLinks:
            teamPage = requests.get(url + "/Pages/UI/" + teamLink)
            teamSoup = bs(teamPage.content, "html.parser")

            # Get batting stats for team
            battingTable = teamSoup.find_all("table")[2]
            logging.debug(f"Batting table retrieved:\n{battingTable.text}")

            batsmanRows = battingTable.find_all("tr")[1:]
            logging.info(f"SETTING BATSMAN DETAILS FOR TEAM: {batsmanRows[0].find_all("td")[2].text}")
            for batsmanRow in batsmanRows:
                batsman = Batsman(
                    name=batsmanRow.find_all("td")[0].text.strip(),
                    teamName=batsmanRow.find_all("td")[2].text.strip(),
                    innings=batsmanRow.find_all("td")[3].text.strip(),
                    runs=batsmanRow.find_all("td")[4].text.strip(),
                    balls=batsmanRow.find_all("td")[5].text.strip(),
                    fours=batsmanRow.find_all("td")[6].text.strip(),
                    sixes=batsmanRow.find_all("td")[7].text.strip()
                )
                batsman.setBattingAverage()
                batsman.setStrikeRate()

                allBatsmen.append(batsman)

            # Get bowling stats for team
            bowlingTable = teamSoup.find_all("table")[3]
            logging.debug(f"Bowling table retrieved:\n{bowlingTable.text}")

            bowlerRows = bowlingTable.find_all("tr")[1:]
            for bowlerRow in bowlerRows:
                bowler = Bowler(
                    name=bowlerRow.find_all("td")[0].text.strip(),
                    teamName=bowlerRow.find_all("td")[2].text.strip(),
                    innings=bowlerRow.find_all("td")[3].text.strip(),
                    overs=bowlerRow.find_all("td")[4].text.strip(),
                    maidens=bowlerRow.find_all("td")[5].text.strip(),
                    runs=bowlerRow.find_all("td")[6].text.strip(),
                    wickets=bowlerRow.find_all("td")[7].text.strip()
                )

                allBowlers.append(bowler)


    allBatsmen.sort(key=lambda b: b.runs, reverse=True)
    allBowlers.sort(key=lambda b: b.wickets, reverse=True)

    logging.info(f"{len(allBatsmen)} batsmen info has been added.")
    logging.info(f"{len(allBowlers)} bowlers info has been added.")

    logging.info("Top 100 batsmen:")
    for i in range(100):
        logging.info(f"{allBatsmen[i].name}, {allBatsmen[i].teamName}, {allBatsmen[i].runs}")

    logging.info("Top 100 bowlers:")
    for i in range(100):
        logging.info(f"{allBowlers[i].name}, {allBowlers[i].teamName}, {allBowlers[i].wickets}")


    # 3. Retrieve player information for each team
    pass




if args.team:
    getTeamDetails(args.team)
elif args.div:
    getDivisionDetails(args.div)
elif args.player:
    getPlayerDetails(args.player)
else:
    # Get top 100 players (100 bowlers and 100 batsmen) in the entire league
    start = int(time.time())
    getTop100()
    end = int(time.time())

    logging.info(f"Time elapsed: {end - start} seconds")
