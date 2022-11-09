from sys import exit


from pojistenec import Pojistenec


class Evidence:

    def __init__(self, soubor):
        self.soubor = soubor

    def pridej_pojistence(self, pojistenec):
        pojistenci = Pojistenec(self.jmeno, self.prijmeni,self.vek,self.telefon)


    def vypis_vsechny(self, pojistenci):
        return self.pojistenci

    def vyhledej_pojistence(self, pojistenec):
        return self.pojistenec



print("EVIDENCE POJIŠTĚNÝCH")

pojistenci = []

pokracovat = "ano"
while (pokracovat =="ano"):
    print("Vyber si akci: ")
    print("1 - Přidat nového pojištěnce ")
    print("2 - Vypsat všechny pojištěnce ")
    print("3 - Vyhledat pojištěnce ")
    print("4 - Konec ")
    akce = int(input(""))

    if(akce == 1):
        jmeno = input("Zadej jméno pojištěného \n")
        prijmeni = input("Zadej příjmení pojištěného \n")
        vek = int(input("Zadej věk pojištěného \n"))
        telefon = int(input("Zadej telefonní číslo pojištěného \n"))
        pojistenci.append(Pojistenec(jmeno,prijmeni,vek,telefon))
        print("Pokračuj klávesou enter \n")

    elif(akce ==2):
       for pojistenec in pojistenci:
            print(pojistenec)
    elif(akce == 3):
        print("Podle čeho chcete vyhledávat? \n")
        print("Vyberte možnost: \n")
        print("1 - podle jména a příjmení  \n")
        print("2 - podle telefonního čísla: \n")
        moznost = int(input(""))
        if(moznost == 1):
            hledane_jmeno = input("Zadejte jméno pojištěnce, kterého hledáte \n")
            hledane_prijmeni = input("Zadejte příjmení, které hledáte \n")
            for pojistenec in pojistenci:
                if hledane_jmeno == pojistenec.jmeno and hledane_prijmeni == pojistenec.prijmeni:
                    print(pojistenec)
        else:
            moznost == 2
            hledany_telefon = int(input("Zadejte telefonní čílo, podle kterého chcete hledat: \n"))
            for pojistenec in pojistenci:
                print(pojistenec)
    else:
        (akce == 4)
        exit()



p1 = Pojistenec(jmeno, prijmeni,vek, telefon)
print(vypis_vsechny)
