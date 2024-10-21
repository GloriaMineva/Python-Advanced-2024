def draw_cards(*args, **kwargs):
    monsters = []
    spells = []
    result = ''
    for i in args:
        card_name, card_type = i
        if card_type == 'monster':
            monsters.append(card_name)
        else:
            spells.append(card_name)
    for dict_name, dict_type in kwargs.items():
        if dict_type == 'monster':
            monsters.append(dict_name)
        else:
            spells.append(dict_name)
    monsters = sorted(monsters, reverse=True)
    spells = sorted(spells)
    if monsters:
        result += 'Monster cards:\n'
        for monster in monsters:
            result += f'  ***{monster}\n'
    if spells:
        result += 'Spell cards:\n'
        for spell in spells:
            result += f'  $$${spell}\n'

    return result




print(draw_cards(("brave attack", "spell"), ("freeze", "spell"), lightning_bolt="spell", fireball="spell",))