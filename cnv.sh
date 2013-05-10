#!/bin/bash
mkdir pdf
for jpg in `ls *.jpg`
do
convert -density 200x200 ${jpg%.jpg}.jpg ./pdf/${jpg%.jpg}.pdf
#convert ${jpg%.jpg}.jpg ./pdf/${jpg%.jpg}.pdf
done
pdftk ./pdf/*.pdf cat output ./pdf/out.pdf
