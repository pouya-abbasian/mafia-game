import pickle
from os import path

# mafia:
# godfather
# nato : naghsh hads mizane
# normal-mafia
# -------
# city:
# doctor
# karegah
# tofangdar
# zere poosh : 2 ta joon dare va
#takaavar : shab shot mafia tir mizane
# normal-city
mafia = ["godfathter", "nato", "normal-mafia"]
city = ["doctor", "karegah", "tofangdar", "zere poosh", "takaavar", "normal-city", "normal-city", "normal-city", "normal-city"]
gamer_file = "gamers.dat"
players_file = "players.dat"
def makeGamersfile():
    f = open(gamer_file, "wb")
    gamers = mafia + city
    pickle.dump(gamers, f)
    f.close
def makePlayersfile():
    f = open(players_file, "wb")
    players = {}
    pickle.dump(players, f)
    f.close() 

print("Wellcome to the mafia game.")



# f = open(, "w+")
makeGamersfile()
makePlayersfile()