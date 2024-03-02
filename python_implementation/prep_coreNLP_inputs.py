"""prep calls text to be parsed using CoreNLP
"""
from pathlib import Path

import file_util
import global_options
import pandas as pd
from tqdm.auto import tqdm




def prep_inputs():
    """prep inputs documents (paragraphs) and IDs for CORENLP processing"""
    # read all csv_files
    csv_files = file_util.get_csv_files()
    # create list of QA and presentation dfs
    all_QA = []
    all_Presentation  = [] 
    for call in tqdm(csv_files):
        call_df = pd.read_csv(call, index_col=0)
        # create call primary id as call_title_date
        # 插入一列名为call_title_date,内容是当前csv的文件名不含扩展
        call_df.insert(0, "call_title_date", call.stem)
        # 删除名为 Title的列
        call_df.drop("Title", axis=1, inplace=True)
        # 如果 第0个ROUND内容为QA
        if call_df.ROUND[0] == "QA":
            # 把这个DataFrame放进 all_QA 数组里
            all_QA.append(call_df)
        else:
            # 把这个DataFrame放进 all_Presentation 数组里
            all_Presentation.append(call_df)
    # 将所有的df连接起来，或称合并了里面所有的表
    all_Presentation = pd.concat(all_Presentation, axis=0, ignore_index=True)
    all_QA = pd.concat(all_QA, axis=0, ignore_index=True)
    # 将QA和Presentation合并
    all_transcripts = pd.concat([all_QA, all_Presentation], axis=0, ignore_index=True)
    # 以"call_title_date", "ROUND", "Paragraph"为顺序进行排列
    all_transcripts = all_transcripts.sort_values(
        ["call_title_date", "ROUND", "Paragraph"]
    )
    # 新增一个列，名为 Paragraph_ID 每列的内容是对应列的 call_title_date--ROUND--Paragraph
    # 举例："Bank7 Corp., Q1 2020 Earnings Call, Apr 30, 2020 2020-04-30--QA--7"
    all_transcripts["Paragraph_ID"] = (
        all_transcripts["call_title_date"].astype(str)
        + "--"
        + all_transcripts["ROUND"].astype(str)
        + "--"
        + all_transcripts["Paragraph"].astype(str)
    )
    print(all_transcripts)
	# 将metadata_clean装载为DF
    # only use US earnings calls (hand-collected and checked)
    cleaned_meta = pd.read_csv(Path(global_options.DATA_PATH, "meta_data_cleaned.csv"))
    # 新增一个列，名为 call_title_date每列的内容是对应列的 call_title 
    cleaned_meta["call_title_date"] = (
        cleaned_meta["call_title"]
        + " "
        # date_EST 形如 4/9/20，转换为2020-04-09
        + pd.to_datetime(cleaned_meta["date_EST"]).dt.strftime("%Y-%m-%d")
    )
    # 将 cleaned_meta 中，call_title_data 值重复的条目删掉
    cleaned_meta = cleaned_meta.drop_duplicates(
        subset=["call_title_date"]
    )  # make sure call_title_date is unique
    # 新增一个列，include_sample ，值为1
    cleaned_meta["include_sample"] = 1
    # 仅取call_title_date 和 include_sample 两列，组成一个序列
    cleaned_meta = cleaned_meta[["call_title_date", "include_sample"]]
    print(cleaned_meta)
    # 挑选all_transcripts中call_title_date 相等的列，将对应的include_sample值填入
    all_transcripts = all_transcripts.merge(cleaned_meta, on="call_title_date")
    print(all_transcripts)
    return all_transcripts


def output_input(all_transcripts):
    Path(global_options.DATA_PATH, "text_corpra", "input").mkdir(
        parents=True, exist_ok=True
    )
    file_util.list_to_file(
        all_transcripts["Paragraph_ID"].tolist(),
        Path(global_options.DATA_PATH, "text_corpra", "input", "document_ids.txt"),
    )
    file_util.list_to_file(
        all_transcripts["text"].tolist(),
        Path(global_options.DATA_PATH, "text_corpra", "input", "documents.txt"),
    )


if __name__ == "__main__":
    all_transcripts = prep_inputs()
    output_input(all_transcripts)
