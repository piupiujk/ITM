import os

with open('lorum.txt', 'w') as f:
    f.write('123')
    f.write('hello')


with os.scandir('.') as entries:
    for entry in entries:
        print(entry.name, '->', entry.stat().st_size, 'bytes')
