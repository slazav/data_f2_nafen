all: text.pdf


%.pdf: %.tex
	pdflatex $<

clean:
	rm -f *.aux *.bak *.pdf *.log
