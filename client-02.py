import pickle
from random import randrange
client = "02"
mafia = ["godfathter", "nato", "normal-mafia"]
gamers_file = "gamers.dat"
players_file = "players.dat"
## first check
def checkMyside():
    f = open(players_file, "rb")
    players = pickle.load(f)
    f.close()
    if players not in mafia:
        print("shoma city hasti")
    else:
        print("shoma mafia hasti")
def checkMyact():
    f = open(players_file, "rb")
    players = pickle.load(f)
    f.close()
    if client in players:
        print("shoma ghablan naghsh gerefti va nemitoni dobare naghsh begiri vaysa hame bgrin!")
        print("naghshe shoma %s va :" %players[client])
        checkMyside()
        exit()

checkMyact()

f = open(gamers_file, "rb")
gamers = pickle.load(f)
random_player = randrange(len(gamers))
player = gamers[random_player]
print("naghshe shoma dar bazi %s shode" %player)
f.close()
del gamers[random_player]
##delet player from all player list
f = open(gamers_file, "wb")
pickle.dump(gamers, f)
f.close
f = open(players_file, "rb")
players =  pickle.load(f)
players[client] = player
f.close()
f = open(players_file, "wb")
pickle.dump(players, f)
f.close()
#check whats my act
checkMyside()
