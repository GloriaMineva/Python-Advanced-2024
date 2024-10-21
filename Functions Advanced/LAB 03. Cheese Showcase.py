def sorting_cheeses(**user_data):
    result = ''
    sorted_dict = sorted(user_data.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    for name, quantities_list in sorted_dict:
        result += f'{name}\n'
        sorted_quantites = sorted(quantities_list, reverse=True)
        for el in sorted_quantites:
            result += f'{el}\n'
    return result



print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
