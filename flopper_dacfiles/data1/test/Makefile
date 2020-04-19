PROG := ../process_flopper_dacfile

all: signal.dat ${PROG}
	${PROG} --points 50 --tfiles . 2020-01-01

signal.dat: ./make_sig_model
	./make_sig_model > $@

clean:
	rm -f *.txt *.dat
