import os
command = input()
while command != 'End':
    action = command.split('-')[0]
    file_name = command.split('-')[1]
    if action == 'Create':
        with open(file_name, 'w'): pass
    elif action == 'Add':
        content = command.split('-')[2]
        with open(file_name, 'a') as file_name:
            file_name.write(content)
            file_name.write('\n')
    elif action == 'Replace':
        old_string = command.split('-')[2]
        new_string = command.split('-')[3]
        try:
            with open(file_name, 'r+') as file_name:
                text = file_name.read()
                file_name.seek(0)
                file_name.truncate(0)
                file_name.write(text.replace(old_string, new_string))
        except FileNotFoundError:
            print('An error occurred')
    elif action == 'Delete':
        try:
            os.remove(file_name)
        except FileNotFoundError:
            print('An error occurred')
    command = input()