#!/usr/bin/python3

import numpy
import math
import requests
import io
from non_uniform_savgol import non_uniform_savgol
import matplotlib.pyplot as plt

################################
# Get smoothed ICTA data for a given time range

# times - numpy array with times
# win  - Smoothing window, points. Default: -1 (no smoothing)
# marg - Time margins, s. Default 600
def get_icta(tmin, tmax, win=0, marg=600):

  r = requests.get(url = "http://slazav.xyz:8091/get_prev?name=icta&t1=%f" %(tmin-marg))
  if r.text=="": t1=tmin-marg
  else: t1 = math.floor(float(r.text.split()[0]))

  r = requests.get(url = "http://slazav.xyz:8091/get_next?name=icta&t1=%f" %(tmax+marg))
  if r.text=="": t2=tmax+marg
  else: t2 = math.ceil(float(r.text.split()[0]))

  r = requests.get(url = "http://slazav.xyz:8091/get_range?name=icta&t1=%f&t2=%f" %(t1,t2))
  icta_data = io.StringIO(r.text)
  (icta_t,y,icta_w) = numpy.loadtxt(icta_data, comments='#', unpack=True, usecols=(0,2,3))

  # fix broken database!
  if icta_w[0]>4000: icta_w=y

  # smooth
  if win > 1:
    icta_sm = non_uniform_savgol(icta_t, icta_w, win, 3) # window size 21, polynomial order 3
    # calculate variance, remove peaks outside it
    dw = icta_sm-icta_w
    ii = numpy.abs(dw) < numpy.var(dw)
    # smooth again
    icta_st = icta_t[ii]
    icta_sw = non_uniform_savgol(icta_st, icta_w[ii], win, 3) # window size 21, polynomial order 3
  else:
    icta_st = icta_t
    icta_sw = icta_w


  return (icta_t, icta_w, icta_st, icta_sw)


################################
# Interpolate ICTA data
# Optionaly make a control plot

# times - numpy array with times
# win  - Smoothing window, points. Default: -1 (no smoothing)
# marg - Time margins, s. Default 600
# return: numpy array of same size at `times`
def interp_icta(times, win=0, marg=600, plot=''):

  # load ICTA data for the whole time range
  tmin = numpy.min(times)
  tmax = numpy.max(times)

  (icta_t, icta_w, icta_st, icta_sw) = get_icta(tmin, tmax, win, marg)

  # interpolate to data values
  icta = numpy.interp(times, icta_st, icta_sw)

  # control plot
  if plot != '':
    plt.clf();
    plt.plot((icta_t-tmin)/3600,  icta_w, 'r-', label = 'original data')
    plt.plot((icta_st-tmin)/3600, icta_sw, 'b-', label = 'smoothed')
    plt.plot((times-tmin)/3600,   icta, 'g*', label = 'interpolated to data points')
    plt.xlabel('time, hours')
    plt.ylabel('ICTA width, Hz')
    plt.legend()
    plt.savefig(plot)


  return icta
