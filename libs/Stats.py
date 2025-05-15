class BattingStats:
    @staticmethod
    def getStrikeRate(runs, balls):
        return round(runs/balls, 2)

    @staticmethod
    def getBattingAverage(runs, innings, notOuts):
        return round(runs/(innings-notOuts), 2)


class BowlingStats:
    @staticmethod
    def getEconomyRate(runs, overs):
        balls = (int(overs)*6) + int((round(overs-int(overs), 1) * 10))
        return round(runs*6/balls, 2)