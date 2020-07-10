#!/usr/bin/python3

import numpy
import math
import matplotlib.pyplot as plt
import scipy.optimize

# Fit multiple normal phase sweeps (R05D08_2p2A)
# with a model with two resonances.
# Free parameters:
#   a1 = -a2 - two amplitude
#   ph1 = 0 ph2 =pi - two phases
#   f1, f2 - two frequencies
#   tau1(n) = tau2(n) two sweep-dependent relaxation times

## read data
FF = numpy.array([])
DD = numpy.array([])
XX = numpy.array([])
YY = numpy.array([])
ICTA = numpy.array([])
NN = numpy.array([], dtype=int)
N = 0
for n in range(12,44):
  fname="../data_freq2/R05D08_2p2A_%02d.dat" % (n)

  # read data
  F,D,X,Y,I = numpy.loadtxt(fname, usecols=(1,2,3,4,7), unpack=True, comments='#')

  # keep only lowest excitation
  ii = (D==11)

  # remove first point
  ii[numpy.argmax(ii)] = False
  FF = numpy.append(FF, F[ii])
  DD = numpy.append(DD, D[ii])
  XX = numpy.append(XX, X[ii])
  YY = numpy.append(YY, Y[ii])
  ICTA = numpy.append(ICTA, I[ii])
  NN = numpy.append(NN, numpy.ones(Y[ii].size)*N)
  N+=1;

#########################
def calc_osc(pars, FF,NN):

  A1  = pars[0]
  A2  = -A1 
#  ph1  = pars[2]
#  ph2  = pars[3]
  ph1 = 0
  ph2 = 0
  f1  = pars[1]
  f2  = pars[2]
  # ph  = 0
  R = numpy.zeros(FF.size, dtype=complex)

  for n in numpy.unique(NN):
    n=int(n)
    ii = (NN==n)
    F = FF[ii]
    tau1  = pars[3+n]
 #   tau2 = pars[7+n*2]
    
    # resonance
    R[ii] = A1/(f1**2 - F**2 + 1j*F/tau1)*numpy.exp(1j*(ph1)) +\
            A2/(f2**2 - F**2 + 1j*F/tau1)*numpy.exp(1j*(ph2))
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
pars = [-0.7, 5.3, 8.1]
bounds = [(-100,100),(2,10), (5,20)]
for n in range(N):
  pars.append(0.1)    #tau1
#  pars.append(0.1)    #tau2
  bounds.append((0.001,2))
# bounds.append((0.001,2))

npars0 = numpy.array(pars)

res = scipy.optimize.minimize(minfunc, npars0, (FF,NN,XX,YY),
   bounds=bounds,
   options={'disp': False, 'maxiter': 10000})
npars = numpy.array(res.x)

###
fres = open("fit_normal_2const_freq_single_tau.txt", "w")
fres.write("# amp1: %f\n" %(npars[0]))
fres.write("# amp2: %f\n" %(-npars[0]))
fres.write("# f1:  %f\n" %(npars[1]))
fres.write("# f2:  %f\n" %(npars[2]))
fres.write("# icta, tau1\n")

icta = numpy.zeros(N)
tau1 = numpy.zeros(N)


ff = numpy.linspace(numpy.min(FF), numpy.max(FF), 100)
cols = 'rgbcmyk'
plt.figure(1)
fig, ax = plt.subplots(1,2, figsize=(8, 10))
for n in range(N):
  n=int(n)
  c = cols[n%len(cols)]
  ii = (NN==n)

  F1 = FF[ii]
  X1 = XX[ii]
  Y1 = YY[ii]

  icta[n] = numpy.mean(ICTA[ii])
  tau1[n] = npars[3+n]
 # tau2[n] = npars[7+2*n]
  fres.write("%f %f\n" % (icta[n], tau1[n]))

  sh = 4*n/1000
  ax[0].plot(F1, X1+sh, c+'.', label=n)
  ax[1].plot(F1, Y1+sh, c+'.')

  xx,yy = calc_osc(npars, ff, n)

  ax[0].plot(ff, xx+sh, c+'-')
  ax[1].plot(ff, yy+sh, c+'-')

fres.close()


ax[0].set_xlabel('freq, Hz')
ax[1].set_xlabel('freq, Hz')
ax[0].set_ylabel('x')
ax[1].set_ylabel('y')
plt.savefig("fit_normal_2const_freq_single_tau.png")

plt.figure(2)
plt.clf()
plt.plot(icta, tau1, 'ro-', label="tau1")
#plt.plot(icta, tau2, 'bo-', label="tau2")
plt.xlabel('icta width, Hz')
plt.ylabel('tau')
plt.legend()
plt.savefig("fit_normal_2const_freq_tau.png")

