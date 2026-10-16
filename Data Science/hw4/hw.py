import blackjack

def updateValAndPi(pi, val, epi, i, gain):
    """
    Updates the action-value function (Q-table) and updates the policy to be 
    greedy with respect to the updated action-values using Monte Carlo / SARSA.
    
    Parameters:
    pi (list): The policy array mapping states to actions.
    val (dict): The action-value tables for 'Hit' and 'Stand'.
    epi (dict): The current episode tracking player states and dealer's cards.
    i (int): The current state index within the episode.
    gain (float): The calculated return (G_t) from this state onward.
    """

    # Extract state indices from the episode
    d = epi["Dealer's first"] - 1
    p = (epi["Player"][i][0] + epi["Player"][i][1]) - 12
    a = epi["Player"][i][1] // 10

    # Index overflow check
    if p < 0 or p > 8:
        return

    # Determine the action taken at the current step
    # If it is the last index in the episode, the action is 'Stand', otherwise 'Hit'
    if i == len(epi["Player"]) - 1:
        action = "Stand"
    else:
        action = "Hit"

    # Incremental update rule
    val[action][d][p][a] += blackjack.ALPHA * (gain - val[action][d][p][a])

    # Policy Improvement:
    # Make the policy greedy based on the highest value between Hit and Stand
    if val["Hit"][d][p][a] > val["Stand"][d][p][a]:
        pi[d][p][a] = "H"
    else:
        pi[d][p][a] = "S"