import random as rand
import sys

from item import Item
from monster import Monster
from player import Player

RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

def menu():
    p1 = Player(10, 3, 1)
    svar = ""
    while svar != "q":
        
        sys.stdout.write(BOLD)
        svar = input(
            "\nVad vill du göra? Inventory [i], Stats [s], Dörr [d], Avsluta [q] ")
        sys.stdout.write(RESET)

        if svar == "s":
            print("\nstrength", p1.strength)
            print("hp", p1.hp)
            print("lvl", p1.lvl)

        elif svar == "i":
            visainv(p1)

        elif svar == "d":
            door(p1)

        if p1.hp < 1:
            break

def door(p1):
    svar = ""
    while svar != "q":
        slumptal = rand.randint(0, 2)
        listalängd = list(range(0, 2))
        sys.stdout.write(BOLD)
        svar = input(
            "\nDu står i ett rum med tre dörrar framför dig. Vänster [v], Mitten [m], Höger [h], Avsluta [q] ")
        sys.stdout.write(RESET)
        if svar == "v":
            if slumptal == 0:
                p1 = fälla(p1)
                return(p1)

            elif slumptal == 1:
                p1 = fåitem(p1)
                return(p1)

            elif slumptal == 2:
                p1 = mötmonster(p1)
                return(p1)

        elif svar == "m":
            if slumptal == 0:
                p1 = fälla(p1)
                return(p1)

            elif slumptal == 1:
                p1 = fåitem(p1)
                return(p1)

            elif slumptal == 2:
                p1 = mötmonster(p1)
                return(p1)

        elif svar == "h":
            if slumptal == 0:
                p1 = fälla(p1)
                return(p1)

            elif slumptal == 1:
                p1 = fåitem(p1)
                return(p1)

            elif slumptal == 2:
                p1 = mötmonster(p1)
                return(p1)

def fälla(p1):
    tal = rand.randint(1, 3)
    if tal == 1:
        sys.stdout.write(RED)
        print("\nDu gick på en spike-trap och förlorade 1 hp")
        sys.stdout.write(RESET)
        p1.hp -= 1
    elif tal == 2:
        sys.stdout.write(RED)
        print("\nDu gick in i en vattenpöl och blev blöt. Du Förlora 1 hp")
        sys.stdout.write(RESET)
        p1.hp -= 1

    elif tal == 3:
        sys.stdout.write(RED)
        print("\nDu gick på en landmina och sprängdes up. Du förlorar 6 hp")
        sys.stdout.write(RESET)
        p1.hp -= 6
    return p1

def bytitem(p1, tilldelat_item):
    for item in p1.inventory:
        print(f"\n{p1.inventory.index(item)+1}: {item.name} strength: {item.strength_bonus} hp: {item.hp_bonus} Lvl: {item.lvl_bonus}")
    while True:
        try:
            sys.stdout.write(BOLD)
            svar = input("\nVilket item vill du byta ut? [1] [2] [3] [4] [5] [q] ")
            sys.stdout.write(RESET)
            if svar == "1":
                p1.inventory[0] = tilldelat_item
                return p1
            elif svar == "2":
                p1.inventory[1] = tilldelat_item
                return p1
            elif svar == "3":
                p1.inventory[2] = tilldelat_item
                return p1
            elif svar == "4":
                p1.inventory[3] = tilldelat_item
                return p1
            elif svar == "5":
                p1.inventory[4] = tilldelat_item
                return p1
            elif svar not in ["1", "2", "3", "4", "5", "q"]:
                raise ValueError
        except(ValueError):
                pass

        return p1 

def fåitem(p1):
    """Ger spelaren ett item eller låter hen byta.
    
    Först använder vi en if-sats för att kolla om Spelaren har fler items än 5, då ger vi 
    spelaren möjlighet att byta ut ett item, Vi kontrollerar spelarens input med en try-sats, 
    om spelaren svarar nej, appendas ett slumpat item till spelarens inventory. 
    
    Parameters: 
        p1: Ett spelar-objekt.

    Returns:
        p1: Samma spelar objekt.

    Raises:
        ValueError: Om spelaren trycker på fel tangent. 
    
    """
    Kaffe = Item("Kaffe", 2, -1, 0)
  
    Äppeljuice = Item("Äppeljuice", 1, 1, 0)

    Choklad = Item("Choklad", 0, 2, 0)

    hjärna = Item("Hjärna", 1, -3, 0)

    corny_big = Item("Corny big", 2, 2, 0)

    gainomax = Item("Gainomax", 6, 1, 0)

    konstig_kaka = Item("Konstig kaka", 0, -8, 3)

    itemslist = [Äppeljuice, Äppeljuice,Kaffe, Choklad, hjärna, corny_big, gainomax, konstig_kaka] 

    tilldelat_item = rand.choice(itemslist)

    
    if len(p1.inventory) == 5:
        while True:
            sys.stdout.write(BOLD)
            svar = input(f"\nDu hittade {tilldelat_item.name}! men ditt inventory är fullt. Vill du byta ut ett föremål? [y] [n] ")
            sys.stdout.write(RESET)
            try:
                if svar not in ["y","n"]:
                    raise ValueError
                elif svar == "y":
                    bytitem(p1, tilldelat_item)
                    return p1
                else:
                    break
            except(ValueError):
                pass


    else:
        Kaffe = Item("Kaffe", 2, -1, 0)
  
        Äppeljuice = Item("Äppeljuice", 1, 1, 0)

        Choklad = Item("Choklad", 0, 2, 0)

        hjärna = Item("Hjärna", 1, -3, 0)

        corny_big = Item("Corny big", 2, 2, 0)

        gainomax = Item("Gainomax", 6, 1, 0)

        konstig_kaka = Item("Konstig kaka", 0, -7, 1)

        itemslist = [Äppeljuice, Äppeljuice,Kaffe, Choklad, hjärna, corny_big, gainomax, konstig_kaka] 

        tilldelat_item = rand.choice(itemslist) 

        p1.inventory.append(tilldelat_item)
        sys.stdout.write(GREEN)
        print(f"\nDu hittade {tilldelat_item.name}!")
        sys.stdout.write(RESET)
    return p1

