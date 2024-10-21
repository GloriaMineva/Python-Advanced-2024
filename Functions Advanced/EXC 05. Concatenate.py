def concatenate(*some_words, **some_dict):
    result = ''.join(some_words)
    for key, value in some_dict.items():
        if key in result:
            result = result.replace(key, value)

    return result


print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))