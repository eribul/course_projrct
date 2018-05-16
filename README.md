# What is it?

This is a mandatory project for the PhD course in Python 2018.

# What is it about?

I include some pseudo data in the data-folder.
One data set identifies cases `df_cases.feather`. Rows corresponds to individual and most columns are just placeholders without any data.
The aim of the project is to allocate data from three other data sources and to fill up the empty columns for the cases. 
More de4tilas can be found in the `pseudocode.txt` file. 

All python code is found in the file `non_equi_joins.Rmd`. This is a R markdown file but it includes Python code. 


# Why use Rmarkdown?

The project is related to data science. An initial aim was therefore to use a Jupyter notebook to make data analysis and reporting intermingled.
During the project planning phase, it was known however that RStudio was working on extended support for Python in RStudio. It was therefore decided to investigate this new feature. 


# System requirements

* **Python3:** with packages [feather](https://github.com/wesm/feather) (to read data), [numpy](http://www.numpy.org/) (for numerical calculations) and [pandas](https://pandas.pydata.org/) (for data manipulation).
* **R:** The R markdown file include Python code but the document itself is generating a HTML-report by using R.
It is therefore necessary to install R in order to produce the report.
Install it from [CRAN](https://cloud.r-project.org/).
* **R packages:** [reticulate](https://rstudio.github.io/reticulate/) (to integrate R and Python) and [rmarkdown](https://rmarkdown.rstudio.com/) (to generate R markdown reports). 
* **RStudio v 1.2:** Personally I prefer to use RStudio for the generating process (although this might not be strictly necessary).
To use the capabilities of intermingling Python code in R markdown, RStudio v 1.2 is required.
As of today (2018-05-16) this version has not yet been officially released.
It can be found though from a daily build: https://dailies.rstudio.com/
Note that this is (so far) not the version that can be installed easily from within Anaconda).
