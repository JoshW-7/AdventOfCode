import copy


with open("input.txt") as file:
    lines = file.read().split("\n")
    foods = []
    for line in lines:
        ingredients = line.split(" (")[0].split(" ")
        known_allergens = line[line.find("(contains ") + len("(contains "):-1].split(", ")
        foods.append({
            "ingredients": set(ingredients),
            "known_allergens": set(known_allergens),
        })

allergens = set()
for food in foods:
    allergens |= food["known_allergens"]

allergen_data = {}
for allergen in allergens:
    allergen_data[allergen] = {
        "potential_ingredients": set(),
        "foods": set(),
    }
    for i,food in enumerate(foods):
        if allergen in food["known_allergens"]:
            allergen_data[allergen]["foods"].add(i)
            for ingredient in food["ingredients"]:
                if ingredient not in allergen_data[allergen]["potential_ingredients"]:
                    allergen_data[allergen]["potential_ingredients"].add(ingredient)

all_found = False
found_ingredients = set()
while not all_found:
    all_found = True
    for allergen,data in allergen_data.items():
        if "name" in data:
            continue
        all_found = False
        first = True
        for food_number in data["foods"]:
            if first:
                shared = foods[food_number]["ingredients"] - found_ingredients
                first = False
            else:
                shared = shared.intersection(foods[food_number]["ingredients"])
        if len(shared) == 1:
            data["name"] = shared.pop()
            found_ingredients.add(data["name"])

count = 0
for food in foods:
    for ingredient in food["ingredients"]:
        if ingredient not in found_ingredients:
            count += 1

translation_list = []
for allergen,data in allergen_data.items():
    translation_list.append((allergen, data["name"]))
translation_list.sort(key=lambda t: t[0])
print(",".join([t[1] for t in translation_list]))