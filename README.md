This is a mandatory project for the PhD course in Python 2018.

# What is it about?

I include som pseudo data in the data-folder.
One data set identifies cases `df_cases.feather` as rows and has some empy columns that I want to fill with data from some other data sets.

All python code is found in the file `non_equi_joins.Rmd`. This is R markdown file but it includes Python code. 


# System requirements

**Python3** with packages `feather`, `numpy`, `pandas`

**R:** The R markdown file include Python code but the document itself is generating a HTML-repost by using R.
It is therefore necessary to install R in order to produce the report.
Do that from here: https://cloud.r-project.org/

**R packages:** The new package `reticulate` is used to incorporate Python code in R. 
Also the `rmarkdown` package is used to generate the report.


**RStudio v 1.2:** Personally I prefer to use RStudio for the generating process (although this might not be strictly necessary).
To use the capabilities of intermingligt Python code in R markdown, RStudio v 1.2 is required.
As of today (2018-05-16) this version has not yet been officially released.
It can be found though from a daily build: https://dailies.rstudio.com/
Note that this is (so far) not the version that can be installed easily from within Anaconda).
