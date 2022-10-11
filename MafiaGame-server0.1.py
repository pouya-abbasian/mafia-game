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
from abc import ABC, abstractmethod
import random
# Class's
class Player(ABC):
    def __init__(self, id, username, role, side, health, s, night):
        self.id = id
        self.username = username
        self.role = role
        self.side = side
        self.health = health
        self.s = s
        self.night = night
    def speak(self, zer):
        self.zer = zer
        print(zer)
        return zer
    def like(self):
        return self.username + " Like"
    def disslike(self):
        return self.username + " DissLike" 
    def lala(self):
        pass
    def wake_up(self):
        pass
class Normal_City(Player):
    pass
class Mafia(Player):
    pass
## 1: GodFather
class GodFather(Mafia):
    def shot(self, user):
        self.user = user
        print("you kill %s" %user)
# 2: Normal-Mafia
class Normal_Mafia(Mafia):
    def AfterGodFather(self):
        if god_father.health == 0:
            print("GodFather Mord")
        else:
            print("Ma Kirekharim")
# 3: Nato Mafia
class NatoMafia(Mafia):
    pass
# 4: Gero Mafia
class GeroMafia(Mafia):
    pass
## City TEAM
# 5: Doctor
class Doctor(Normal_City):
    pass
# 6 : Commondo
class Commondo(Normal_City):
    pass
# 7 : Negahbaan
class Negahban(Normal_City):
    pass
# 8 :Gunman
class Gunman(Normal_City):
    pass
# 9: Detective
class Detective(Normal_City):
    def check(self, name):
        self.name = name
        if self.name.s == "like":
            print("Mafia")
        else:
            print("City")
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
##FIRST CHARS
## 1 :GodFather:  Shot Shab

god_father = {
    "id" : 1,
    "username" : "pouya",
    "role" : "God-Father",
    "side" : "Mafia",
    "health" : 1,
    "s" : "Disslike",
    "night" : 1
}
## 2: Normal Mafia ~> Bad az God Father, Tofang be mafia sade mirese!
normal_mafia = {
    "id" : 2,
    "username" : "Ali",
    "role" : "Normal-Mafia",
    "side" : "Mafia",
    "health" : 1,
    "s" : "like",
    "night" : 1
}
## 3: Nato Mafia ~> naghshe kasi ro mitune hads bezane, agar dorst bege, ... agr berine, mire birun
nato_mafia = {
    "id" : 3,
    "username" : "ahmad",
    "role" : "Nato-Mafia",
    "side" : "Mafia",
    "health" : 1,
    "s" : "like",
    "night" : 1
}
## 4: Gero Mafia ~> ye Gohi mikhore k hanoz nmidonm che Gohi
gero_mafia = {
    "id" : 4,
    "username" : "Mohammad",
    "role" : "Gero-Mafia",
    "side" : "Mafia",
    "health" : 1,
    "s" : "like",
    "night" : 2
}
##end 
### City TEAM
## 5 : Doctor ~> Shab bidar mishe yekio health +1 mikone!
city_doctor = {
    "id" : 5,
    "username" : "Armin",
    "role" : "Doctor",
    "side" : "City",
    "health" : 1,
    "s" : "Disslike",
    "night" : 3
}
## 6 : Commondo ~> Age shab shot beshe mitune bidar she va tir bzne, age mafia bzne. mimune tu bazi va mafia mire, age city bzne, khodesh mire birun.
#Ta Zamani k tir nkhorde, normal_city e ;)
city_commondo = {
    "id" : 6,
    "username" : "Fardin",
    "role" : "Commondo",
    "side" : "City",
    "health" : 1,
    "s" : "Disslike",
    "night" : 0##agaram beshe : night 4
}
# Negahban ~> Shab Shot Beshe mire birun, Sobh ba raygiri birun nmire.
## shab health = 1
## Sobh health = 2, ta zamani k y bar, separesh bshkane!
city_negahban = {
    "id" : 7,
    "username" : "Reza",
    "role" : "NegahBaan",
    "side" : "City",
    "health" : 1,#Sobh Health = 2, Shab health = 1
    "s" : "Disslike",
    "night" : 0
}
## Gunman ~> age delesh bekhad be 2 nafar tir mide.
city_gunman = {
    "id" : 8,
    "username" : "Sadegh",
    "role" : "Gunman",
    "side" : "City",
    "health" : 1,
    "s" : "Disslike",
    "night" : 5,
    "fake" : "Empty",
    "realy" : "Empty"
}
# Detective ~> Shab Estelame kasi ke mikhad ro migire
city_detective = {
    "id" : 9,
    "username" : "Saber",
    "role" : "Detective",
    "side" : "City",
    "health" : 1,
    "s" : "Disslike",
    "night" : 6
}
normal_city00 = {
    "id" : 10,
    "username" : "Moein",
    "role" : "Normal-City",
    "side" : "City",
    "health" : 1,
    "s" : "Disslike",
    "night" : 0
}
normal_city01 = {
    "id" : 11,
    "username" : "Soheyl",
    "role" : "Normal-City",
    "side" : "City",
    "health" : 1,
    "s" : "Disslike",
    "night" : 0
}
normal_city02 = {
    "id" : 12,
    "username" : "Morad",
    "role" : "Normal-City",
    "side" : "City",
    "health" : 1,
    "s" : "Disslike",
    "night" : 0
}
   
