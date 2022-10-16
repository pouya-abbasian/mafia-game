# ids = random.sample(range(0, 12), 12) 
## Kasi Ke id 1 mishe, darvaghe godfather mishe
#har client baraye khodesh ye id migire : # ids = random.sample(range(0, 12), 12)
##TODO in mishe file server, client bayad neveshte beshe
## aval user & pass check beshe bad start game kone o id bgire az server[mysql]
## id = randrange(1,13) username = username
## id1 = godfaher, id2= mafia sade va ...
## user,  id ro migire o miad inja id mide, naghsh migire
## user ha nabayad poshte sare ham bashan va ba randrange, bayad jahashon avaz beshe ke naghsh hashon az tarighe bug, moshakhas nabashe!!!
## masaln intori : 3, 6, 1, 2, 9, 12, 5 ... k user3 darvaghe hamoon nato mafia e
## chinesh ham pas ba randrange ok mishe va toye ye file 'sort.dat' save mikonim. va sare sohbat k shansi peyda shode bud(exaple :3)
## shoro be sohbat mikone. ba function 
## user ha be tartib
from os import system
from time import sleep
import pickle
from abc import ABC, abstractmethod
import random
from os import path
import pickle
# users_file = "database.dat"
# users = []
# def checkUSERSfile():
#     if not path.exists(users_file):
#         f = open(users_file, "wb")
#         pickle.dump(users, f)
#         f.close
# checkUSERSfile()
# f = open(users_file, "rb")
# users_num = int(len(pickle.load(f)))
# f.close()
# def console():

#     system("cls")
#     print("Wellcome To Mafia... \nWaiting For Users. %susers joined!" %users_num)

# while users_num < 12:
#     console()
#     sleep(2)
#     f = open(users_file, "rb")
#     users_num = int(len(pickle.load(f)))
#     f.close
#     print(users_num)
#     f = open(users_file, "rb")
#     users = pickle.load(f)
#     users = users
#     f.close()
# Class's
users = ["pouya", "ali", "ahmad", "sara", "parisa", "fateme", "mohammad", "hosein", "hasaan", "armin", "amir", "mehead"]
class Player(ABC):
    def __init__(self, player, username, role, side, health, s, night):
        self.player = player
        self.username = username
        self.role = role
        self.side = side
        self.health = health
        self.s = s
        self.night = night
    def speak(self):
        if int(all_players[self.player-1].health) > 0:
            message = input("%s befarmayid : " %all_players[self.player-1].username)
            print("%s : %s" %(all_players[self.player-1].username, message))
        else:
            print("Pass!")
    def like(self):
        print("%i : %s LIKE!" %(self.player, self.username))
    def disslike(self):
        print("%i : %s DIssLIKE!" %(self.player, self.username))
    def lala(self):
        pass
    def wake_up(self):
        pass
    def getInfo(self):
        print("%i : %s ~> %s : %i : %s\n================" %(self.player, self.username, self.role, int(self.health), self.side))
    def newDay(self):
        if int(all_players[self.player-1].health) <= 0:
            all_players[self.player-1].side = "DEAD"
            all_players[self.player-1].s = "DEAD"
            all_players[self.player-1].night = "DEAD"
            all_players[self.player-1].health = 0
            all_players[self.player-1].username = "$DEAD[%s]$" %all_players[self.player-1].username
            print("%s raft birun" %all_players[self.player-1].username)
        else:
            all_players[self.player-1].health = 1



class Normal_City(Player):
    pass
class Mafia(Player):
    def shot(self, inputuser):
        self.inputuser = inputuser - 1
        all_players[self.inputuser].health -= 1
        print("%s : %i" %(all_players[self.inputuser].username, all_players[self.inputuser].health))
        print("ok")
        # print("%i %s Shot and health is : %i" %(all_players[player].player, all_players[player].username, all_players[player].health))
## 1: GodFather
class GodFather(Mafia):
    pass
# 2: Normal-Mafia
class Normal_Mafia(Mafia):
    pass

# 3: Nato Mafia
class NatoMafia(Mafia):
    def nato(self, inputuser, inputrole):
        self.inputuser = inputuser -1
        self.inputrole = inputrole
        if all_players[self.inputuser].role == self.inputrole:
            all_players[self.inputuser].health -= 2
            print("%s Dead!" %all_players[self.inputuser].username)
        else:
            print("Nato kir khorde")
# 4: Gero Mafia
class GeroMafia(Mafia):
    ## naghshe shakhs ro gero migire
    ## har shab bayad yeki ro gero begire ya yeki dar mion
    pass
