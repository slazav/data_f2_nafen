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
  datadir = 'X:/fridge2_rawdata/Nafen_cell/RUN9/Cooldown/FLOPPER'

#load data

ch1_f, ch1_r, ch1_i = numpy.loadtxt(datadir+'/FSWP_FLOPPER_RUN9_Cooldown_4000mV_1kOhm_301020_0p4Afull2nd.dat',
              unpack=True, skiprows=1)

ch2_f, ch2_r, ch2_i = numpy.loadtxt(datadir+'/FSWP_FLOPPER_RUN9_Cooldown_4000mV_1kOhm_301020_0p4Afull3rd.dat',
              unpack=True, skiprows=1)

#process data
###phase to minimise ch2 = 2.172##


def rotate_real(ch1_real, ch2_real, phase):
  return ch1_real*numpy.cos(phase) + ch2_real*numpy.sin(phase)

def rotate_imag(ch1_imag, ch2_imag, phase):
  return -ch1_imag*numpy.sin(phase) + ch2_imag*numpy.cos(phase)

new_ch1_real = rotate_real(ch1_r, ch2_r, 2.172)
new_ch2_real = rotate_imag(ch1_r, ch2_r, 2.172)
new_ch1_imag = rotate_real(ch1_i, ch2_i, 2.172)
new_ch2_imag = rotate_imag(ch1_i, ch2_i, 2.172)

#test plot
fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(ch1_f, new_ch1_real, label = 'Ch1 Real')
ax1.plot(ch2_f, new_ch2_real, label = 'Ch2 Real')
ax1.plot(ch1_f, new_ch1_imag, label = 'Ch1 Imag')
ax1.plot(ch2_f, new_ch2_imag, label = 'Ch2 Imag')
ax1.set_title('2.172 rad rotation')
ax1.legend()

ax2.plot(ch1_f, ch1_r, label = 'Ch1 Real')
ax2.plot(ch2_f, ch2_r, label = 'Ch2 Real')
ax2.plot(ch1_f, ch1_i, label = 'Ch1 Imag')
ax2.plot(ch2_f, ch2_i, label = 'Ch2 Imag')
ax2.set_title('Original')
ax2.legend()
plt.show()
