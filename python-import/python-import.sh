#!/usr/bin/sh

timer () {
    python -c"import time;t0=time.time();import $1;print '$1 %0.3f' % (time.time() - t0)"
}

for module in `cat modules`; do
    (for i in `seq 10`; do timer $module; done) | awk '{n=$1;s+=$2} END {printf "%.4f %s\n", s/10, $1}'
done
