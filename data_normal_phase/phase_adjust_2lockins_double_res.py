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

def rotate_real(ch1_real, ch2_real, phase):
  return ch1_real*numpy.cos(phase) + ch2_real*numpy.sin(phase)

def rotate_real(ch1_imag, ch2_imag, phase):
  return -ch1_imag*numpy.sin(phase) + ch2_imag*numpy.cos(phase)

###phase to minimise ch2 = 2.17

#load data

ch1freq, ch1_r, ch1_i = numpy.loadtxt(datadir+'/FSWP_FLOPPER_RUN9_Cooldown_4000mV_1kOhm_301020_0p4Afull2nd.dat',
              unpack=True, skiprows=1)




