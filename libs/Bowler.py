def getNumberOfBalls(overs):
    return (int(overs) * 6) + int((round(overs - int(overs), 1) * 10))

def getEconomyRate(runs, overs):
    return round(runs*6/getNumberOfBalls(overs), 2)

def getBowlingAverage(runs, wickets):
    try:
        return round(runs/wickets, 2)
    except ZeroDivisionError:
        return None

def getBowlingStrikeRate(overs, wickets):
    try:
        return round(getNumberOfBalls(overs)/wickets, 2)
    except ZeroDivisionError:
        return None


class Bowler:
    def __init__(self, name, teamName, innings, overs, maidens, runs, wickets):
        self.name = name
        self.teamName = teamName
        self.innings = int(innings)
        self.overs = float(overs)
        self.runs = int(runs)
        self.wickets = int(wickets)

        self.econ = getEconomyRate(self.runs, self.overs)
        self.avg = getBowlingAverage(self.runs, self.wickets)
        self.str = getBowlingStrikeRate(self.overs, self.wickets)

    # def __str__(self):
    #     return (f"{self.name},"
    #             f"{self.teamName},"
    #             f"{self.runs},"
    #             f"{self.wickets},"
    #             f"{self.overs},"
    #             f"{self.econ},"
    #             f"{self.avg},"
    #             f"{self.str}"
    #     )