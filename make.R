# This is a short make file to generate the markdown report and to publish
# the result into the /docs directory

rmarkdown::render("non_equi_joins.Rmd")
file.rename("non_equi_joins.html", "docs/index.html")


# We also want to extract the Python code to a separate .py file
# I find no easy way to do this from the R Markdown file so do it
# from the generated HTML file

library(rvest)
webpage <- read_html("docs/index.html")
rank_data_html <- html_nodes(webpage,'.python')
rank_data <- html_text(rank_data_html)

div <- "\n\n\n\n############# Python Code block extracted from non_equi_joins.Rmd ##############\n\n"

all_py_code <- paste(rank_data, collapse = div)
all_py_code <- gsub("\r\n", "\n", all_py_code)
all_py_code <- paste0(substring(div, 9), all_py_code, "\n")

writeLines(all_py_code, "extracted_py_code.py", sep = "")
