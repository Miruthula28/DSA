
n = int(input())

max_lead = 0
p1 = 0
p2 = 0

# Iterate through rounds
for i in range(n):\
    n  
    
    score_player_1, score_player_2 = map(int, input().split())

    # Update total scores
    p1 += score_player_1
    p2 += score_player_2

    # Calculate lead
    lead = abs(p1 - p2)

    # Update maximum lead and winner
    if lead > max_lead:
        max_lead = lead
        if p1 > p2:
            winner = 1
        else:
            winner = 2


print(f"{winner} {max_lead}")

    