god_father = GodFather(god_father["id"], god_father["username"], god_father["role"], god_father["side"], god_father["health"], god_father["s"] ,god_father["night"])
normal_mafia = Normal_Mafia(normal_mafia["id"], normal_mafia["username"], normal_mafia["role"], normal_mafia["side"], normal_mafia["health"], normal_mafia["s"], normal_mafia["night"])
nato_mafia = NatoMafia(nato_mafia["id"], nato_mafia["username"], nato_mafia["role"], nato_mafia["side"], nato_mafia["health"], nato_mafia["s"], nato_mafia["night"])
gero_mafia = GeroMafia(gero_mafia["id"], gero_mafia["username"], gero_mafia["role"], gero_mafia["side"], gero_mafia["health"], gero_mafia["s"], gero_mafia["night"])
city_doctor = Doctor(city_doctor["id"], city_doctor["username"], city_doctor["role"], city_doctor["side"], city_doctor["health"], city_doctor["s"], city_doctor["night"])
city_commondo = Commondo(city_commondo["id"], city_commondo["username"], city_commondo["role"], city_commondo["side"], city_commondo["health"], city_commondo["s"],  city_commondo["night"])
city_negahban = Negahban(city_negahban["id"], city_negahban["username"], city_negahban["role"], city_negahban["side"], city_negahban["health"], city_negahban["s"],  city_negahban["night"])
city_gunman = Gunman(city_gunman["id"], city_gunman["username"], city_gunman["role"], city_gunman["side"], city_gunman["health"], city_gunman["s"],  city_gunman["night"])
city_detective = Detective(city_detective["id"], city_detective["username"], city_detective["role"], city_detective["side"], city_detective["health"], city_detective["s"],  city_detective["night"])
normal_city00 = Normal_City(normal_city00["id"], normal_city00["username"], normal_city00["role"], normal_city00["side"], normal_city00["health"],normal_city00["s"],  normal_city00["night"])
normal_city01 = Normal_City(normal_city01["id"], normal_city01["username"], normal_city01["role"], normal_city01["side"], normal_city01["health"],normal_city01["s"],  normal_city01["night"])
normal_city02 = Normal_City(normal_city02["id"], normal_city02["username"], normal_city02["role"], normal_city02["side"], normal_city02["health"],normal_city02["s"], normal_city02["night"])

# normal_mafia.AfterGodFather()
# ## khob hala godfather health -= 1 :
# god_father.health -= 1
# normal_mafia.AfterGodFather()
## END
mafia_team = [god_father, normal_mafia, nato_mafia, gero_mafia]
city_team = [city_doctor, city_commondo, city_negahban, city_gunman, city_detective, normal_city00, normal_city01, normal_city02]
all_players = mafia_team + city_team
# city_detective.check(god_father)
# name = nato_mafia
# city_detective.check(name)

# random.sample(range(0, 12), 12)
newlist = []
j = 1
for i in random.sample(range(0, 12), 12):
    print("bazikone shomare" + str(j) + " be id " + str(all_players[i].id) + " ba naghshe " + all_players[i].role + " az side %s" %all_players[i].side + " ke be onvane %i omin nafar, cheshbaz mikone" %all_players[i].night)
    j += 1

