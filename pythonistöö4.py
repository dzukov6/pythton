#iseseisevtöö
#Daniel Zukov
#10.01.2024

import random

#4.1
# def banner(eh):
#     print(eh.upper()
#           )

# lokomotiv = int(input("kui palju: "))
# text = input("pane tekst: ")

# for i in range(lokomotiv):
#     banner(text)

#4.2

# def mahlapakkide_arv(kg):
#     mahlapakkidearv = round(kg * 0.4 / 3) 
#     return mahlapakkidearv

# applekogus = float(input("kui palju õune, võiks rünnata newtoni pead: "))
# print(mahlapakkide_arv(applekogus))

#4.3


#4.4
def tervitus(jrk):
    print("võõras: tere!")
    print(f" täna{jrk}, kord tervitada, mõtiskleb võõrustaja")
    print("külaline: tere,suur tänu kutse eest!")

    kylaliste_arv = int(input("mitu inimest oli kutsutud?: "))
    for i in range(kylaliste_arv):
        tervitus(i+1)





