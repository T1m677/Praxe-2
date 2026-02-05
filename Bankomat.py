   def zapis_do_souboru(castka):
       with open("ucet.txt","w") as f:
          f.write(str(castka+/n)


    def vklad():
       a=int(input("Zadej castku"))
       zapis_do_souboru(a)


    def vyber():
       b=int(input("Zadej castku"))
       zapis_do_souboru(-b)

    def zustatek():
        kolik=0

       return kolik

    # hlavni menu
     while True:
        uzivatel= int(input("1-vklad, 2 vyber, 3 zustatek, 0 konec"))
        if uzivatel==1:
            vklad()
        if uzivatel==2:
            vyber()
        if uzivatel==3:
            zustatek()
        if uzivatel==0:
            break