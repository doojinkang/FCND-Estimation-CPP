import sys
import numpy as np

if len(sys.argv) < 2:
  print("Usage : calc_std.py filename")
  exit()

filename = sys.argv[1]
data = np.loadtxt(filename, delimiter=',', dtype='Float64', skiprows=1)

pos_x = data[:,1]
print('data length = ', len(pos_x), ', std = ', np.std(pos_x))

