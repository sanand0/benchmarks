import time
import datetime
import dateutil.parser
import pandas as pd

def timing(label, fn):
    t0 = time.time()
    fn()
    t1 = time.time()
    print '%s: %d ms' % (label, int((t1 - t0) * 1000))

s = pd.Series(['01-31-2012']*100000)

timing('to_datetime', lambda: pd.to_datetime(s))
timing('dateutil', lambda: s.apply(dateutil.parser.parse))
timing('strptime', lambda: s.apply(lambda v: datetime.datetime.strptime(v, '%m-%d-%Y')))
timing('manual', lambda: s.apply(lambda v: datetime.datetime(int(v[6:10]), int(v[0:2]), int(v[3:5]))))
