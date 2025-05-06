import random

#import random

# Funkcija simpātijas vārda random ģenerēšanai
def generate_crush_name():
    """
    Function to randomly generate a name for the crush.
    Returns:
        str: A randomly chosen name.
    """
    names = [
        "Jānim", "Kristapam", "Mārtiņam", "Tomasam", "Edgaram",
        "Robertam", "Ralfam", "Kārlim", "Artūram", "Dāvim",
        "Elvim", "Laurim", "Chimpanzini Banini", "Arvilam", "Arvīdam",
        "Bruno", "Matīsam", "Patrikam", "Verneram", "Reinim"
    ]
    return random.choice(names)

# Funkcija ievades validācijai
def get_user_input(prompt, options):
    while True:
        choice = input(prompt).strip().lower()
        if choice in options:
            return choice
        print(f"Nepareiza izvēle! Lūdzu, izvēlies no {', '.join(options)}.")

def dressing_game():
    # Ģenerēt simpātijas vārdu
    crush_name = generate_crush_name()
    print(f"Rīts! Tev jāizvēlas, ko vilkt uz skolu, lai iepatiktos {crush_name}...\n")

    # 1. Apģērba veida izvēle
    outfit_type = get_user_input("Izvēlies apģērba veidu (kleita / bikses un krekls / šorti un krekls / svārki un krekls): ",
                                 ['kleita', 'bikses un krekls', 'šorti un krekls', 'svārki un krekls'])

    # 2. Krāsas un rakstu izvēle
    if outfit_type == 'kleita':
        color = get_user_input("Izvēlies kleitas krāsu (rozā / melna / balta / zila / violeta / zaļa): ",
                               ['rozā', 'melna', 'balta', 'zila', 'violeta', 'zaļa'])
        print(f"Tu izvēlējies {color} kleitu — Laba izvēle queen!")
    else:
        pattern = get_user_input("Izvēlies krekla rakstu (leoparda / zebras / puķains / strīpains / punktains / bez raksta): ",
                                 ['leoparda', 'zebras', 'puķains', 'strīpains', 'punktains', 'bez raksta'])
        print(f"Tu izvēlējies {pattern} raksta kreklu.")
        if outfit_type == 'bikses un krekls':
            bottom_color = get_user_input("Izvēlies bikšu krāsu (gaiši zilas / tumši zilas / melnas / baltas / brūnas): ",
                                          ['gaiši zilas', 'tumši zilas', 'melnas', 'baltas', 'brūnas'])
            print(f"Tu izvēlējies {bottom_color} bikses.")
        elif outfit_type == 'šorti un krekls':
            bottom_color = get_user_input("Izvēlies šortu krāsu (gaiši zilus / tumši zilus / melnus / baltus / brūnus): ",
                                          ['gaiši zilus', 'tumši zilus', 'melnus', 'baltus', 'brūnus'])
            print(f"Tu izvēlējies {bottom_color} šortus.")
        elif outfit_type == 'svārki un krekls':
            bottom_color = get_user_input("Izvēlies svārku krāsu (gaiši zilus / tumši zilus / melnus / baltus / brūnus): ",
                                          ['gaiši zilus', 'tumši zilus', 'melnus', 'baltus', 'brūnus'])
            print(f"Tu izvēlējies {bottom_color} svārkus.")

    # 3. Mati
    hair = get_user_input("Kāda frizūra? (izlaisti / copē / bizēs / kā ir tā ir / buzzcut ): ", ['izlaisti', 'copē', 'bizēs', 'kā ir tā ir', 'buzzcut'])
    print(f"Tava izvēle: {hair}.")
    
    # Spēle beidzas, ja izvēlas buzzcut
    if hair == 'buzzcut':
        print("Labāk uzvelc parūku. Spēle beigusies!")
        return  # Beidz funkcijas izpildi

    # 4. Apavi
    shoes = get_user_input("Apavi? (kedas / platformas / augstpapēži / čības): ", ['kedas', 'platformas', 'augstpapēži', 'čības'])
    print(f"Tava izvēle: {shoes}.")

    # Spēle beidzas, ja izvēlas čības
    if shoes == 'čības':
        print("Nu girl, kas tas. Spēle beigusies!")
        return  # Beidz funkcijas izpildi

    # 5. Garastāvoklis
    mood = get_user_input("Kāds ir Tavs garastāvoklis? (labs / slikts): ", ['labs', 'slikts'])
    if mood == 'labs':
        mood_bonus = 8
        print(f"Yaas!")
    else:
        mood_bonus = -10
        print(f"Lift up your head queen, your crown is falling")

    # Bonuss
    crush_notice_chance = mood_bonus
    if outfit_type == 'kleita' and color in ['rozā', 'balts']:
        crush_notice_chance += 20
    if outfit_type in ['bikses un krekls', 'šorti un krekls', 'svārki un krekls'] and pattern in ['leoparda', 'bez raksta']:
        crush_notice_chance += 6
    if hair == 'izlaisti':
        crush_notice_chance += 40
    if shoes in ['platformas', 'augstpapēži']:
        crush_notice_chance += 10

    # Rezultāts
    roll = random.randint(-100, 100)
    print(f"\nViņš ({crush_name}) lingero pie tevis")
    print(f"(Tavs liktenis ir laimes rokās: {roll}, tavs score: {crush_notice_chance})")

    if crush_notice_chance + roll >= 40:
        print(f"Go diva! {crush_name} pienāk un saka: 'Čau skaistule'")
    elif crush_notice_chance + roll >= 10:
        print(f"{crush_name} uzmet aci un smaida... Tu esi out of his league tā pat!")
    else:
        print(f"{crush_name} tevi nepamana... Tev vajag fashion advice!")

# Starta punkts
if __name__ == "__main__":
    dressing_game()