Scripts for processing large DAC files and extracting
tables with all data, and averaged signals (if needed)

Data will go to ../data1_1m and ../data1_5m folders

Access to /mnt/luna/fridge2_rawdata/Nafen_cell
data folder should be available for processing

Only RUN5 files are processed

Data format:
* Time, unix seconds (beginning of each signal).
* Frequency used for processing. It is rounded to the nearest 0.1 Hz value, in this sense it is fixed.
* Drive offset and drive amplitude (first harmonic), extracted from recorded data, mV.
* Phase, difference between drive and signal, rad
* amp1, amp2, amp3 - three first harmonics of the signal (constant offset is not written)
