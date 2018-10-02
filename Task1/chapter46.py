def display_result(winner, score, **other_info):
    print("The winner was " + winner)
    print("The score was " + score)
    for key, value in other_info.items():
        print(key + ": " + value)
        
        
team = "Barcelona"
goals = "6-0"
injures = "none"
substitute = 3

display_result(team, goals)
