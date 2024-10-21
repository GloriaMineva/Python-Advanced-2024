def math_operations(*numbers_float, **elements_dict):
    for el_index in range(len(numbers_float)):
        if (el_index + 1) % 4 == 0:
            elements_dict['m'] *= float(numbers_float[el_index])
        elif (el_index + 1) % 4 == 3:
            if float(numbers_float[el_index]) != 0:
                elements_dict['d'] /= float(numbers_float[el_index])
        elif (el_index + 1) % 4 == 2:
            elements_dict['s'] -= float(numbers_float[el_index])
        elif (el_index + 1) % 4 == 1:
            elements_dict['a'] += float(numbers_float[el_index])
    sorted_elements = sorted(elements_dict.items(), key=lambda kvp: (-kvp[1], kvp[0]))
    result = []
    for k, v in sorted_elements:
        result.append(f'{k}: {v:.1f}')
    return '\n'.join(result)


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))


