def cookbook(*recipes):
    cook_dict = {}

    for current_recipe in recipes:
        recipe = current_recipe[0]
        cuisine = current_recipe[1]
        ingredient = current_recipe[2]
        if cuisine not in cook_dict:
            cook_dict[cuisine] = []
        cook_dict[cuisine].append((recipe, ingredient))

    sorted_cook_dict = sorted(cook_dict.keys(), key=lambda x: (-len(cook_dict[x]), x))

    result = ''
    for cuisine in sorted_cook_dict:
        result += f'{cuisine} cuisine contains {len(cook_dict[cuisine])} recipes:\n'
        sorted_recipes = sorted(cook_dict[cuisine], key=lambda x: x[0])
        for recipe in sorted_recipes:
            result += f'  * {recipe[0]} -> Ingredients: {", ".join(recipe[1])}\n'

    return result


print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
    ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
    ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
    ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"])
    ))