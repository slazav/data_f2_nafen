datadir=/mnt/luna/fridge2_rawdata/Nafen_cell

all:

data:
	while read d t; do\
	    [ "$$d" != "#" ] || continue;\
	    [ "$$d" != "" ] || continue;\
	    name=$$(echo $$d | sed 's|/|_|g');\
	    echo "$$name";\
	    mkdir -p $$name;\
	    for f in ${datadir}/$$d/*; do\
	      awk '$$1>0 && $$1<90000 {print $$1,$$2,$$10}' $$f > $$name/$${f##*/};\
	    done;\
	done < list_w2w.tab

clean:
	rm -rf RUN*

zip:
	zip -r data_w2w.zip RUN*