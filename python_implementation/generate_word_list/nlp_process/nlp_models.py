import sys

# 将父目录添加到系统路径中
sys.path.append("..")

import datetime
from pathlib import Path

# 导入自定义的文件实用程序模块
import file_util

# 导入gensim库，用于文本处理和建模
import gensim

# 导入全局选项模块
import global_options

# 导入用于处理停用词的库
import stopwordsiso as stopwords

# 导入tqdm库，用于显示循环进度条
import tqdm

# 从gensim库中导入models模块
from gensim import models


def train_bigram_model(input_path, model_path):
    """ Train a phrase model and save it to the disk. 
    
    Arguments:
        input_path {str or Path} -- input corpus
        model_path {str or Path} -- where to save the trained phrase model?
    
    Returns:
        gensim.models.phrases.Phrases -- the trained phrase model
    """
    # 创建保存模型的父目录
    Path(model_path).parent.mkdir(parents=True, exist_ok=True)
    
    # 打印当前时间
    print(datetime.datetime.now())
    print("Training phraser...")
    
    # 从文件中读取语料库
    corpus = gensim.models.word2vec.PathLineSentences(
        str(input_path), max_sentence_length=10000000
    )
    
    # 计算语料库中的行数
    n_lines = file_util.line_counter(input_path)
    
    # 训练短语模型
    bigram_model = models.phrases.Phrases(
        tqdm.tqdm(corpus, total=n_lines),
        min_count=global_options.PHRASE_MIN_COUNT,
        scoring="default",
        threshold=global_options.PHRASE_THRESHOLD,
        common_terms=stopwords.stopwords("en"),
    )
    
    # 保存训练好的短语模型
    bigram_model.save(str(model_path))
    
    return bigram_model


def bigram_transform(line, bigram_phraser):
    """ Helper file fore file_bigramer
    Note: Needs a phraser object in the enviroment.

    Arguments:
        line {str}: a line 
        return: a line with phrases joined using "_"
    """
    # 将单词列表中的短语连接起来
    return " ".join(bigram_phraser[line.split()])


def file_bigramer(input_path, output_path, model_path, threshold=None, scoring=None):
    """ Transform an input text file into a file with 2-word phrases. 
    Apply again to learn 3-word phrases. 

    Arguments:
        input_path {str}: Each line is a sentence
        ouput_file {str}: Each line is a sentence with 2-word phraes concatenated
    """
    # 创建保存输出文件的父目录
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    Path(model_path).parent.mkdir(parents=True, exist_ok=True)
    
    # 加载已训练的短语模型
    # https://radimrehurek.com/gensim/models/phrases.html#module-gensim.models.phrases
    bigram_model = gensim.models.phrases.Phrases.load(str(model_path))
    
    # 根据需要调整短语模型的阈值和评分
    if scoring is not None:
        bigram_model.scoring = getattr(gensim.models.phrases, scoring)
    if threshold is not None:
        bigram_model.threshold = threshold
    
    # 读取输入文件中的数据
    with open(input_path, "r") as f:
        input_data = f.readlines()
    
    # 对每行数据进行短语转换
    data_bigram = [bigram_transform(l, bigram_model) for l in tqdm.tqdm(input_data)]
    
    # 将处理后的数据写入输出文件
    with open(output_path, "w") as f:
        f.write("\n".join(data_bigram) + "\n")
    
    # 检查输入数据行数与输出文件行数是否相等
    assert len(input_data) == file_util.line_counter(output_path)


def train_w2v_model(input_path, model_path, *args, **kwargs):
    """ Train a word2vec model using the LineSentence file in input_path, 
    save the model to model_path.count
    
    Arguments:
        input_path {str} -- Corpus for training, each line is a sentence
        model_path {str} -- Where to save the model? 
    """
    Path(model_path).parent.mkdir(parents=True, exist_ok=True)
    # 保存训练好的Word2Vec模型
    
    # 从文件中读取语料库
    corpus_confcall = gensim.models.word2vec.PathLineSentences(
        str(input_path), max_sentence_length=10000000
    )
    
	# https://radimrehurek.com/gensim/models/word2vec.html
    # 训练Word2Vec模型
    model = gensim.models.Word2Vec(corpus_confcall, min_count=1, *args, **kwargs)
        # 创建保存模型的父目录

    model.save(str(model_path))
