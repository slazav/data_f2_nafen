all:

data:
	sh process_all_1m
	sh process_all_5m

zip:
	zip flopper_data1.zip *.dat Readme.md

clean:
	rm -f *.dat *.zip