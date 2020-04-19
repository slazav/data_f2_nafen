## Data splitted by drive frequency and amplitude, with ICTA column added.

For each series I choose 1m or 5m
dataset, split measurements with different excitation
amplitudes/frequencies and added ICTA width column.

* R05D01a_5A -- slow warming up from low temperature to above Tc with f =
1Hz and single amplitude. Two kinks are visible near tc. Data with
1-minute resolution is used to resolve these transitions.
Transitions: Ta1 = 717, Tc = 814

* R05D01b_5A1, R05D01b_5A1 -- frequency sweeps at two different amplitudes
and slightly different temperatures. Data with 1-minute resolution is used,
starting part of each signal where drive is not stable is removed.

* R05D02a_5A -- Same as R05D01a_5A, slow warming up from low temperatures.
For some reason response is 1.2 times smaller (different lockin phase?)
Two transitions: Ta1 = 703, Tc = 819 Hz
Note that at T>Tc and T<Tc curves are close to each other. This maybe show
that viscosity effects for ICTA and for flopper are same, no strong effects from
aerogel!

* R05D03a_5A -- Amplitude sweep at ICTA = 250-280 Hz. 5-minutes data is used.

* R05D03b_5A, R05D03c_4A, R05D03d_8A -- Short temperature sweeps at low temperatures.

* R05D04a_5A1, R05D04a_5A2 -- warming up from low temperature to
above Tc with f = 4Hz and two different amplitudes.
1-minute data are used for better temperature resolution.
Transitions: Tc = 847 Hz

* R05D04b_4A1,2,3,4 -- warming up with 4 different frequencies and 20 many drive
amplitudes (20 different combinations). I split it into 4 files with different freq.
1-minute data are used for better temperature resolution.
Non-linearity at low temperatures is visible!
Transitions: Tc = 822 Hz

* R05D05a_0A -- amplitude sweep at ICTA = 201-210 Hz, 5-minutes data is used.
Is it actually 0A?

* R05D05b_8A1..5 -- Warming up from low temperatures. freq = 2Hz, 5 different amplitudes.
Warming up at high drive and cooling at low drive is clearly seen!
Transiotions: Tc = 817 Hz

* R05D06a_8A -- Warming up from low temperatures, freq - 2Hz, 6 different amplitudes
Transiotions: Tc = 832 Hz

* R05D06b_8A -- Same (what is difference between 2p8A and 5p8A in file names?)
Transiotions: Tc = 814 Hz

* R05D07a_3A
Transiotions: Tc = 843 Hz

* R05D07b_3A

