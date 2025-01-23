import random
def uvod():
    print("\nVítej, zaklínači/n")
    print("Stojíš u cedule kde jsou 3 kontrakty. Můžeš si vybrat co chceš.")
    print("1. Zničit hnízdo harpyi na ztroskotané lodi")
    print("2. Porazit ghoula který se vyskytuje na bývalém bojišti")
    print("3. Porazit přízrak který napadá pozůstalé na hřbitově")

def uvod_h():
    print("\nVrátil ses zpět ceduli s kontrakty. Už jsou tady pouze 2./n")
    print("1. Porazit ghoula který se vyskytuje na bývalém bojišti")
    print("2. Porazit přízrak který napadá pozůstalé na hřbitově")

def boj_harpye():
    print("\nPřibližuješ se k hejnu. Všimli si tě, normální lidé by utekli ale tebe na tohle připravovali celý život./n") 
    #procenta na vyhru 
    if random.random() > 0.3:  # 70%
        print("\nPorazil si celé hejno a zničil jejich hnízdo.")
        uvod_h()
    else:
        print("\nBylo jich až moc. Musel si utéct.")
        uvod()
#moznost 2 u questu 1
def hnizdo():
    print("\nNad hlavou ti pořád lítá hejno, ale rozhodl ses jít přímo po hnízdu.")
    #procenta na vyhru
    if random.random() > 0.3:  # 70%
        print("\nÚspěšně si zničil hnízdo a celé hejno zmizelo.")
        uvod_h()
    else:
        print("\nZkusil si všechno co si mohl ale nic nefungovalo. Musel si utéct.")
        uvod()


def harpye():
    print("\nVstoupil si do ztroskotané lodi. Nad hlavou ti lítá hejno harpyí.")
    print("Hnízdo harpyí se nachází u kormidla. Musíš se k němu dostat.")
    print("Budeš bojovat s harpyemi přímo nebo zničíš hnízdo první?")
    print("Víš že můžeš harpye porazit, ale taky víš ze svého výcviku že pokud jim zničíš hnízdo tak se přehnízdí a v okolí nezůstanou.")
    print("Jaký přístup zvolíš?")
    volba = input("Zvol (1) pro boj s harpyemi, (2) pro zničení hnízda, (3) pro vrácení zpět na začátek ")
    #vyber pristupu k ukolu
    if volba == "1":
        boj_harpye()

    elif volba == "2":
        hnizdo()

    elif volba == "3":
        uvod()    

    else:
        print("Neplatná volba. Vyber 1, 2 nebo 3.")
        harpye() 


                    
   