## City TEAM
# 5: Doctor
class Doctor(Normal_City):
    def save(self, inputuser):
        self.inputuser = inputuser -1
        if all_players[self.player -1 ].health > 0:
            if all_players[self.inputuser].health > 0:
                all_players[self.inputuser].health += 1
                print("[%s] saved with doctor" %all_players[self.inputuser].username)
            else:
                print("Kes Gir Biardi? Morde yaroo")
        else:
            print("Doctor Morde :D")
            #print khode doctor
            # print(all_players[self.player -1 ].player)
# 6 : Commondo
## shab age tir bohkore 
## age godfather bzne jofteshon mishinn
class Commondo(Normal_City):
    pass
# 7 : Negahbaan
## shab bidar mishe az naghsh dar moghabel gero negah dari mikone  [ba shakhs kar mikone]
## 
class Negahban(Normal_City):
    pass
# 8 :Gunman
class Gunman(Normal_City):
    pass
# 9: Detective
class Detective(Normal_City):
    def check(self, inputuser):
        self.inputuser = inputuser - 1
        print(all_players[self.inputuser].s)
##Este'laam ro bayad dorost konm.
#mafia be tartib : god, nato, mafia, gero
#shab bidar mishe like mibine
#takaavar zamaani shab mitune shot kone k khodesh tir khorde bashe
## negah ban shab shot mishe vali sobh birun nmire####
######################################################
######################################################
####               ## 12 Players                  ####
####  1: Godfather, 2: mafia-sade, 3: Nato-mafia  ####
####  4: Gero-Mafia 5: Doctor      6: Commondo    ####
####  7: NegahBan   8: gunman      9: Detective   ####
####        10, 11, 12 : Normaly-City             ####
######################################################
######################################################

#Functions : 
def checkCity():
    mafias = []
    citys = []
    deads = []
    city = {
        "mafia" : mafias,
        "city" : citys,
        "dead" : deads
    }
    for i in range(0, len(all_players)):
        if all_players[i] in mafia_team and all_players[i].health != 0:
            mafias.append(all_players[i])
            city["mafia"] = mafias
        elif all_players[i] in city_team and all_players[i].health != 0:
            citys.append(all_players[i])
            city["city"] = citys
        elif all_players[i] in gero_from_mafia and all_players[i].health != 0:
            mafias.append(all_players[i])
        else:
            deads.append(all_players[i])
            city["dead"] = deads
    return city
def getinFormation():
    for i in range(0, len(all_players)):
        all_players[i].getInfo()
def wakeUp():
    for i in range(0, len(all_players)):
        if all_players[i].side != "DEAD":
            all_players[i].newDay()
def sPeak():
    for i in range(0, len(all_players)):
        all_players[i].speak()

def wakeUp_mafia():
    print(checkCity()["mafia"])
    for i in range(0, len(checkCity()["mafia"])):
        mafia_team[i].speak()
def mafiaShot():
    inputuser = int(input("entekhab mafia baraye shot shab [1 - 12] ~> "))
    if god_father.health > 0:
        god_father.shot(inputuser)
    elif normal_mafia.health > 0:
        normal_mafia.shot(inputuser)
    elif nato_mafia.health > 0:
        nato_mafia.shot(inputuser)
    else:
        gero_mafia.shot(inputuser)

def mafiaNato():
    inputuser = int(input("nato'ee baraye che kasi ? [1 - 12] ~> "))
    inputrole = input("che naghshi dare ?  ")
    nato_mafia.nato(inputuser, inputrole)
## Nato OR shot in night
def natoORshot():
    answer = int(input("shot or nato?[1= shot, 2=nato]~>"))
    if answer == 1:
        mafiaShot()
    elif answer == 2:
        mafiaNato()
    else:
        print("Agha kos gir avordi?")
        natoORshot()
selfsave = 1
## save with doctor
def doctorSave():
    inputuser = int(input("[GOD] doctor che kasi ra save mikonad? [1 - 12] ~> "))
    city_doctor.save(inputuser)

#Randomise USers
newname = []
for i in random.sample(range(0, 12), 12):
    newname.append(users[i])
