#!/bin/bash

pdflatex latex_template.tex
bibtex latex_template.aux
pdflatex latex_template.tex
pdflatex latex_template.tex

rm latex_template.aux
rm latex_template.bbl
rm latex_template.blg
rm latex_template.lof
rm latex_template.log
rm latex_template.lot
rm latex_template.toc
