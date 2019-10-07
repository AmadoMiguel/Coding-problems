
def groupingDishes(dishes):
    ingredAndDishes = {}
    # Iterate over the dishes parent array and collect information in
    # a map
    for items in dishes:
        # Iterate over the ingredients only
        for ingred in items[1:]:
            if ingred in ingredAndDishes.keys():
                ingredAndDishes[ingred].append(items[0])
            else:
                ingredAndDishes[ingred] = [items[0]]
    # Now, check number of meals per ingredient
    finalInfo = []
    for ingred, meals in ingredAndDishes.items():
        if len(meals) <= 1:
            continue
        finalInfo.append([ingred]+list(sorted(meals)))
    return list(sorted(finalInfo))
