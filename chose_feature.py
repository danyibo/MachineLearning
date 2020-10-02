import os
import pandas as pd


def chose_feature(feature_path, data_path, store_path, store_name):
    """

    :param feature_path: 传入需要的特征csv列表：feature_name后面就是特征名
    :param data_path: 传入大的特征表格
    :param store_path: 存放路径
    :param store_name: 存放名字
    :return:
    """
    pd_feature = pd.read_csv(feature_path)
    feature_list = pd_feature["feature_name"]
    pd_data = pd.read_csv(data_path)
    feature_name = pd_data.columns[2:]
    try:
        case_name = pd_data["CaseName"]
    except:
        case_name = pd_data["Unnamed: 0"]
    label = pd_data["label"]
    pd_new = pd_data[feature_list]
    pd_new = pd.concat([case_name, label, pd_new], axis=1)
    pd_new.to_csv(os.path.join(store_path, store_name + ".csv"), index=None)


if __name__ == '__main__':
    select_feature = r"E:\EGFR TKI\feature_subtraction\sub_feature\pe_sub_p\selected.csv"
    data_path = r"E:\EGFR TKI\feature_subtraction\sub_feature\pe_sub_p\clinical_pe_sub_p.csv"
    store_path = r"E:\EGFR TKI\feature_subtraction\sub_feature\pe_sub_p"
    store_name = "train_and_test"
    chose_feature(feature_path=select_feature, data_path=data_path, store_path=store_path, store_name=store_name)