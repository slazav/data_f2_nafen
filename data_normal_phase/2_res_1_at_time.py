#!/usr/bin/python3

import numpy
import math
import matplotlib.pyplot as plt
import scipy.optimize as opt
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
  datadir = 'X:/fridge2_rawdata/Nafen_cell/RUN9/Cooldown/'

#load icta
icta_date, icta_time = numpy.loadtxt(datadir+'Wires/FSWP_ICTA_RUN9_Cooldown_100_231020.dat', dtype=str, usecols=(0, 1), unpack=True)
icta_width = numpy.loadtxt(datadir+'Wires/FSWP_ICTA_RUN9_Cooldown_100_231020.dat', usecols=(4))

icta_datetime = []
for x in range(0,len(icta_date)):
    icta_datetime.append(numpy.datetime64(icta_date[x][6:]+'-'+icta_date[x][3:5]+'-'+icta_date[x][0:2]+'T'+icta_time[x]).astype(int))


#load data
from sweep_packer import sweep_packer


ch1 = open(datadir+'FLOPPER/FSWP_FLOPPER_RUN9_Cooldown_4000mV_1kOhm_301020_0p4A_testfull2nd.dat')
ch1 = sweep_packer(ch1)
ch2 = open(datadir+'FLOPPER/FSWP_FLOPPER_RUN9_Cooldown_4000mV_1kOhm_301020_0p4A_testfull3rd.dat')
ch2 = sweep_packer(ch2)

#process data
###phase to minimise ch2 = 2.172##
showplot = False

def rotate_real(ch1_real, ch2_real, phase):
  return ch1_real*numpy.cos(phase) + ch2_real*numpy.sin(phase)

def rotate_imag(ch1_imag, ch2_imag, phase):
  return -ch1_imag*numpy.sin(phase) + ch2_imag*numpy.cos(phase)

def find_nearest(time_array, time):
    time_array = numpy.asarray(time_array)
    idx = (numpy.abs(time_array - time)).argmin()
    return time_array[idx]
ch1['new_ch1_real'], ch2['new_ch2_real'], ch1['new_ch1_imag'], ch2['new_ch2_imag'] = {}, {}, {}, {}

for ind in range(0,len(ch1['Date'])):

  #  print(ind)
    ch1_f = ch1['Freq'][ind]
    ch1_r = ch1['Vx'][ind]
    ch1_i = ch1['Vy'][ind]
    ch2_r = ch2['Vx'][ind]
    ch2_i = ch2['Vy'][ind]

    ch1['new_ch1_real'][ind] = rotate_real(ch1_r, ch2_r, 2.172)
    ch2['new_ch2_real'][ind] = rotate_imag(ch1_r, ch2_r, 2.172)
    ch1['new_ch1_imag'][ind] = rotate_real(ch1_i, ch2_i, 2.172)
    ch2['new_ch2_imag'][ind] = rotate_imag(ch1_i, ch2_i, 2.172)

#fitting
def lor(frequency, pars):
    A = pars[0]
    ph = pars[1]
    f = pars[2]
    tau1 = pars[3]
    bkgd_1 = pars[4]
    bkgd_0 = pars[5]
    bkgd_2 = pars[6]
    bkgd_3 = pars[7]
    R = A/(f**2 - frequency**2 + 1j*frequency/tau1)*numpy.exp(1j*(ph)) + bkgd_1*frequency + bkgd_0 + 1j*(bkgd_2*frequency + bkgd_3)
    return numpy.real(R), numpy.imag(R)

def lor_poly(frequency, pars):
    A = pars[0]
    ph = pars[1]
    f = pars[2]
    tau1 = pars[3]
    bkgd_real = numpy.polyval(pars[4:7], frequency)
    bkgd_imag = 1j*numpy.polyval(pars[7:], frequency)
    R = A/(f**2 - frequency**2 + 1j*frequency/tau1)*numpy.exp(1j*(ph)) + bkgd_real*bkgd_imag
    return numpy.real(R), numpy.imag(R)

