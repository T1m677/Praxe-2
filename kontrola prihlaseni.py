jmeno=(input("zadej jmeno a heslo"))
heslo=(input("zadej jmeno a heslo"))
nasel=False
with open("seznam hesel.txt","w") as file:
     for i in file:
         i=i.strip()
         pole=i.split(" ; ")
         if pole[0]==jmeno:
             if pole[1]==heslo:
                 print("PRISTUP POVOLEN")
                 nasel=True
                 break
if nasel:
    print("PRISTUP POVOLEN")
else:
    print("ZAKAZ PRISTUPU")