users = newname
del newname
##FIRST CHARS
## 1 :GodFather:  Shot Shab
users[0] = {
    
    "player" : 0,
    "username" : users[0],
    "role" : "God-Father",
    "side" : "Mafia",
    "health" : 1,
    "s" : "Disslike",
    "night" : 1
}
## 2: Normal Mafia ~> Bad az God Father, Tofang be mafia sade mirese!
users[1] = {
    "player" : 1,
    "username" : users[1],
    "role" : "Normal-Mafia",
    "side" : "Mafia",
    "health" : 1,
    "s" : "like",
    "night" : 1
}
## 3: Nato Mafia ~> naghshe kasi ro mitune hads bezane, agar dorst bege, ... agr berine, mire birun
users[2] = {
    "player" : 2,
    "username" : users[2],
    "role" : "Nato-Mafia",
    "side" : "Mafia",
    "health" : 1,
    "s" : "like",
    "night" : 1
}
## 4: Gero Mafia ~> ye Gohi mikhore k hanoz nmidonm che Gohi
users[3] = {
    "player" : 3,
    "username" : users[3],
    "role" : "Gero-Mafia",
    "side" : "Mafia",
    "health" : 1,
    "s" : "like",
    "night" : 2
}
##end 
### City TEAM
## 5 : Doctor ~> Shab bidar mishe yekio health +1 mikone!
users[4] = {
    "player" : 4,
    "username" : users[4],
    "role" : "Doctor",
    "side" : "City",
    "health" : 1,
    "s" : "Disslike",
    "night" : 3
}
## 6 : Commondo ~> Age shab shot beshe mitune bidar she va tir bzne, age mafia bzne. mimune tu bazi va mafia mire, age city bzne, khodesh mire birun.
#Ta Zamani k tir nkhorde, normal_city e ;)
users[5] = {
    "player" : 5,
    "username" : users[5],
    "role" : "Commondo",
    "side" : "City",
    "health" : 1,
    "s" : "Disslike",
    "night" : 0##agaram beshe : night 4
}
# Negahban ~> Shab Shot Beshe mire birun, Sobh ba raygiri birun nmire.
## shab health = 1
## Sobh health = 2, ta zamani k y bar, separesh bshkane!
users[6] = {
    "player" : 6,
    "username" : users[6],
    "role" : "NegahBaan",
    "side" : "City",
    "health" : 1,#Sobh Health = 2, Shab health = 1
    "s" : "Disslike",
    "night" : 0
}
## Gunman ~> ta vaghti bidar mishe k 2 ta tir asli dashte bashe
users[7] = {
    "player" : 7,
    "username" : users[7],
    "role" : "Gunman",
    "side" : "City",
    "health" : 1,
    "s" : "Disslike",
    "night" : 5,
    "fake" : "Empty",
    "realy" : "Empty"
}
# Detective ~> Shab Estelame kasi ke mikhad ro migire
users[8] = {
    "player" : 8,
    "username" : users[8],
    "role" : "Detective",
    "side" : "City",
    "health" : 1,
    "s" : "Disslike",
    "night" : 6
}
users[9] = {
    "player" : 9,
    "username" : users[9],
    "role" : "Normal-City",
    "side" : "City",
    "health" : 1,
    "s" : "Disslike",
    "night" : 0
}
users[10] = {
    "player" : 10,
    "username" : users[10],
    "role" : "Normal-City",
    "side" : "City",
    "health" : 1,
    "s" : "Disslike",
    "night" : 0
}
users[11] = {
    "player" : 11,
    "username" : users[11],
    "role" : "Normal-City",
    "side" : "City",
    "health" : 1,
    "s" : "Disslike",
    "night" : 0
}


god_father = GodFather(users[0]["player"], users[0]["username"], users[0]["role"], users[0]["side"], users[0]["health"], users[0]["s"] ,users[0]["night"])
normal_mafia = Normal_Mafia(users[1]["player"], users[1]["username"], users[1]["role"], users[1]["side"], users[1]["health"], users[1]["s"], users[1]["night"])
nato_mafia = NatoMafia(users[2]["player"], users[2]["username"], users[2]["role"], users[2]["side"], users[2]["health"], users[2]["s"], users[2]["night"])
gero_mafia = GeroMafia(users[3]["player"], users[3]["username"], users[3]["role"], users[3]["side"], users[3]["health"], users[3]["s"], users[3]["night"])
city_doctor = Doctor(users[4]["player"], users[4]["username"], users[4]["role"], users[4]["side"], users[4]["health"], users[4]["s"], users[4]["night"])
city_commondo = Commondo(users[5]["player"], users[5]["username"], users[5]["role"], users[5]["side"], users[5]["health"], users[5]["s"],  users[5]["night"])
city_negahban = Negahban(users[6]["player"], users[6]["username"], users[6]["role"], users[6]["side"], users[6]["health"], users[6]["s"],  users[6]["night"])
city_gunman = Gunman(users[7]["player"], users[7]["username"], users[7]["role"], users[7]["side"], users[7]["health"], users[7]["s"],  users[7]["night"])
city_detective = Detective(users[8]["player"], users[8]["username"], users[8]["role"], users[8]["side"], users[8]["health"], users[8]["s"],  users[8]["night"])
normal_city00 = Normal_City(users[9]["player"], users[9]["username"], users[9]["role"], users[9]["side"], users[9]["health"],users[9]["s"],  users[9]["night"])
normal_city01 = Normal_City(users[10]["player"], users[10]["username"], users[10]["role"], users[10]["side"], users[10]["health"],users[10]["s"],  users[10]["night"])
normal_city02 = Normal_City(users[11]["player"], users[11]["username"], users[11]["role"], users[11]["side"], users[11]["health"],users[11]["s"], users[11]["night"])
mafia_team = [god_father, normal_mafia, nato_mafia]
gero_from_mafia = [gero_mafia]
city_team = [city_doctor, city_commondo, city_negahban, city_gunman, city_detective, normal_city00, normal_city01, normal_city02]
all_players = mafia_team + gero_from_mafia +  city_team

