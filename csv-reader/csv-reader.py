import time
import csv
import pandas as pd
import tabular

t0 = time.time()
data = list(csv.reader(open('data.csv')))
t1 = time.time()

data = list(csv.DictReader(open('data.csv')))
t2 = time.time()

data = pd.read_csv('data.csv')
t3 = time.time()

data = tabular.tabarray(SVfile='data.csv', headerlines=1, verbosity=0)
t4 = time.time()

print 'csv.reader: %d ms, csv.DictReader: %d ms, pandas: %d ms, tabular: %d ms' % (
    int((t1 - t0) * 1000),
    int((t2 - t1) * 1000),
    int((t3 - t2) * 1000),
    int((t4 - t3) * 1000),
)
