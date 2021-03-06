#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as pp

pp.xlabel('Array size')
pp.ylabel('Time in mSec')
pp.title('CUDA vector addition timing metrics')

data_32 = np.loadtxt('q2_32.dat')
x_32 = data_32[:, 0]
y_32_incl = data_32[:, 1]
y_32_excl = data_32[:, 2]
pp.semilogx(x_32, y_32_incl, 'bo-', basex=2, linewidth=5)
pp.semilogx(x_32, y_32_excl, 'ro-', basex=2, linewidth=5)

data_1024 = np.loadtxt('q2_1024.dat')
x_1024 = data_1024[:, 0]
y_1024_incl = data_1024[:, 1]
y_1024_excl = data_1024[:, 2]
pp.semilogx(x_1024, y_1024_incl, 'bs-', basex=2, linewidth=1)
pp.semilogx(x_1024, y_1024_excl, 'rs-', basex=2, linewidth=1)

p1 = pp.Rectangle((0, 0), 1, 1, fc="blue")
p2 = pp.Rectangle((0, 0), 1, 1, fc="red")
pp.legend([p1, p2], ['Inclusive time', 'Exclusive time'], 'upper left')
pp.grid('on')
pp.show()
