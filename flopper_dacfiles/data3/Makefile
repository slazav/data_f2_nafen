all:

clean:
	rm -f *.dat *.png *.zip


skip1 = 1575631997 1575632202 1575632242 1575632816 1575632857 1575632980 1575633226\
        1575633882 1575634250 1575634496 1575634742 1575635356 1575635397
skip2 = 1575635858 1575635899 1575636241 1575636664

data:
	sh process_all
	sh process_fre
	for i in ${skip1}; do sed -i "/^$$i/d" R05D01b_5p0A_04Hz_24mV.dat; done
	for i in ${skip2}; do sed -i "/^$$i/d" R05D01b_5p0A_08Hz_48mV.dat; done
	for i in *_plot plot_*; do ./$$i; done

zip:
	zip flopper_data3.zip *.dat *.png *_plot plot_* Readme.md
