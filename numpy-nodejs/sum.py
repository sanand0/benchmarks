import time
import numpy

data = numpy.arange(0, 50000000, 1.)

t0 = time.time()
data += 1
t1 = time.time()

print '%d ms' % int((t1 - t0) * 1000)
