elements = []

while True:
    a = input('enter element or type quit: ')
    if a != 'quit':
        elements += [a]
    else:
        break

print('Elements:', elements)