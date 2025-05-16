def getBattingAverage(runs, innings, notOuts):
    return round(runs/(innings-notOuts), 2)

def getStrikeRate(runs, ballsFaced):
    try:
        return round(runs*100/ballsFaced, 2)
    except ZeroDivisionError:
        return 50

class Batsman:
    dismissalTypes = {
        "bowled": 0,
        "caught": 0,
        "run out": 0,
        "stumped": 0,
        "not out": 0
    }

    def __init__(self, name, teamName, runs, balls, innings, fours, sixes):
        self.highestScore = None
        self.str = None
        self.avg = None
        self.name = name
        self.teamName = teamName
        self.runs = int(runs)
        self.balls = int(balls)
        self.innings = int(innings)
        self.fours = int(fours)
        self.sixes = int(sixes)

    def setDismissal(self, dismissal_type):
        self.dismissalTypes[dismissal_type] += 1

    def setBattingAverage(self):
        self.avg = getBattingAverage(self.runs, self.innings, self.dismissalTypes["not out"])

    def setStrikeRate(self):
        self.str = getStrikeRate(self.runs, self.balls)

    def setHighestScore(self, highestScore):
        self.highestScore = highestScore
