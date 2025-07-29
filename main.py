import requests

def filter_heroes(gender, is_working):

    if not isinstance(gender, str):
        raise TypeError("gender должен быть строкой")

    if not isinstance(is_working, bool):
        raise TypeError("is_working должен быть логическим значением")

    url = "https://akabab.github.io/superhero-api/api/all.json"
    response = requests.get(url)
    data = response.json()

    correct_heroes = []
    for hero in data:
        if hero["appearance"]["gender"] == gender.capitalize():
            if hero["work"]["occupation"] == "-" and is_working == False:
                correct_heroes.append(hero)
            elif hero["work"]["occupation"] != "-" and is_working == True:
                correct_heroes.append(hero)
            else:
                pass

    result = None
    max_height = 0
    for hero in correct_heroes:
        height, measurement_type = hero["appearance"]["height"][1].split(" ")
        height = int(float(height) * 100) if measurement_type == "meters" else int(height)

        if height > max_height:
            max_height = height
            result = hero

    return result


if __name__ == "__main__":
    print(filter_heroes("female", True))