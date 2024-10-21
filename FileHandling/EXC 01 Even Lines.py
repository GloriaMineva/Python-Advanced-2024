symbols = ("-", ",", ".", "!", "?")

with open("text.txt", "r") as even_lines_file:
    text = even_lines_file.readlines()

for row in range(0, len(text), 2):

    for symbol in symbols:
        text[row] = text[row].replace(symbol, "@")
    # first option split + join
    # to_be_reversed = text[row].split()
    # print(' '.join(to_be_reversed[::-1]))
    # second option with unpacking:
    print(*text[row].split()[::-1])
