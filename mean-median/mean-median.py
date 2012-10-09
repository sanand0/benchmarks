import time
import numpy

data = numpy.random.rand(50000000)

t0 = time.time()
mean = numpy.mean(data)
t1 = time.time()
median = numpy.median(data)
t2 = time.time()

print 'mean: %d s, median: %d s' % (int((t1 - t0) * 1000), int((t2 - t1) * 1000))