def visainv(p1):
    
    svar = ""
    while svar != "q":
        if len(p1.inventory) == 0:
            sys.stdout.write(RED)
            print("\nDitt inventory är tomt")
            sys.stdout.write(RESET)
        else: 

            for item in p1.inventory:
            
                print(f"\n{p1.inventory.index(item)+1}: {item.name} strength: {item.strength_bonus} hp: {item.hp_bonus} Lvl: {item.lvl_bonus}")

        try:
            sys.stdout.write(BOLD)
            svar = input("\nVilket item vill du använda? [1] [2] [3] [4] [5] [q] ")
            sys.stdout.write(RESET)
            if svar == "1":
                target_item = list.pop(p1.inventory, 0)
                p1.hp += target_item.hp_bonus
                p1.strength += target_item.strength_bonus
                p1.lvl += target_item.lvl_bonus
                sys.stdout.write(BOLD)
                print(f"\nDu använde {target_item.name} och fick {target_item.hp_bonus} hp och {target_item.strength_bonus} styrka")
                sys.stdout.write(RESET)
            elif svar == "2":
                target_item = list.pop(p1.inventory, 1)
                p1.hp += target_item.hp_bonus
                p1.strength += target_item.strength_bonus
                p1.lvl += target_item.lvl_bonus
                sys.stdout.write(BOLD)
                print(f"\nDu använde {target_item.name} och fick {target_item.hp_bonus} hp och {target_item.strength_bonus} styrka")
                sys.stdout.write(RESET)
            elif svar == "3":
                target_item = list.pop(p1.inventory, 2)
                p1.hp += target_item.hp_bonus
                p1.strength += target_item.strength_bonus
                p1.lvl += target_item.lvl_bonus
                sys.stdout.write(BOLD)
                print(f"\nDu använde {target_item.name} och fick {target_item.hp_bonus} hp och {target_item.strength_bonus} styrka")
                sys.stdout.write(RESET)
            elif svar == "4":
                target_item = list.pop(p1.inventory, 2)
                p1.hp += target_item.hp_bonus
                p1.strength += target_item.strength_bonus
                p1.lvl += target_item.lvl_bonus
                sys.stdout.write(BOLD)
                print(f"\nDu använde {target_item.name} och fick {target_item.hp_bonus} hp och {target_item.strength_bonus} styrka")
                sys.stdout.write(RESET)
            elif svar == "5":
                target_item = list.pop(p1.inventory, 2)
                p1.hp += target_item.hp_bonus
                p1.strength += target_item.strength_bonus
                p1.lvl += target_item.lvl_bonus
                sys.stdout.write(BOLD)
                print(f"\nDu använde {target_item.name} och fick {target_item.hp_bonus} hp och {target_item.strength_bonus} styrka")
                sys.stdout.write(RESET)
                

        except(IndexError, TypeError):
            pass

    return p1 

def mötmonster(p1):
    monsterlista = [Monster("skeleton", 5), Monster("Zombie", 3), Monster("Goblin", 1), Monster("Drake", 10), Monster("råtta", 0), Monster("Mimic", 6), Monster("annan ädventyrare", p1.strength + 1)]
    fiende = rand.choice(monsterlista)
    print(f"\nDu träffade på en {fiende.name} med {fiende.strength} styrka!" )
    if p1.strength > fiende.strength:
        sys.stdout.write(GREEN)
        print("Du vann och gick upp i level!")
        sys.stdout.write(RESET)
        p1.lvl += 1
        if p1.lvl >= 10:
            sys.stdout.write(GREEN)
            print("Du vann spelet!")
            sys.stdout.write(RESET)
            sys.exit()
        return p1

    elif p1.strength == fiende.strength:
        print("Ni var lika starka, ingenting hände")

    elif p1.strength < fiende.strength:
        sys.stdout.write(RED)
        print("Du förlorade och tog 1 skada")
        sys.stdout.write(RESET)
        p1.hp -= 1
        
        return p1

if __name__ == "__main__":
    menu()

    sys.stdout.write(RED)
    print("\nGAME OVER")
    sys.stdout.write(RESET)
    svar = ""
    while svar != "q":
        sys.stdout.write(BOLD)
        svar = input("\nVill du pröva igen? [y] Vill du avsluta [n] ")
        sys.stdout.write(RESET)
        if svar == "y":
            menu()

        elif svar == "n":
            sys.exit()
