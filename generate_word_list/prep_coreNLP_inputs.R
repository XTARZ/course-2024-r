
library(tools)

prep_inputs <- function(x) {

  # goto data location
  setwd("/home/xtarz/course/The-Role-of-Corporate-Culture-in-Bad-Times/data")
  csv_files <- list.files(path = ".", pattern = "*.csv")

  all_QA <- list()
  all_Presentation <- list()
  for (single_call_csv in csv_files) {
    call_csv_dataframe <- read.csv(single_call_csv)
    call_csv_dataframe$"call_title_date" <- tools::file_path_sans_ext(single_call_csv)
    call_csv_dataframe <- 
  }
  

  return(csv_files)
}

prep_inputs()
