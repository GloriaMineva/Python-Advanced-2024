def cookbook(*recipes):
    result = ''
    by_country = {}
    for recipe in recipes:
        name, country, ingredients = recipe
        if country not in by_country:
            by_country[country] = {}
        by_country[country][name] = ingredients

    sorted_by_country = dict(sorted(by_country.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])))
    for location, data in sorted_by_country.items():
        result += f'{location} cuisine contains {len(data)} recipes:\n'
        sorted_data = dict(sorted(data.items(), key=lambda kvp: kvp[0]))
        for data_name, data_ingredients in sorted_data.items():
            result += f"  * {data_name} -> Ingredients: {', '.join(data_ingredients)}\n"
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





