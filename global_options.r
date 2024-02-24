# Data and model paths
data_path <- "data/"
model_path <- "data/models/"
# ==== parsing pdfs ====

# where to put raw pdf files
pdf_path <- "data/pdfs/raw/"

# where to put parsed pdf files (in csv format)
pdf_parsed_path <- "Data/pdfs/parsed/"

# number of CPU cores to use for parsing
n_cores <- 4


# create nessesary folders
dir.create(data_path, recursive = TRUE, showWarnings = FALSE)
dir.create(model_path, recursive = TRUE, showWarnings = FALSE)
dir.create(pdf_path, recursive = TRUE, showWarnings = FALSE)
dir.create(pdf_parsed_path, recursive = TRUE, showWarnings = FALSE)

# ==== training word2vec model ====

# max RAM allocated for parsing using CoreNLP
ram_corenlp <- "32G"

# number of lines in the input file to process uing CoreNLP at once.
# Increase on workstations with larger RAM (e.g. to 1000 if RAM is 64G)
parse_chunk_size <- 1000

# CoreNLP directory location
# location of the CoreNLP models
Sys.setenv(CORENLP_HOME = "/Users/mai/stanford-corenlp-full-2018-10-05")

# threshold of the phraser module (smaller -> more phrases)
phrase_threshold <- 10

# min number of times a bigram needs to appear in the corpus
#  to be considered as a phrase
phrase_min_count <- 20

# dimension of word2vec vectors
w2v_dim <- 300

# window size in word2vec
w2v_window <- 5

# number of iterations in word2vec
w2v_iter <- 40

# change to a fraction number (e.g. 0.2) to restrict
# to the dictionary vocab in the top 20% of most frequent vocab
dict_restrict_vocab <- NULL
