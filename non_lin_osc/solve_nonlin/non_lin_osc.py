#!/usr/bin/python3

import numpy
import math
import scipy.optimize
import scipy.integrate

#######################################################

# Equilibriun function of a non-linear oscillator
# at periodic drive.
#
# u,v - van der Pol coordinates (x,x' rotated by w*t)
# w - frequency
# func - second derivative function, x'' = func(x, x')
#
# Coordinated are averaged over rotation period (phase 0..2*pi)
# Output is u' and v',  they should be zero in equilibrium.
#
# See text in http://www.scholarpedia.org/article/Duffing_oscillator
#

def nonlin_osc_eq(uv,w, F, func, fpars):

  p = 2*math.pi*numpy.linspace(0,1,100) # phase for integration
  sp = numpy.sin(p)
  cp = numpy.cos(p)
  x = uv[0]*cp-uv[1]*sp;
  dx = w*(-uv[0]*sp-uv[1]*cp);
  ddx = F*cp - func(x,dx,fpars);

  duv = [-scipy.integrate.trapz(p, (ddx + w**2*x)*sp)/w,\
         -scipy.integrate.trapz(p, (ddx + w**2*x)*cp)/w];
  return duv


#######################################################

# Find equilibrium (zero of nonlin_osc_eq function).
# Whis is enough for simple small non-linearities,
# for duffing oscillator it does not work properly
# (one should integrate trajectories in u-v space instead)

def nonlin_osc_solve0(w, F, func, fpars, uv0):
  return scipy.optimize.fsolve(nonlin_osc_eq, uv0, (w,F,func,fpars))

#######################################################

## pseudoplastic osc N1
def osc_pseudopl1(x,dx, pars):
  w0  = pars[0] # resonant frequency
  tau = pars[1] # relaxation time at low velocuty
  vc  = pars[2] # critical velocity
  k   = pars[3] # relaxation factor for large velocity
  return w0**2*x + dx/tau * (k - (1-k) * vc/numpy.sqrt(vc**2 + dx**2))
