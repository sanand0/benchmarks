import time
import datetime
import dateutil.parser
import pandas as pd

def timing(label, fn):
    t0 = time.time()
    fn()
    t1 = time.time()
    print '%s: %d ms' % (label, int((t1 - t0) * 1000))

def lookup(s):
    """
    This is an extremely fast approach to datetime parsing.
    For large data, the same dates are often repeated. Rather than
    re-parse these, we store all unique dates, parse them, and
    use a lookup to convert all dates.
    """
    dates = {date:pd.to_datetime(date) for date in s.unique()}
    return s.apply(lambda v: dates[v])

s = pd.Series(['01-31-2012']*100000)

timing('to_datetime', lambda: pd.to_datetime(s))
timing('dateutil', lambda: s.apply(dateutil.parser.parse))
timing('strptime', lambda: s.apply(lambda v: datetime.datetime.strptime(v, '%m-%d-%Y')))
timing('manual', lambda: s.apply(lambda v: datetime.datetime(int(v[6:10]), int(v[0:2]), int(v[3:5]))))
timing('lookup', lambda: lookup(s))
