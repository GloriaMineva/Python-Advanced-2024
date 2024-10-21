from string import punctuation
with open('text.txt') as file:
    text = file.readlines()

with open('output.txt', 'w') as output:
    for row in range(len(text)):
        letter_counter = 0
        marks_counter = 0
        for el in text[row]:
            if el.isalpha():
                letter_counter += 1
            elif el in punctuation:
                marks_counter += 1
        output.write(f'Line {row + 1}: {text[row][:-1]} ({letter_counter})({marks_counter})\n')
