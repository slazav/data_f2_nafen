#!/usr/bin/python3

import numpy
import matplotlib.pyplot as plt

# A model of non-symmetric flopper
# See: http://slazav.xyz/notes/2020_flopper.htm

k1=15
k2=10
m=1
I=1
Dx=0.5
Dp=0.5
r1=0.5
r2=0.5
r0=0.1
F=1

w = numpy.linspace(0,10,100)
A = k1 + k2 - m*w**2 + 1j*w*Dx
B = k1*r1 - k2*r2
C = k1*r1**2 + k2*r2**2 - I*w**2 + 1j*w*Dp


xc  = F*(C - B*r0)/(A*C + B**2)
phi = F*(B - A*r0)/(A*C + B**2)

plt.plot(w, numpy.real(xc), 'r-')
plt.plot(w, numpy.imag(xc), 'b-')

plt.savefig("flopper_model.png")
