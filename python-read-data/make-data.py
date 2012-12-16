words = '''ad
adipisicing
aliqua
aliquip
amet
anim
aute
cillum
commodo
consectetur
consequat
culpa
cupidatat
deserunt
do
dolor
dolore
duis
ea
eiusmod
elit
enim
esse
est
et
eu
ex
excepteur
exercitation
fugiat
id
in
incididunt
ipsum
irure
labore
laboris
laborum
lorem
magna
minim
mollit
nisi
non
nostrud
nulla
occaecat
officia
pariatur
proident
qui
quis
reprehenderit
sed
sint
sit
sunt
tempor
ullamco
ut
velit
veniam
voluptate'''.split()

# Create the data in memory
data = []
for row in range(0, 1000000):
    data.append({
        'A': words[row % len(words)],
        'B': chr(64 + (row % 62)),
        'C': row,
        'D': row + 1,
        'E': row + 2,
        'F': row + 3,
    })

# Save CSV
import csv
keys = sorted(data[0].keys())
out = csv.DictWriter(open('data.csv', 'w'),
    fieldnames=keys,
    lineterminator='\n')
out.writerow(dict(zip(keys, keys)))
out.writerows(data)

# JSON
import json
json.dump(data, open('data.json', 'w'), separators= (',', ':'))

# JSON-array
import json
json.dump([data[0].keys()] + [row.values() for row in data],
    open('data-array.json', 'w'),
    separators= (',', ':'))

import cPickle as pickle
pickle.dump(data, open('data.pickle', 'wb'), pickle.HIGHEST_PROTOCOL)
