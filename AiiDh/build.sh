#!/bin/bash

svnversion > globalRevisionNumber.tex  && \
date "+%d-%b-%Y" | tr "[:upper:]"  "[:lower:]" > builddate.tex && \
pdflatex AiiDh && \
pdflatex AiiDh && \
latex2html -split 0 AiiDh.tex


