Processing large DAC files and extracting
tables with signal parameters.

Access to /mnt/luna/fridge2_rawdata/Nafen_cell
data folder should be available.

Only RUN5 files are processed at the moment.

Tables contain following columns:
* Time, unix seconds (corresponds to the center of each signal).
* Frequency used for processing. It is rounded to the nearest 0.1 Hz value, in this sense it is fixed.
* Drive offset and drive amplitude (first harmonic), extracted from recorded data, V.
* Phase, difference between drive and signal, rad
* amp1, amp2, amp3 - three first harmonics of the signal (constant offset is not written).

Data is avalible in two versions with 1- and 5-minutes resolution (files with 1m_ and 5m_ prefix).
