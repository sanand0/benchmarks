import time
import csv
import json
import cPickle as pickle

t0 = time.time()
data = list(csv.reader(open('data.csv')))
t1 = time.time()

data = json.load(open('data.json'))
t2 = time.time()

data = json.load(open('data-array.json'))
t3 = time.time()

data = pickle.load(open('data.pickle', 'rb'))
t4 = time.time()

print 'csv: %d ms, json: %d ms, json-array: %d ms, pickle: %d ms' % (
    int((t1 - t0) * 1000),
    int((t2 - t1) * 1000),
    int((t3 - t2) * 1000),
    int((t4 - t3) * 1000),
)
