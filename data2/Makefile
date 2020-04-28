# all files
FILES :=\
  RUN5_DM1_flopper_AC_5A.dat\
  RUN5_DM1_flopper_Fsweep_5A.dat\
  RUN5_DM2_flopper_AC_1Hz_5A.dat\
  RUN5_DM3_flopper_AC_1Hz_2p5A_amp_sweep.dat\
  RUN5_DM3_flopper_AC_1Hz_2p5A.dat\
  RUN5_DM3_flopper_AC_1Hz_4A.dat\
  RUN5_DM3_flopper_AC_1Hz_5p8A.dat\
  RUN5_DM4_flopper_4Hz_2p5A.dat\
  RUN5_DM4_flopper_amp_sweep4A.dat\
  RUN5_DM5_flopper_2Hz_2p0A.dat\
  RUN5_DM5_flopper_2Hz_5p8A.dat\
  RUN5_DM6_flopper_2Hz_2p8A.dat\
  RUN5_DM6_flopper_2Hz_5p8A.dat\
  RUN5_DM7_flopper_3Hz_3A_AmpSweep.dat\
  RUN5_DM7_flopper_3Hz_5p2A_AmpSweep.dat

all:

data: $(patsubst %, ./1ma_%, ${FILES})\
      $(patsubst %, ./5ma_%, ${FILES})

# define smoothing window sizes:
WIN:=21
%_RUN5_DM1_flopper_AC_5A.dat:                  WIN:=11
%_RUN5_DM1_flopper_Fsweep_5A.dat:              WIN:=1
%_RUN5_DM3_flopper_AC_1Hz_2p5A_amp_sweep.dat:  WIN:=1
%_RUN5_DM3_flopper_AC_1Hz_2p5A.dat:            WIN:=5
%_RUN5_DM4_flopper_4Hz_2p5A.dat:               WIN:=11
%_RUN5_DM7_flopper_3Hz_5p2A_AmpSweep.dat:      WIN:=101

SKIP:=""
5ma_RUN5_DM1_flopper_AC_5A.dat:        SKIP:=0-2
1ma_RUN5_DM1_flopper_AC_5A.dat:        SKIP:=0-10
5ma_RUN5_DM3_flopper_AC_1Hz_2p5A.dat:  SKIP:=0-4,135-139
1ma_RUN5_DM3_flopper_AC_1Hz_2p5A.dat:  SKIP:=0-20,675-695
5ma_RUN5_DM3_flopper_AC_1Hz_4A.dat:    SKIP:=0-7,360-
1ma_RUN5_DM3_flopper_AC_1Hz_4A.dat:    SKIP:=0-35,1800-
5ma_RUN5_DM3_flopper_AC_1Hz_5p8A.dat:  SKIP:=0-7,822-
1ma_RUN5_DM3_flopper_AC_1Hz_5p8A.dat:  SKIP:=0-35,4110-
5ma_RUN5_DM4_flopper_4Hz_2p5A.dat:     SKIP:=0-5
1ma_RUN5_DM4_flopper_4Hz_2p5A.dat:     SKIP:=0-25
5ma_RUN5_DM5_flopper_2Hz_2p0A.dat:     SKIP:=0-4
1ma_RUN5_DM5_flopper_2Hz_2p0A.dat:     SKIP:=0-20
5ma_RUN5_DM6_flopper_2Hz_2p8A.dat:     SKIP:=0-6,331-
1ma_RUN5_DM6_flopper_2Hz_2p8A.dat:     SKIP:=0-30,1655-
5ma_RUN5_DM7_flopper_3Hz_3A_AmpSweep.dat: SKIP:=0-5,870-900
1ma_RUN5_DM7_flopper_3Hz_3A_AmpSweep.dat: SKIP:=0-25,4350-4500

1ma_%.dat: ../data1/1m_%.dat
	./add_icta $< $@ --sm_win ${WIN} --icta_plot ${@:%.dat=%.png} --skip ${SKIP}

5ma_%.dat: ../data1/5m_%.dat
	./add_icta $< $@ --sm_win ${WIN} --icta_plot ${@:%.dat=%.png} --skip ${SKIP}

clean:
	rm -f 1ma_*.dat 1ma_*.png
	rm -f 5ma_*.dat 5ma_*.png

zip:
	zip flopper_data2.zip *.dat *.png Readme.md