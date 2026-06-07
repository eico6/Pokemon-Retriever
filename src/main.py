import requests

API_URL = "https://pokeapi.co/api/v2/pokemon/"


def get_pokemon(name):
    response = requests.get(API_URL + name.lower(), timeout=10)

    if response.status_code == 404:
        return None

    response.raise_for_status()
    return response.json()


def print_pokemon(pokemon):
    name = pokemon["name"].capitalize()
    weight = pokemon["weight"]
    height = pokemon["height"]
    base_experience = pokemon["base_experience"]

    print()
    print("╔══════════════════════════════╗")
    print("║        Pokémon Found!        ║")
    print("╠══════════════════════════════╣")
    print(f"║ Name            : {name:<10} ║")
    print(f"║ Weight          : {weight:<10} ║")
    print(f"║ Height          : {height:<10} ║")
    print(f"║ Base experience : {base_experience:<10} ║")
    print("╚══════════════════════════════╝")
    print()


def main():
    print("================================")
    print("        Pokémon Retriever       ")
    print("================================")
    print("Search for Pokémon by name.")
    print("Type 'quit' to exit.")
    print()

    while True:
        name = input("Enter Pokémon name: ").strip()

        if name.lower() == "quit":
            print("\nGoodbye! 👋")
            break

        if not name:
            print("\n⚠️  Please enter a Pokémon name.\n")
            continue

        try:
            pokemon = get_pokemon(name)

            if pokemon is None:
                print("\n❌ Pokémon not found. Try another name.\n")
            else:
                print_pokemon(pokemon)

        except requests.RequestException as error:
            print(f"\n⚠️  Could not contact PokéAPI: {error}\n")


if __name__ == "__main__":
    main()