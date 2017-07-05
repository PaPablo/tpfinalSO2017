SRC=tp_final

all: pdf bib pdf pdf

pdf: 
	pdflatex $(SRC)

bib:
	bibtex $(SRC)

2pdf: 
	pdflatex $(SRC) && pdflatex $(SRC)

clean: 
	rm *.aux *.log *.out *.dvi *.toc *.bbl *.blg *.bcf *.run*
