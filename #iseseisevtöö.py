#iseseisevtöö
#16.01.2024
#Daniel Žukov

#2

# #Vanused
# 	loo vanuste loend 1p
# 	leia numbrite suurim ja vĆ¤ikseim arv  1p
# 	kogusumma  1p
# 	keskmine 1p

# vanused = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# def vanustestatistika(v):
#     print(f"maximum vanus {max(v)}, minimum vanus {min(v)}")
#     print(f"kogusumma {sum(v)}")
# summa = sum(vanused)

# print ("keskmine", summa/len(vanused))
       
# vanustestatistika(vanused)

#4
# List Less Than Ten
# 	Take a list and write a program that prints out all the elements of the list that are less than 5. 1p
# 		a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# 	Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list. 1p
# 	Write this in one line of Python. 1p
# 	Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# print([numbrid for numbrid in a if numbrid < 5])
# suva_number = int(input("pane number: "))
# print([numbrid for numbrid in a if numbrid < suva_number])

#6
# Koosta programm, mis kontrollib, kas kasutaja poolt sisestatud arv on paaris vÃµi paaritu
# 	kuvatakse korrektne arusaadav kÃ¼simus ja vastus - 1p
# 	eelnev kontroll, kas kasutaja ei lisanud arvu vÃµi pani nulli - 1p
# 	kood mis teavitab paaris vÃµi paaritust arvust - 1p
# 	kuvatakse programmi pealkiri - 1p
# 	kood kommenteeritud - 1p

# Programm, mis kontrollib, kas kasutaja poolt sisestatud arv on paaris või paaritu


# print("paaris ja paaritu arvu kontrollimine")
# input_number = input("sisesta arv: ")
# if not input_number:
#     print("sisesta arv")
# else:
#     number = int(input_number)
#     if number == 0:
#         print("sisestatud arv on null")
#     elif number % 2 == 0:
#         print(f"{number} on paaris arv")
#     else:
#         print(f"{number} on paaritu arv")



#8
# 8. Täringud
# 	kuvatakse korrektne arusaadav küsimus ja hiljem vastus - 1p
# 	kasutaja võistleb kahe täringuga arvuti vastu - 1p
# 	kasutaja teeb pakkumise ning suurima täringupunktisumma võitja saab laual oleva raha endale - 2p
# 	kood kommenteeritud - 1p

# import random
# rahakott = 100
# panus = 10

# print("taringumang: voistle selle boti vastu")
# while rahakott >= panus:
# print(f"sul on {rahakott} raha")
#     print(f"iga mängu panus on {panus} raha")
#     vastus = input("kas soovid mängida jah voi ei? ")

#     if vastus = jah:
#         break

#     rahakott = rahakott - panus
# taring1 = random.randint(1, 6)
# taring2 = random.randint(1, 6)
# botitaring1 = random.randint(1, 6)
# botitaring2 = random.randint(1, 6)
# print(f"su taringud: {taring1}, {taring2}")
# arvamus = int(input("arva ara: "))
# summa = taring1 + taring2
# botisumma = botitaring1 + botitaring2
# print(f"boti taringud: {botitaring1}, {botitaring2}")
# print(f"su taringute summa: {summa}")
# print(f"boti taringute summa: {botisumma}")
# if summa > botisumma:
# rahakott = rahakott + panus
#     print("congrats, sa voitsid ja said moni")
# elif summa < botisumma:
#     print("oled ise nuud bot, sa kaotasid. bot ise voitsis")
# else:
#     print("viik, olete molemad botid")

#10
# Kaugushüpe
# 	kasutaja sisestab 3 kaugushüppe tulemust - 1p
# 	sinu programm leiab ning väljastab parima ja keskmise tulemuse - 2p
# 	programmi dialoog kasutajaga on arusaadav ja õheselt mõistetav - 1p
# 	kood kommenteeritud - 1p

# Kaugushüppe programm

# tulemus1 = float(input("sisesta esimene tulemus meetrites: "))
# tulemus2 = float(input("sisesta teine tulemus meetrites: "))
# tulemus3 = float(input("sisesta kolmas tulemus meetrites: "))
# parimtulemus = max(tulemus1, tulemus2, tulemus3)
# keskminetulemus = (tulemus1 + tulemus2 + tulemus3) / 3
# print(f"parim tulemus: {parimtulemus} meetrit")
# print(f"keskmine tulemus: {keskminetulemus} meetrit")



