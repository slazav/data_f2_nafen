all: signal.dat ../process_flopper_dacfile
	../process_flopper_dacfile --points 50 --tfiles . 2020-01-01

signal.dat: ./make_sig_model
	./make_sig_model > $@

clean:
	rm -f *.txt *.dat