import time
import csv
import json
import cPickle as pickle
import pandas as pd
import tabular

def timing(label, fn):
    t0 = time.time()
    fn()
    t1 = time.time()
    print '%s: %d ms' % (label, int((t1 - t0) * 1000))

timing('csv.reader',            lambda: list(csv.reader(open('data.csv'))))
timing('csv.DictReader',        lambda: list(csv.DictReader(open('data.csv'))))
timing('json',                  lambda: json.load(open('data.json')))
timing('json-array',            lambda: json.load(open('data-array.json')))
timing('tabular.tabarray',      lambda: tabular.tabarray(SVfile='data.csv', headerlines=1, verbosity=0))
timing('pickle',                lambda: pickle.load(open('data.pickle', 'rb')))
timing('pandas.load',           lambda: pd.load('data.pandas'))
timing('pandas.read_csv',       lambda: pd.read_csv('data.csv'))
timing('pandas.read_csv:gz',    lambda: pd.read_csv('data.csv.gz', compression='gzip'))
timing('pandas.read_csv:bz2',   lambda: pd.read_csv('data.csv.bz2', compression='bz2'))
