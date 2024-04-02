# 加载所需的R包
library(tidyverse) # 加载tidyverse包，提供了数据处理和可视化的功能
library(stringr) # 加载stringr包，用于字符串操作
library(tidytext) # 加载tidytext包，用于文本数据处理
library(stm) # 加载stm包，用于主题建模

# 设置工作目录
setwd(here::here()) # 使用here包设置工作目录

# 读取所有转录数据
all_transcripts <- read_csv("data/text_corpra/all_transcripts_parsed.csv.gz") # 从CSV文件中读取所有转录数据

all_transcripts <- all_transcripts %>% mutate(id = row_number()) # 添加行号（段落ID）



# 读取筛选后的与COVID相关的词语列表
covid_related_words <- read_csv("data/word_list_filtered.csv") %>% pull(word) # 从CSV文件中读取COVID相关的词语列表 # nolint
original_list <- c("covid-19") # 初始种子词语

covid_related_words <- c(covid_related_words, original_list) %>% unique() # 合并词语列表并去重

# 检测是否有未解析的实体中出现的词语
covid_related_words_single <- covid_related_words[!str_detect(covid_related_words, "_")] # 过滤未解析的实体
covid_related_words_single <- c(original_list, covid_related_words_single) # 合并列表

# 使用扩展列表计算分数
all_transcripts_tidy <- all_transcripts %>%
  dplyr::select(id, text_parsed) %>%
  unnest_tokens(word, text_parsed, token = "regex", pattern = " ") # 使用tidytext将文本数据转换为单词列表
all_transcripts_tidy <- all_transcripts_tidy %>% dplyr::filter(word %in% covid_related_words) # 筛选包含COVID相关词语的单词

all_transcripts_tidy2 <- all_transcripts %>%
  dplyr::select(id, text) %>%
  unnest_tokens(word, text) # 在原始文本中查找解析文本中未检测到的单词
all_transcripts_tidy2 <- all_transcripts_tidy2 %>% dplyr::filter(word %in% covid_related_words_single) # 筛选出包含在covid_related_words_single中的单词

undetected <- all_transcripts_tidy2 %>% anti_join(all_transcripts_tidy, by = c("id")) # 仅计算缺失的单词

all_transcripts_tidy <- bind_rows(all_transcripts_tidy, undetected) # 将未检测到的单词添加到数据集中
all_transcripts_tidy <- all_transcripts_tidy %>%
  group_by(id) %>%
  count() # 统计每段落中的单词数量

all_transcripts <- all_transcripts %>% left_join(all_transcripts_tidy, by = "id") # 将计数结果与原始数据集连接
all_transcripts <- all_transcripts %>% rename(expanded_n = n) # 重命名列名

all_transcripts_covid_related <- all_transcripts %>% filter(expanded_n > 0) # 保留包含关键词的段落

all_transcripts_covid_related %>% write_csv(
  paste0(
    "data/text_corpra/all_transcripts_covid_related",
    ".csv.gz"
  ),
  na = ""
)
