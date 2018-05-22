# This is a short make file to generate the markdown report and to publish
# the result into the /docs directory

rmarkdown::render("non_equi_joins.Rmd")
file.rename("non_equi_joins.html", "docs/index.html")
