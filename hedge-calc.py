def oddsToProbability(odds):
    if odds < 0:
        return abs(odds) / (abs(odds) + 100)
    else:
        return 100 / (odds + 100)
    
def betPayout(odds, bet):
    if odds < 0:
        return bet * 100 / abs(odds)
    else:
        return bet * odds / 100

# to win finals
PACERS_CASH_OUT = 239.55
PACERS_BET = 100
PACERS_FINALS_ODDS_ORIGINAL = 15000
PACERS_FINALS_ODDS_NEW = 2500

# to win ecf
CELTICS_ECF_ODDS = -1250
PACERS_ECF_ODDS = 710

# nba finalists
BOS_MIN = -145
BOS_DAL = 150
IND_MIN = 1100
IND_DAL = 1700
total = sum([oddsToProbability(_) for _ in [BOS_MIN, BOS_DAL, IND_MIN, IND_DAL]])
pacers_implies_prob_vs_celtics = (oddsToProbability(IND_MIN) + oddsToProbability(IND_DAL)) / total

# celtics bet to win ecf
CELTICS_BET = 4500

# if celtics win
print(betPayout(CELTICS_ECF_ODDS, CELTICS_BET) - PACERS_BET)

# implied probability pacers win finals
pacers_implied = oddsToProbability(PACERS_FINALS_ODDS_NEW) / oddsToProbability(PACERS_ECF_ODDS)

# if pacers win
print(pacers_implied * PACERS_FINALS_ODDS_ORIGINAL - CELTICS_BET)