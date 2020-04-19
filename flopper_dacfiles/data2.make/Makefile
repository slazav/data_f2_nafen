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


all: ${FILES:%=../data2_1m/%}\
     ${FILES:%=../data2_5m/%}


# define smoothing window sizes:
WIN:=21
%/RUN5_DM1_flopper_AC_5A.dat:                  WIN:=11
%/RUN5_DM1_flopper_Fsweep_5A.dat:              WIN:=1
%/RUN5_DM3_flopper_AC_1Hz_2p5A_amp_sweep.dat:  WIN:=1
%/RUN5_DM3_flopper_AC_1Hz_2p5A.dat:            WIN:=5
%/RUN5_DM4_flopper_4Hz_2p5A.dat:               WIN:=11
%/RUN5_DM7_flopper_3Hz_5p2A_AmpSweep.dat:      WIN:=101

SKIP:=""
../data2_5m/RUN5_DM1_flopper_AC_5A.dat:        SKIP:=0-2
../data2_1m/RUN5_DM1_flopper_AC_5A.dat:        SKIP:=0-10
../data2_5m/RUN5_DM3_flopper_AC_1Hz_2p5A.dat:  SKIP:=0-4,135-139
../data2_1m/RUN5_DM3_flopper_AC_1Hz_2p5A.dat:  SKIP:=0-20,675-695
../data2_5m/RUN5_DM3_flopper_AC_1Hz_4A.dat:    SKIP:=0-7,360-
../data2_1m/RUN5_DM3_flopper_AC_1Hz_4A.dat:    SKIP:=0-35,1800-
../data2_5m/RUN5_DM3_flopper_AC_1Hz_5p8A.dat:  SKIP:=0-7,822-
../data2_1m/RUN5_DM3_flopper_AC_1Hz_5p8A.dat:  SKIP:=0-35,4110-
../data2_5m/RUN5_DM4_flopper_4Hz_2p5A.dat:     SKIP:=0-5
../data2_1m/RUN5_DM4_flopper_4Hz_2p5A.dat:     SKIP:=0-25
../data2_5m/RUN5_DM5_flopper_2Hz_2p0A.dat:     SKIP:=0-4
../data2_1m/RUN5_DM5_flopper_2Hz_2p0A.dat:     SKIP:=0-20
../data2_5m/RUN5_DM6_flopper_2Hz_2p8A.dat:     SKIP:=0-6,331-
../data2_1m/RUN5_DM6_flopper_2Hz_2p8A.dat:     SKIP:=0-30,1655-
../data2_5m/RUN5_DM7_flopper_3Hz_3A_AmpSweep.dat: SKIP:=0-5,870-900
../data2_1m/RUN5_DM7_flopper_3Hz_3A_AmpSweep.dat: SKIP:=0-25,4350-4500

../data2_1m/%.dat: ../data1_1m/%.dat
	mkdir -p ../data2_1m
	./add_icta $< $@ --sm_win ${WIN} --icta_plot ${@:%.dat=%.png} --skip ${SKIP}

../data2_5m/%.dat: ../data1_5m/%.dat
	mkdir -p ../data2_5m
	./add_icta $< $@ --sm_win ${WIN} --icta_plot ${@:%.dat=%.png} --skip ${SKIP}

clean:
	rm -f ../data2_1m/*.dat ../data2_1m/*.png
	rm -f ../data2_5m/*.dat ../data2_5m/*.png
