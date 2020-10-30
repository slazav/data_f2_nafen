#!/usr/bin/python3

import numpy
import math
import matplotlib.pyplot as plt
import scipy.optimize
import socket


# Fit multiple normal phase sweeps (R05D08_2p2A)
# with a model with two resonances.
# Free parameters:
#   a1, a2 - two amplitude
#   ph2 - phase of the second resonance
#   f1(n), f2(n) - two sweep-dependent frequencies
#   tau1(n), tau2(n) - two sweep-dependent relaxation times

datadir = '../data_freq2'
if socket.gethostname() == 'pya015000009':    #viktor uses a table to automatically find which directory on local computer to use
  datadir = 'X:/fridge2_rawdata/Nafen_cell/slava_data/flopper_data_freq2'

## read data
FF = numpy.array([])
DD = numpy.array([])
XX = numpy.array([])
YY = numpy.array([])
NN = numpy.array([], dtype=int)
N = 0
for n in range(12,44):
  fname=datadir+"/R05D08_2p2A_%02d.dat" % (n)

  # read data
  F,D,X,Y = numpy.loadtxt(fname, usecols=(1,2,3,4), unpack=True, comments='#')
  X = X
  Y = Y

  # keep only lowest excitation
  ii = (D==11)

  # remove first point
  ii[numpy.argmax(ii)] = False
  FF = numpy.append(FF, F[ii])
  DD = numpy.append(DD, D[ii])
  XX = numpy.append(XX, X[ii])
  YY = numpy.append(YY, Y[ii])
  NN = numpy.append(NN, numpy.ones(Y[ii].size)*N)
  N+=1;

#########################
def calc_osc(pars, FF,NN):
    
  A1  = pars[0]
  A2  = pars[1] 
  ph  = pars[2]
  # ph  = 0
  R = numpy.zeros(FF.size, dtype=complex)

  for n in numpy.unique(NN):
    n=int(n)
    ii = (NN==n)
    F = FF[ii]
    f1  = pars[3+n*4]
    f2 = pars[4+n*4]
    tau1 = pars[5+n*4]
    tau2 = pars[6+n*4]

    # resonance
    R[ii] = A1/(f1**2 - F**2 + 1j*F/tau1)+A2/(f2**2 - F**2 + 1j*F/tau2)*numpy.exp(1j*(ph))
#    R[ii] += -B/(C + 1j*F/tau) # strange additional term

  # see fit_dummy script
  phase_shift = 0.226612/FF**1.205703

  # rotate phase
  R *= numpy.exp(1j*(phase_shift))

  return numpy.real(R), numpy.imag(R)

#########################
# function for minimization
def minfunc(pars, FF,NN,X,Y):
  xx,yy = calc_osc(pars, FF, NN)
  sum = numpy.linalg.norm(X-xx) + numpy.linalg.norm(Y-yy)
  return sum

#########################

#########################
#fit data

# build pars
pars = [-0.21, 0.21, 3]
bounds = [(-100,100),(-100,100),(0,2*numpy.pi)]
for n in range(N):
  pars.append(6)    #f1
  pars.append(10)  #f2
  pars.append(0.1)    #tau1
  pars.append(0.1)    #tau2
  bounds.append((1,10))
  bounds.append((1,20))
  bounds.append((0.001,2))
  bounds.append((0.001,2))
  
npars0 = numpy.array(pars)

res = scipy.optimize.minimize(minfunc, npars0, (FF,NN,XX,YY),
   bounds=bounds,
   options={'disp': False, 'maxiter': 10000})
npars = numpy.array(res.x)

ff = numpy.linspace(numpy.min(FF), numpy.max(FF), 100)
cols = 'rgbcmyk'
fig, ax = plt.subplots(1,2, figsize=(8, 10))
for n in range(N):
  n=int(n)
  c = cols[n%len(cols)]
  ii = (NN==n)

  F1 = FF[ii]
  X1 = XX[ii]
  Y1 = YY[ii]
  sh = 4*n/1000
  ax[0].plot(F1, X1+sh, c+'.', label=n)
  ax[1].plot(F1, Y1+sh, c+'.')
#  plt.plot(X1*F1, Y1*F1, c+'*', label=dd[i])

  xx,yy = calc_osc(npars, ff, n)

  ax[0].plot(ff, xx+sh, c+'-')
  ax[1].plot(ff, yy+sh, c+'-')
#  plt.plot(xx*ff, yy*ff, c+'.-')


print(npars[0],npars[1],npars[2])

for n in range(N):
  n=int(n)
  print('%02d: f1 = %f f2 = %f tau1 = %f tau2 = %f'% (n, npars[3+4*n], npars[4+4*n], npars[5+4*n], npars[6+4*n]))

#  npars[6+3*n] = 0

for n in range(N):
  sh = 4*n/1000
#  xx,yy = calc_osc(npars, ff, n)
#  ax[0].plot(ff, xx+sh, 'k-')
#  ax[1].plot(ff, yy+sh, 'k-')
#  ff0=numpy.arange(0.5,10,0.1)
#  xx0,yy0 = calc_osc(npars0, ff0, n) 
#  ax[0].plot(ff0, xx0+sh, 'b-')
#  ax[1].plot(ff0, yy0+sh, 'b-')

ax[0].set_xlabel('freq, Hz')
ax[1].set_xlabel('freq, Hz')
ax[0].set_ylabel('x')
ax[1].set_ylabel('y')
#plt.legend()
plt.savefig("fit_2Lor.png")
