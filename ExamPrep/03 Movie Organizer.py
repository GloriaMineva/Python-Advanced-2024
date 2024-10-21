from collections import defaultdict
def movie_organizer(*catalogue):
    result = ''
    organiser = defaultdict(list)
    for title, genre in catalogue:
        organiser[genre].append(title)
    sorted_organiser = sorted(organiser.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    for sorted_genre, not_sorted_titles in sorted_organiser:
        result += f'{sorted_genre} - {len(not_sorted_titles)}\n'
        for title in sorted(not_sorted_titles):
            result += f'* {title}\n'
    return result


print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))

