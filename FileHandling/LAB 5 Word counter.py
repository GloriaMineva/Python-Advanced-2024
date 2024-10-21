import re
occ = {}
with open('words.txt') as file:
    words = file.read().split()
with open('input.txt') as file:
    input_data = file.read()
for word in words:
    pattern = rf'\b{word}\b'
    result = re.findall(pattern, input_data, re.IGNORECASE)
    occ[word] = len(result)
print(occ)
sorted_occ = dict(sorted(occ.items(), key=lambda kvp: -kvp[1]))
result = ''
for k, v in sorted_occ.items():
    result += f'{k} - {v}\n'
print(result)

with open('output.txt', 'a') as file:
    file.write(result)