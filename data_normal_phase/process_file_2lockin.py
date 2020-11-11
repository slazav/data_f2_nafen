#!/usr/bin/python3

import numpy
import math
import matplotlib.pyplot as plt
import scipy.optimize
import socket


datadir = '../data_freq2'
if socket.gethostname() == 'pya015000009':    #viktor uses a table to automatically find which directory on local computer to use
  datadir = 'X:/fridge2_rawdata/Nafen_cell/RUN9/DM01/'

#load icta
icta_date, icta_time = numpy.loadtxt(datadir+'Wires/FSWP_ICTA_RUN9_DM01_1k_101120.dat', dtype=str, usecols=(0, 1), unpack=True)
icta_width = numpy.loadtxt(datadir+'Wires/FSWP_ICTA_RUN9_DM01_1k_101120.dat', usecols=(4))

icta_datetime = []
for x in range(0,len(icta_date)):
    icta_datetime.append(numpy.datetime64(icta_date[x][6:]+'-'+icta_date[x][3:5]+'-'+icta_date[x][0:2]+'T'+icta_time[x]).astype(int))



from sweep_packer import sweep_packer



#ch1_f, ch1_r, ch1_i = numpy.loadtxt(datadir+'/FSWP_FLOPPER_RUN9_Cooldown_4000mV_1kOhm_301020_0p4Afull2nd.dat',
#              unpack=True, skiprows=1)

#ch2_f, ch2_r, ch2_i = numpy.loadtxt(datadir+'/FSWP_FLOPPER_RUN9_Cooldown_4000mV_1kOhm_301020_0p4Afull3rd.dat',
#              unpack=True, skiprows=1)

#process data
###phase to minimise ch2 = 2.172 (cooldown), = 1.70 (DM01)##
showplot = False

def rotate_real(ch1_real, ch2_real, phase):
  return ch1_real*numpy.cos(phase) + ch2_real*numpy.sin(phase)

def rotate_imag(ch1_imag, ch2_imag, phase):
  return -ch1_imag*numpy.sin(phase) + ch2_imag*numpy.cos(phase)

def find_nearest(time_array, time):
    time_array = numpy.asarray(time_array)
    idx = (numpy.abs(time_array - time)).argmin()
    return time_array[idx]
fig, (ax1, ax2) = plt.subplots(1, 2)

drives = [9.0, 18.0]
for drive in drives:
#load data
    ch1 = open(datadir+'FLOPPER/FSWP_FLOPPER_RUN9_DM01_4P0A_%iMVfull2nd.dat'%int(drive))
    ch1 = sweep_packer(ch1)
    ch2 = open(datadir+'FLOPPER/FSWP_FLOPPER_RUN9_DM01_4P0A_%iMVfull3rd.dat'%int(drive))
    ch2 = sweep_packer(ch2)

    for ind in range(2,len(ch1['Date'])-1):

        print(ind)
        ch1_f = ch1['Freq'][ind]
        ch1_r = ch1['Vx'][ind]
        ch1_i = ch1['Vy'][ind]
        ch2_r = ch2['Vx'][ind]
        ch2_i = ch2['Vy'][ind]

        new_ch1_real = rotate_real(ch1_r, ch2_r, 2.172)
        new_ch2_real = rotate_imag(ch1_r, ch2_r, 2.172)
        new_ch1_imag = rotate_real(ch1_i, ch2_i, 2.172)
        new_ch2_imag = rotate_imag(ch1_i, ch2_i, 2.172)

        if ind%10 == 0:
            showplot=True


        if showplot == True:
            #test plot

            ax1.plot(ch1_f, new_ch1_real, label = 'Ch1 Real')
            ax1.plot(ch1_f, new_ch2_real, label = 'Ch2 Real')
            ax1.plot(ch1_f, new_ch1_imag, label = 'Ch1 Imag')
            ax1.plot(ch1_f, new_ch2_imag, label = 'Ch2 Imag')
            ax1.set_title('2.172 rad rotation')
            ax1.legend()

            ax2.plot(ch1_f, ch1_r, label = 'Ch1 Real')
            ax2.plot(ch1_f, ch2_r, label = 'Ch2 Real')
            ax2.plot(ch1_f, ch1_i, label = 'Ch1 Imag')
            ax2.plot(ch1_f, ch2_i, label = 'Ch2 Imag')
            ax2.set_title('Original')
            ax2.legend()
            plt.draw()



        start_time = ch1['Date_Time_Num'][ind]
        icta_start = find_nearest(icta_datetime, start_time)
        #save process files
        comments = "# t1: %i t2: %i icta: %f\n" \
                   "# time -- freq -- exc -- x -- y -- x2 -- y2 -- icta" %(start_time,start_time+1000,icta_start)

        time = numpy.linspace(start_time, start_time+1000, 40)
        time = time.astype(int)
        freq = ch1_f
        exc = drive*numpy.ones(len(ch1_f))
        x = new_ch1_real
        y = new_ch1_imag
        x2 = new_ch2_real
        y2 = new_ch2_imag

        icta = []
        for val in time:
            icta.append(find_nearest(icta_datetime, val))
        icta = numpy.array(icta)

        data_to_save = numpy.column_stack((time, freq, exc, x, y, x2, y2, icta))
        if drive == drives[0]:
            f = open('X:/fridge2_rawdata/Nafen_cell/slava_data/flopper_data_freq3/R09D01_4A_highf_%02d.dat'%ind, 'w')
            for i in range(0, len(freq)):
                f.write('%i %f %f %f %f %f %f %f\n'%(time[i], freq[i], exc[i], x[i], y[i], x2[i], y2[i], icta[i]))
            f.close()

        else:
            f = open('X:/fridge2_rawdata/Nafen_cell/slava_data/flopper_data_freq3/R09D01_4A_highf_%02d.dat'%ind, 'a')
            for i in range(0, len(freq)):
                f.write('%i %f %f %f %f %f %f %f\n'%(time[i], freq[i], exc[i], x[i], y[i], x2[i], y2[i], icta[i]))
            f.close()

