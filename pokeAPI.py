import requests

basic_url = "https://pokeapi.co/api/v2/"
def get_pokemon_info(name): 
    url = f"{basic_url}/pokemon/{name}"
    response = requests.get(url)
    
    
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retrieve data {response.status_code}")
    



pokemon_name = input("Enter a pokemon name: ")
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"Name : {pokemon_info["name"]}")
    print(f"Height : {pokemon_info["height"]}cm/M")
    print(f"Weight : {pokemon_info["weight"]}Ibs")
    print(f"ID : {pokemon_info["id"]}")
    
    