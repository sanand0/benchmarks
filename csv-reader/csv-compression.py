import time
import csv
import gzip
import bz2

t0 = time.time()
data = list(csv.reader(open('data.csv')))
t1 = time.time()

data = list(csv.reader(gzip.open('data.csv.gz')))
t2 = time.time()

data = list(csv.reader(bz2.BZ2File('data.csv.bz2')))
t3 = time.time()

print 'uncompressed: %d ms, gzip: %d ms, bzip2: %d ms' % (
    int((t1 - t0) * 1000),
    int((t2 - t1) * 1000),
    int((t3 - t2) * 1000),
)
