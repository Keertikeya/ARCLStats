def getBattingAverage(runs, innings, notOuts):
    return round(runs/(innings-notOuts), 2)

def getStrikeRate(runs, ballsFaced):
    return round(runs*100/ballsFaced, 2)

class Batsman:
    dismissalTypes = {
        "bowled": 0,
        "caught": 0,
        "run out": 0,
        "stumped": 0,
        "not out": 0
    }

    def __init__(self, name, teamName, runs, balls, innings):
        self.str = None
        self.avg = None
        self.name = name
        self.teamName = teamName
        self.runs = runs
        self.balls = balls
        self.innings = innings

    def setDismissal(self, dismissal_type):
        self.dismissalTypes[dismissal_type] += 1

    def setBattingAverage(self):
        self.avg = getBattingAverage(self.runs, self.innings, self.dismissalTypes["not out"])

    def setStrikeRate(self):
        self.str = getStrikeRate(self.runs, self.balls)
