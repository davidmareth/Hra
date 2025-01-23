print("4. Vyrazit do tajuplné věže.")
def vez():
    print("\nZavítal jsi k tajuplné věži. Slyšíš jak vítr šustí korunamy stromů a obloha nad věží se neustále mění.")
    volba = input("Jsi si jistý, že chceš vstoupit do věže? (1 = Odejít, 2 = Vstoupit do věže): ")
    if volba == "1":
        print("Odcházíš od věže v pořádku, ale nic nezískáváš.")
        return 0
    elif volba == "2":
        print("Vztupuješ do věže, vidíš dveře a schody, které vedou nahoru i dolů. Dveře, kterými jsi přišel záhadně zmizely.")
def vstupni_mistnost():
    volba = input("\nMůžeš prozkoumat co se skrývá za dvěřmi nebo můžeš pokračovat po schodech nahoru (1 = Otevřít dveře, 2 = Pokračovat po schodech nahoru, 3 = Pokračovat po schodech dolů)")
    if volba == "1":
        print("Vstupuješ do temné místnosti kde se nachází truhla")
        volba == input("\n1 = Vrátit se do vstupní místnosti, 2 = Otevřít truhlu")
        if volba == "1":
            vstupni_mistnost()
        elif volba =="2":
            print("Truhla byla prázdná, nic nezískáváš a vracíš se do vstupní místnosti")
            vstupni_mistnost()
    elif volba == "2":
        print("Vydal jsi se po schodech nahoru a našel jsi další dveře.")
        volba = input("\n1 = Otevřít dveře, 2 = Vrátit se zpět")
        if volba == "1":
            print("V místnosti hoří louče a uprostřed vidíš oltář na kterém je otevřená kniha. Po boku vidíš knihovný s hromadou knih")
            volba = ("\n1 = Přečíst si knihu, 2 = Odejít z místnosti")
            if volba == "1":
                print("Přečetl jsi nahlas jednu stránku z knihy. Po chvíli se začne třást celá věž a citíš jak se v tobě probouzí neznámá síla")
                return 3
            elif volba == "2":
                vstupni_mistnost()           
    elif volba == "3":
        print("Postupuješ dolů po schodech. Najednou zakopneš a kutálíš se až úplně dolů. Po tom co jsi se otřepal z pádu se rozhlédneš kolem sebe a vidíš 3 truhly vedle sebe.")
        volba = input("\n1 = Otevřít truhlu na levo, 2 = Otevřít truhlu uprostřed, 3 = Otevřít truhlu na pravo, 4 = Vrátit se zpět")
        if volba == "1":
            print("Otevřel jsi truhlu a všimneš si, že ta truhla má zuby. Je však už pozdě a truhla po tobě skočí a sežere tě. No jo, byl to mimik")
            return -1
        elif volba == "2":
            print("Otevřel jsi truhlu. Vidíš v ní hromadu předmětů, ale žádný nevypadá, že by měl nějákou cenu. Krom teda jednoho, kterého si všimneš a vezmeš. Našel jsi artefakt, který ti přidává 2 body a 2 body síly")
            return 2
        elif volba == "3":
            print("Otevřel jsi truhlu. Vidíš v ní hromadu předmětů, ale žádný nevypadá, že by měl nějákou cenu. Odcházíš s prázdnou")
            vstupni_mistnost()
        else:
            vstupni_mistnost()
    else:
        print("Neplatná volba")
        vstupni_mistnost()
vez()
vstupni_mistnost()
