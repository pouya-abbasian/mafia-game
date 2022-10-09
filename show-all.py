import pickle
players_file = "players.dat"
gamers_file = "gamers.dat"
f = open(players_file, "rb")
players = pickle.load(f)
f.close()
print(players)
f = open(gamers_file, "rb")
gamers = pickle.load(f)
print(gamers)
f.close()