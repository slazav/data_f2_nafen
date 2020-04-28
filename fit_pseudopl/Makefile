all:

FILES:=\
  R05D10_3p5A_10.dat\
  R05D10_3p5A_13.dat\
  R05D10_3p5A_14.dat\
\
  R05D08_2p2A_13.dat\
  R05D08_2p2A_23.dat\
  R05D08_2p2A_33.dat\
  R05D08_2p2A_43.dat\
\
  R05D08_dummy_00.dat\
\
  R05D09_4p5A_30.dat\
  R05D09_4p5A_31.dat\
  R05D09_4p5A_32.dat\
  R05D09_4p5A_34.dat\

data:
	for i in ${FILES}; do cp -f ../data_freq2/$$i .; done


png:
	for i in $$(seq -w 13 43); do ./fit_normal1 ../data_freq2/R05D08_2p2A_$$i.dat ./R05D08_2p2A_$$i.png; done