#12
# Eurokalkulaator
# 	Koosta programm, mis kalkuleerib valuuta vastavalt kasutaja soovile EUR->EEK vÃµi EEK->EUR.
# 	Oluline on kasutada kahte funktsiooni!!

# def eur_to_eek(kogus):
#     midaiganes = 15.6466
#     tulemus = kogus * midaiganes
#     return tulemus

# def eek_to_eur(kogus):
#     midaiganes = 0.0639
#     tulemus = kogus * midaiganes
#     return tulemus

# def see():
#     print("eurokalkulaator")
#     valik = input("vali valuutavahetus 1 - EUR->EEK, 2 - EEK->EUR: ")

#     if valik == "1":
#         kogus = float(input("sisesta summa eurodes: "))
#         tulemus = eur_to_eek(kogus)
#         print(f"{kogus} eurot on {tulemus} Eesti krooni")
#     elif valik == "2":
#         kogus = float(input("sisesta summa Eesti kroonides: "))
#         tulemus = eek_to_eur(kogus)
#         print(f"{kogus} Eesti krooni on {tulemus} eurot")
#     else:
#         print("ei, vali 1 või 2")


#14
# Palkade võrdlus - Loo palk.txt fail töötajate nime, soo ja palganumbriga (10 töötajat).
# 	Koosta programm, mis analüüsib kas firmas toimub diskrimineerimist soo järgi. Selleks võrdle omavahel meeste ja naiste palkade keskmiseid, samuti meeste ja naiste kõige kõrgemat palka. Programm peab tegema otsuse.

# 	Hubert Hunt m 2340
# 	Siim Siil m 2570
# 	Märt Mäger m 1960
# 	Vilma Vihmauss n 2060
# 	Merike Metskits n 2250
# 	Kati Karu n 2370
# 	Elmar Elevant m 2900
# 	Timoteus Tigu m 2850
# 	Reet Rebane n 2340
# 	Kalev Kaamel m 2570
# 	Karmen Kass n 2120
# 	Kornelius Koer m 2250

# import math

# mhm = []

# with open(r'C:\Users\dzukov\Desktop\python\pythton\palk.txt') as f:
#     for line in f:
#         vaike = min(mhm)
#         suur = max(mhm)
#         keskmine = sum(mhm) / len(mhm)
#         print("suur:", suur)
#         print("vaike:", vaike)
#         print("kesk:", keskmine)

   





#16
# 16. TÃ¤ringud
# 	Kasutaja vÃµistleb kahe tÃ¤ringuga arvuti vastu. Kasutaja teeb pakkumise ning suurima tÃ¤ringupunktisumma vÃµitja saab laual oleva raha endale juurde. MÃ¤ng kestab kuni kummalgi on raha otsas.
# 	(Vihjed: kÃ¼si kasutajalt nime, kuva pidevalt konto seisu ja tÃ¤ringuviskeid, kasutajate raha hulga mÃ¤ngu alguses mÃ¤Ã¤rad sina)


# import random

# rahakott = 100
# panus = 10

# print("taringumang: voistle selle boti vastu")
# while rahakott >= panus:
#     print(f"sul on {rahakott} raha")
#     print(f"iga mängu panus on {panus} raha")
#     vastus = input("kas soovid mängida jah voi ei? ")

#     if vastus == 'ei':
#         break

#     rahakott = rahakott - panus
#     taring1 = random.randint(1, 6)
#     taring2 = random.randint(1, 6)
#     botitaring1 = random.randint(1, 6)
#     botitaring2 = random.randint(1, 6)
#     print(f"su taringud: {taring1}, {taring2}")
#     arvamus = int(input("arva ara: "))
#     summa = taring1 + taring2
#     botisumma = botitaring1 + botitaring2
#     print(f"boti taringud: {botitaring1}, {botitaring2}")
#     print(f"su taringute summa: {summa}")
#     print(f"boti taringute summa: {botisumma}")

#     if summa > botisumma:
#         rahakott = rahakott + panus
#         print("congrats, sa voitsid ja said moni")
#     elif summa < botisumma:
#         print("oled ise nuud bot, sa kaotasid. bot ise voitsis")
#     else:
#         print("viik, olete molemad botid")
