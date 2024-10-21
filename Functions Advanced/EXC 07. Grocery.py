def grocery_store(**products):
    sorted_products = dict(sorted(products.items(), key=lambda kvp: (-kvp[1], -len(kvp[0]), kvp[0])))
    result = []
    for k, v in sorted_products.items():
        result.append(f'{k}: {v}')
    return '\n'.join(result)


print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))