## END

##Randomise Players
j = 1
random_roles = []
for i in random.sample(range(0, 12), 12):
    random_roles.append(all_players[i])
    all_players[i].player = j
    j += 1 
all_players = random_roles
del j
del random_roles






##Start Game


# natoORshot()
# getinFormation()
# ## Night One
# print("Shab mishavad!")
# n = int(input("[GOD] Doctor Che kasi ra mikhahad save konad? ~>"))
# city_doctor.save(n)
# # n = int(input("[GOD] mafia be che kasi shelik mikonad? ~>"))
# # mafiaShot(n)
# n = int(input("[GOD] detectice estelame che kasi ra mikhahad? ~>"))
# city_detective.check(n)

# ## Day 2 
# print("Sobh shode cheshmatono baz konid . ")
# wakeUp()
# getinFormation()
# sPeak()

# ## Night 2
# print("Shab mishavad!")
# n = int(input("[GOD] Doctor Che kasi ra mikhahad save konad? ~>"))
# city_doctor.save(n)
# n = int(input("[GOD] mafia be che kasi shelik mikonad? ~>"))
# god_father.shot(n)
# n = int(input("[GOD] detectice estelame che kasi ra mikhahad? ~>"))
# city_detective.check(n)


# ## Day 3
# print("Sobh shode cheshmatono baz konid . ")
# wakeUp()
# getinFormation()
# sPeak()

# ## Night 3
# print("Shab mishavad!")
# n = int(input("[GOD] Doctor Che kasi ra mikhahad save konad? ~>"))
# city_doctor.save(n)
# n = int(input("[GOD] mafia be che kasi shelik mikonad? ~>"))
# god_father.shot(n)
# n = int(input("[GOD] detectice estelame che kasi ra mikhahad? ~>"))
# city_detective.check(n)



# ## Day 4
# print("Sobh shode cheshmatono baz konid . ")
# wakeUp()
# getinFormation()
# sPeak()

# ## Night 4
# print("Shab mishavad!")
# n = int(input("[GOD] Doctor Che kasi ra mikhahad save konad? ~>"))
# city_doctor.save(n)
# n = int(input("[GOD] mafia be che kasi shelik mikonad? ~>"))
# god_father.shot(n)
# n = int(input("[GOD] detectice estelame che kasi ra mikhahad? ~>"))
# city_detective.check(n)



# ## Day 5
# print("Sobh shode cheshmatono baz konid . ")
# wakeUp()
# getinFormation()
# sPeak()

# ## Night 5
# print("Shab mishavad!")
# n = int(input("[GOD] Doctor Che kasi ra mikhahad save konad? ~>"))
# city_doctor.save(n)
# n = int(input("[GOD] mafia be che kasi shelik mikonad? ~>"))
# god_father.shot(n)
# n = int(input("[GOD] detectice estelame che kasi ra mikhahad? ~>"))
# city_detective.check(n)

# ## 
## start game

getinFormation()
while len(checkCity()["mafia"]) != 0:
    len_mafia = len(checkCity()["mafia"])
    len_city = len(checkCity()["city"])
    len_dead = len(checkCity()["dead"])
    print("Mafia : %i\nCity : %i\nDead : %i" %(len_mafia, len_city, len_dead))
    if len_mafia == len_city:
        print("mafia win!")
        break
    elif len_city == 2:
        print("Bayad Dast Bedan Be ham")
        # all_players = checkCity()["mafia"] + checkCity()["city"]
        number = 0
        keyas_players = []
        for i in range(0, 12):
            if all_players[i].health != 0:
                keyas_players.append(all_players[i])
                keyas_players[number].player = number + 1
                number += 1
        all_players = keyas_players
        del keyas_players
        del number

        getinFormation()
        sPeak()
        break
    #Day
    # sPeak()
    #checkGun()

    #Night
    doctorSave()
    natoORshot()
    
    #good night, GO to Next Day
    wakeUp()
    getinFormation()
# sPeak()
if len_mafia == 0:
    print("city win")
print("Good Lock")
