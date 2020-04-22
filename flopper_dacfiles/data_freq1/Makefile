prefix = /mnt/luna/fridge2_rawdata/Nafen_cell

all:

data:
	mkdir -p R05D08 R05D09 R05D10
	cp ${prefix}/RUN5/DM8/flopper/*full.dat R05D08
	cp ${prefix}/RUN5/DM9/flopper/*full.dat R05D09
	cp ${prefix}/RUN5/DM10/flopper/{*full.dat,full2nd.dat} R05D10
	cp ${prefix}/RUN5/DM8/flopper/dummy_sweeps/*full.dat R05D08


zip:
	zip -r flopper_data_freq1.zip R05D08 R05D09 R05D10 Readme

clean:
	rm -rf R05D08 R05D09 R05D10
