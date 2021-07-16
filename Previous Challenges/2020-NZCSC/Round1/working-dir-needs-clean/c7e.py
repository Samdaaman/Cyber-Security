names = [
    'Khnumhotep',
    'Khnumhotep 2',
    'Khnumhotep II',
    'Khnumhotep ii',
    'Beni Hasan',
    'Beni Hasan 3',
    'BH3',
    'Niankhkhnum'
]

for name in names:
    add = name.lower()
    if add not in names:
        names.append(add)

for name in names:
    add = name.replace(' ', '')
    if add not in names:
        names.append(add)

print(names)
for name in names:
    print(name)
