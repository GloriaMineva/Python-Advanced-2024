from collections import defaultdict
def team_lineup(*args):
    result = ''
    teams = defaultdict(list)
    for data in args:
        name, country = data
        teams[country].append(name)
    sorted_teams = sorted(teams.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    for countries, players in sorted_teams:
        result += f'{countries}:\n'
        for el in players:
            result += f'  -{el}\n'
    return result


print(team_lineup(
   ("Lionel Messi", "Argentina"),
   ("Neymar", "Brazil"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Harry Kane", "England"),
   ("Kylian Mbappe", "France"),
   ("Raheem Sterling", "England")))

