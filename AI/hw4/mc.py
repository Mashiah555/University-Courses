import blackjack as bj
import hw

pi = bj.initPolicy()
val = bj.initVal()
for _ in range(2000000):
    epi = bj.generateEpisode(pi)
    gain = 0
    for i in range(bj.episodeLen(epi)-1, -1, -1):
        gain = bj.GAMMA * gain + bj.reward(epi, i)
        hw.updateValAndPi(pi, val, epi, i, gain)
bj.printPolicy(pi)







































