all:

data:
	./process_sweeps R05D08_2p2A --dt 30
	./process_sweeps R05D08_5p0A --dt 30 --skip 23-32,208-
	./process_sweeps R05D09_4p5A --dt 30
	./process_sweeps R05D10_3p5A --dt 30
	./process_sweeps R05D10_4p3A --dt 30
	./process_sweeps R05D10_6p0A --dt 30

clean:
	rm -f *.png *.dat

zip:
	zip ../flopper_data_freq2.zip *.dat *.png Readme.md
