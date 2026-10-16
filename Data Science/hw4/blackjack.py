import random

GAMMA = 1
ALPHA = 0.9
EPSILON = 0.2

#Initialzes the policy: always stand
def initPolicy():
    pi = 10 * [0]
    for d in range(10):#Dealers's first card = d+1
        pi[d] = 9 * [0]
        for p in range(9):#Player's sum = p+12 (one ace counts as 11)
            pi[d][p] = ["H", "H"]# [0] - no ace  [1] - with an ace
    return pi


def initVal():
    valHit = 10 * [0]
    valStand = 10 * [0]
    for d in range(10):#Dealers's first card = d+1
        valHit[d] = 9 * [0]
        valStand[d] = 9 * [0]
        for p in range(9):#Player's sum = p+12 (one ace counts as 11)
            # [0] - no ace  [1] - with an ace
            valHit[d][p] = [0,0]
            valStand[d][p] = [0,0]
    return {"Hit":valHit, "Stand":valStand}


#Retuens an entire episode = player's states,
#dealer's sum of cards and dealer's first card
def generateEpisode(pi):
    tot = 0
    ace = 0
    while tot+ace < 12:#Getting to the "interesting" states
        card = drawCard()
        tot += card
        if card == 1:
            ace = 10
        if tot+ace > 21 and ace == 10:
            ace = 0
    ep = [[tot, ace]]
    dealerFirst = drawCard()
    # Adding cards to the episode
    rnd = random.random()
    while tot+ace < 21 and \
          ( pi[dealerFirst-1][tot+ace-12][ace//10] == "H" and rnd > EPSILON\
            or\
            pi[dealerFirst-1][tot+ace-12][ace//10] == "S" and rnd <= EPSILON ):
        card = drawCard()
        tot += card
        if card == 1:
            ace = 10
        if tot+ace>21:
            ace = 0
        ep += [[tot, ace]]
        rnd = random.random()
    return {"Player":ep, "Dealer's first":dealerFirst, "Dealer's sum": dealer(tot = dealerFirst)}       
    
#Returns a randomly selected card
def drawCard():
    return random.choice(list(range(1, 10)) + [10]*4 )

#Returns the sum of dealer's cards
#May get the first card as a parameter
def dealer(tot = 0):
    if tot == 1:
        ace = 10
    else:
        ace = 0
    while tot+ace < 17:
        card = drawCard()
        tot += card
        if card == 1:
            ace = 10
        if tot+ace>21 and ace==10:
            ace = 0
    return tot+ace

#Returns the number of states in the episode
def episodeLen(epi):
    return len(epi["Player"])

#Returns the reward for state i in the episode
def reward(epi, i):
    if episodeLen(epi) == i+1:
        player = epi["Player"][i][0] + epi["Player"][i][1]
        dealer = epi["Dealer's sum"]
        if player > 21:
            return -1
        if dealer > 21 or player > dealer:
            return 1
        if player < dealer:
            return -1
    return 0    

def printPolicy(pi):
    for a in [0,1]:
        print()
        print(["Without an ace", "With an ace"][a])
        for d in range(10):
            print()
            for p in range(9):
                print(pi[d][p][a], end = "")


                
