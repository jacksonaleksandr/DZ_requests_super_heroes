import requests
TOKEN = "2619421814940190"
superheroes = ["Hulk", "Captain America", "Thanos"]
action = "/search/"


def super_hero(superheroes):
    hero_list = []
    intelligence_list = []
    url = "https://superheroapi.com/api/"
    for hero in superheroes:
        response = requests.get(url + TOKEN + action + hero)
        response_json = response.json()
        for item in response_json["results"]:
            if item["name"] == hero:
                hero_list.append(int(item["powerstats"]["intelligence"]))
                intelligence_list.append(item["name"])
    united_list = zip(hero_list, intelligence_list)
    united_list_sorted = sorted(united_list)
    print(
        f"А самый умный в этой тройке игроков {united_list_sorted[-1][1]}, {united_list_sorted[-1][0]} очков у победителя.")


super_hero(superheroes)
