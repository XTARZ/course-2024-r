library(tools)
# goto data location
setwd(
  "/home/xtarz/course/The-Role-of-Corporate-Culture-in-Bad-Times/data/"
)

# read all csv_files
csv_files <- list.files(
  path = paste(getwd(), "/pdfs/parsed", sep = ""), # 待优化
  pattern = "*.csv", recursive = TRUE, full.names = TRUE,
  include.dirs = TRUE
)

# prepare var to store data
all_QA <- list()
all_Presentation <- list()
all_transcripts <- list()

for (single_call_csv in csv_files) {
  # read silgle csv into df
  call_csv_dataframe <- read.csv(single_call_csv)

  # 插入一列名为call_title_date,内容是当前csv的文件名不含扩展
  call_csv_dataframe$"call_title_date" <-
    tools::file_path_sans_ext(single_call_csv)
  # 删除名为 Title的列
  # 实际操作是，将所有列提取出来，除了 Title 列以外，并装回原变量里
  call_csv_dataframe <-
    call_csv_dataframe[, !names(call_csv_dataframe) == "Title"]

  all_transcripts[[length(all_transcripts) + 1]] <- call_csv_dataframe
}
print(all_transcripts)





# traversal csv files
# for (single_call_csv in csv_files) {
#   # read silgle csv into df
#   call_csv_dataframe <- read.csv(single_call_csv)
#   # create call primary id as call_title_date
#   # 插入一列名为call_title_date,内容是当前csv的文件名不含扩展
#   call_csv_dataframe$"call_title_date" <-
#     tools::file_path_sans_ext(single_call_csv)
#   # 删除名为 Title的列
#   # 实际操作是，将所有列提取出来，除了 Title 列
#   call_csv_dataframe <-
#     call_csv_dataframe[, !names(call_csv_dataframe) == "Title"]
#   all_transcripts <-
#     c(all_transcripts, call_csv_dataframe)
# }
# all_transcripts <-
#   all_transcripts[
#     order(
#       all_transcripts$call_title_date,
#       all_transcripts$ROUND,
#       all_transcripts$Paragraph
#     ),
#   ]

# cleaned_meta <- read.csv(file = "./meta_data_cleaned.csv")

# cleaned_meta$call_title_date <- paste(
#   cleaned_meta$call_title,
#   " ",
#   format(as.Date(cleaned_meta$date_EST, "%m/%d/%y"), "%Y-%m-%d"),
#   sep = ""
# )
# print(cleaned_meta)

prep_inputs()
