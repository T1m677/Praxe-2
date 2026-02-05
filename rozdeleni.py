with open("Malta.txt","r") as file:
        radky= f.readlines()
delici= int(input("Zadej delici cislo:"))

with open("mala.txt","w") as f:
       for i in radky:
           cislo_cs= int (i)
           if cislo_cs<=delici:
              f.write(i)
with open("vychovujici.txt","r") as file:
    for i in radky:
        cislo_cs= int(i)
        if cislo_cs>= int(i):
                  f.wtite(i)

