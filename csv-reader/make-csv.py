import sys
import csv

out = csv.writer(sys.stdout, lineterminator='\n')
out.writerow(['A', 'B', 'C', 'D', 'E', 'F'])
for row in range(0, 1000000):
    out.writerow([chr(64 + row % 64), row, row+1, row+2, row+3, row+4])