def lor2(frequency, pars):
    A1 = pars[0]
    ph1 = pars[1]
    f1 = pars[2]
    tau1 = pars[3]
    A2 = pars[4]
    ph2 = pars[5]
    f2 = pars[6]
    tau2 = pars[7]
    bkgd_1 = pars[8]
    bkgd_0 = pars[9]
    bkgd_2 = pars[10]
    bkgd_3 = pars[11]
    R = A1 / (f1 ** 2 - frequency ** 2 + 1j * frequency / tau1) * numpy.exp(
        1j * (ph1)) +  A2 / (f2 ** 2 - frequency ** 2 + 1j * frequency / tau2) * numpy.exp(
        1j * (ph2)) + bkgd_1 * frequency + bkgd_0 + 1j * (bkgd_2 * frequency + bkgd_3)
    return numpy.real(R), numpy.imag(R)

def minfunc(pars, freq, xdata, ydata):
    xfit, yfit = lor(freq, pars)
    sum = numpy.linalg.norm(xdata - xfit) + numpy.linalg.norm(ydata - yfit)
    return sum

def minfunc2(pars, freq, xdata, ydata):
    xfit, yfit = lor2(freq, pars)
    sum = numpy.linalg.norm(xdata - xfit) + numpy.linalg.norm(ydata - yfit)
    return sum

select =  [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 120, 140, 160, 180, 200]
#for ind in range(0, len(ch1['Date'])):
for ind in select:

    ch1_f = ch1['Freq'][ind]
    print(len(ch1_f))

    x = ch1['new_ch1_real'][ind]
    y = ch1['new_ch1_imag'][ind]

    pars0 = [0.8, numpy.pi/2.0, 7.6, 5.0, 0, 0, 0, 0]
    bounds = [(-100,100), (0, 2*numpy.pi), (1,10), (0.001, 100), (-10, 10), (-10, 10), (-10, 10), (-10, 10)]
    res = opt.minimize(minfunc, pars0, (ch1_f, x, y), bounds=bounds,
    options={'disp': False, 'maxiter': 10000})
    pars1 = numpy.array(res.x)
    osc_real, osc_imag = lor(ch1_f, pars1)

    print('f0 = %f, tau = %f, amp = %f, phase = %f'%(pars1[2], pars1[3], pars1[0], pars1[1]))
    print('bkgd: %f+%fi * freq + %f+%fi'%(pars1[4], pars1[6], pars1[5], pars1[7]))
    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.plot(ch1_f, x, '.')
    ax1.plot(ch1_f, osc_real)
    ax2.plot(ch1_f, y, '.')
    ax2.plot(ch1_f, osc_imag)
    plt.show()

    ch1_f2 = ch1_f[180:]
    x2 = x[180:]
    y2 = y[180:]

    pars0 = [0.05, numpy.pi, 12.5, 5.0, 0, 0, 0, 0, 0, 0]
    bounds = [(-100,100), (0, 2*numpy.pi), (10,20), (0.001, 100), (-10, 10), (-10, 10), (-10, 10), (-10, 10),
              (-10, 10), (-10, 10)]
    res = opt.minimize(minfunc, pars0, (ch1_f2, x2, y2), bounds=bounds,
    options={'disp': False, 'maxiter': 10000})
    pars2 = numpy.array(res.x)
    osc_real, osc_imag = lor_poly(ch1_f2, pars2)

    print('f0 = %f, tau = %f, amp = %f, phase = %f'%(pars2[2], pars2[3], pars2[0], pars2[1]))
    print('bkgd: %f+%fi * freq + %f+%fi'%(pars2[4], pars2[6], pars2[5], pars2[7]))
    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.plot(ch1_f2, x2, '.')
    ax1.plot(ch1_f2, osc_real)
    ax2.plot(ch1_f2, y2, '.')
    ax2.plot(ch1_f2, osc_imag)
    plt.show()

    pars0 = numpy.concatenate((pars1[:-4], pars2[:-4], pars1[4:]))
    bounds = [(-100,100), (0, 2*numpy.pi), (1,10), (0.001, 100), (-100,100), (0, 2*numpy.pi), (9,20), (0.001, 100),
              (-10, 10), (-10, 10), (-10, 10), (-10, 10)]

    osc_real, osc_imag = lor2(ch1_f, pars0)
    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.plot(ch1_f, x, '.')
    ax1.plot(ch1_f, osc_real)
    ax2.plot(ch1_f, y, '.')
    ax2.plot(ch1_f, osc_imag)
    plt.show()