import random
import string

def coin_flip():
    """
    Function to simulate a coin flip.
    Returns:
        str: The result of the coin flip - "Galva" (Heads) or "Astes" (Tails).
    """
    return random.choice(["Galva", "Astes"])

def multiple_coin_flips(num_flips):
    """
    Function to simulate multiple coin flips.
    Args:
        num_flips (int): Number of times the coin will be flipped.
    Returns:
        dict: A dictionary with the count of "Galva" and "Astes".
    """
    results = {"Galva": 0, "Astes": 0}
    flips = [coin_flip() for _ in range(num_flips)]
    for result in flips:
        results[result] += 1
    return results

def random_text_generator(word_count=1, use_real_words=True):
    """
    Function to generate random words.
    Args:
        word_count (int): Number of words to generate.
        use_real_words (bool): Whether to use a predefined list of real words.
    Returns:
        list: A list of randomly generated words.
    """
    word_list = [
        "ābols", "bumbieris", "ķirsis", "zemenes", "banāns","ābols", "bērns", "ceļš", "diena", "ezers", "futbols", "gads", "halva", "irbe", "jaka", "kakls", "lācis",
        "datums", "programma", "kaķis", "suns", "putns","māja", "nazis", "oga", "pils", "roka", "saule", "tirgus", "uguns", "vāze", "zāle", "āda", "bumba", "cūka",
        "mašīna", "māja", "skola", "universitāte", "grāmata", "dārzs", "ērkšķis", "grāmata", "hokejs", "īris", "jūra", "koks", "liepa", "mēness", "nīca",
        "ozols", "pērle", "rīkle", "siers", "tēja", "ūdens", "vārna", "zirgs", "ābele", "bikses", "cepure", "dators",
        "ērglis", "gurķis", "hamburgers", "iela", "jautājums", "kafija", "lampa", "punkts",
        "mākonis", "sirds", "banka", "dzelzceļš", "ērce", "zvaigzne", "kalns", "laiva", "medus", "naktssargs",
        "operācija", "pilsēta", "rīts", "sniegs", "tālrunis", "vējš", "zāģis", "ābolkoks", "bļoda", "cepums",
        "dāvana", "ērkšķogles", "gredzens", "hlorofils", "ievārījums", "jautrība", "kaktiņš", "lāpsta",
        "mārketings", "ņiprs", "mērkaķis", "pērtiķis", "rāpulis", "sēne", "trusis", "ūsas", "vārti", "zirneklis",
        "ātrums", "jaunība", "cīņa", "dūnas", "ērģeles", "glāze", "herbārijs", "intervija", "jūlijs", "kabata", "līmenis", "mīkla",

    ]
    generated_words = []
    if use_real_words:
        generated_words = [random.choice(word_list) for _ in range(word_count)]
    else:
        for _ in range(word_count):
            word_length = random.randint(3, 10)
            word = ''.join(random.choices(string.ascii_lowercase, k=word_length))
            generated_words.append(word)
    return generated_words

def generate_random_number(min_value, max_value):
    """
    Function to generate a random number within a given range.
    Args:
        min_value (int): The minimum value of the range.
        max_value (int): The maximum value of the range.
    Returns:
        int: A randomly generated number within the range.
    """
    return random.randint(min_value, max_value)

def display_menu():
    """
    Display a menu for the user to choose actions.
    """
    print("\nIzvēlies darbību:")
    print("1. Vienas monētas mešana")
    print("2. Vairāku monētu mešana")
    print("3. Random vārdu ģenerēšana")
    print("4. Ģenerēt random skaitli noteiktā vērtībā")
    print("5. Parādīt pēdējos rezultātus")
    print("6. Iziet no programmas")

def main():
    """
    Main function to run the program.
    """
    print("Laipni lūgti programmā!")
    print("Šeit jūs varat mest monētas, ģenerēt random vārdus vai skaitļus.")
    
    last_results = None  # To store the last results of any operation

    while True:
        display_menu()
        try:
            choice = int(input("\nIevadiet izvēles numuru (1, 2, 3, 4, 5 vai 6): "))
        except ValueError:
            print("Lūdzu, ievadiet derīgu numuru!")
            continue

        if choice == 1:
            print("\nMonētas mešanas spēle:")
            result = coin_flip()
            print(f"Rezultāts: {result}\n")
            last_results = f"Vienas monētas mešanas rezultāts: {result}"
        elif choice == 2:
            print("\nVairāku monētu mešanas spēle:")
            try:
                num_flips = int(input("Cik reizes vēlaties mest monētu? "))
                results = multiple_coin_flips(num_flips)
                print(f"Rezultāti pēc {num_flips} mešanas reizēm:")
                print(f"Galva: {results['Galva']}, Astes: {results['Astes']}\n")
                last_results = f"Vairāku monētu mešanas rezultāti: {results}"
            except ValueError:
                print("Lūdzu, ievadiet derīgu skaitli!")
        elif choice == 3:
            print("\nRandom vārdu ģenerators:")
            try:
                word_count = int(input("Cik vārdus vēlaties ģenerēt? "))
                use_real_words = input("Vai izmantot īstus vārdus? (jā/nē): ").strip().lower() == "jā"
                words = random_text_generator(word_count, use_real_words)
                print(f"Ģenerētie vārdi: {', '.join(words)}\n")
                last_results = f"Ģenerētie vārdi: {', '.join(words)}"
            except ValueError:
                print("Lūdzu, ievadiet derīgu skaitli!")
        elif choice == 4:
            print("\nNejauša skaitļa ģenerators:")
            try:
                min_value = int(input("Ievadiet minimālo vērtību: "))
                max_value = int(input("Ievadiet maksimālo vērtību: "))
                if min_value > max_value:
                    print("Minimālajai vērtībai jābūt mazākai vai vienādai ar maksimālo vērtību!")
                    continue
                random_number = generate_random_number(min_value, max_value)
                print(f"Random ģenerētais skaitlis vērtībā ({min_value}, {max_value}): {random_number}\n")
                last_results = f"Random ģenerētais skaitlis: {random_number}"
            except ValueError:
                print("Lūdzu, ievadiet derīgas skaitliskas vērtības!")
        elif choice == 5:
            print("\nPēdējie rezultāti:")
            if last_results:
                print(last_results)
            else:
                print("Nav datu par pēdējiem rezultātiem.\n")
        elif choice == 6:
            print("\nPaldies, ka izmantojāt programmu! Tiekamies atkal!")
            break
        else:
            print("Lūdzu, izvēlieties derīgu opciju (1, 2, 3, 4, 5 vai 6).")

if __name__ == "__main__":
    main()