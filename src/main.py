import requests

API_URL = "https://pokeapi.co/api/v2/pokemon/"
REQUEST_TIMEOUT = 10


def get_pokemon(name: str) -> dict | None:
    """Fetch Pokémon data from PokéAPI. Returns None if not found."""
    response = requests.get(API_URL + name.lower(), timeout=REQUEST_TIMEOUT)

    if response.status_code == 404:
        return None

    response.raise_for_status()
    return response.json()


def print_pokemon(pokemon: dict) -> None:
    """Print Pokémon information in a pretty format."""
    name = pokemon["name"].capitalize()
    weight = pokemon["weight"] / 10 # hectorgram -> kg
    height = pokemon["height"] / 10 # decimeter  -> meter
    base_experience = pokemon["base_experience"]
    
    print()
    print(f"╔══════════════════════════════╗")
    print(f"║        Pokémon Found!        ║")
    print(f"╠══════════════════════════════╣")
    print(f"║ Name            : {name:<10} ║")
    print(f"║ Weight          : {str(weight) + ' kg':<10} ║")
    print(f"║ Height          : {str(height) + ' m':<10} ║")
    print(f"║ Base experience : {base_experience:<10} ║")
    print(f"╚══════════════════════════════╝")
    print()


def main() -> None:
    """Run the application."""
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