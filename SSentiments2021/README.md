
## cleandata.py <inputfile.csv>

Removes unessicary fields and rows and outputs it as `<inputfile>_clean.csv`. For cleaning purposes, it is encouraged to put all the inputfiles into a dedicated folder.

## combinecleandata.py <PATH> <outfile> --append

Combines all files in <PATH> folder (non recursively) with `_clean.csv` as its suffix into one dataset. After which it deletes the datasets to be combined. Default output file is `cleanedData.csv`