algebraic_expression = input()
stack_indexes = []
extraction = ''
for i in range(len(algebraic_expression)):
    if algebraic_expression[i] == '(':
        stack_indexes.append(i)
    if algebraic_expression[i] == ')':
        starting_index = stack_indexes[-1]
        stack_indexes.pop()
        end_index = i + 1
        extraction = algebraic_expression[starting_index:end_index]
        print(extraction)


