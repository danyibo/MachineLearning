import os
import pandas as pd

"""
    说明：需要传入的是两个路径
        （1）：特征表格
        （2）：存放各类特征表格的路径
        
    注意：特征表格中需要有label
    
"""


def make_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


class GetSingleFeature:
    def __init__(self, data_path, store_path):
        self.data_path = data_path
        self.store_path = store_path
        self.pd_feature = pd.read_csv(self.data_path)
        self.feature_name = self.pd_feature.columns[2:]
        self.case_name = self.pd_feature["CaseName"]
        self.label = self.pd_feature["label"]

    def get_feature_class(self):
        feature_list = []
        for feature in self.feature_name:
            if len(feature) > 20:  # 跳过临床特征
                # print(feature)
                feature_list.append(feature.split("_")[-2])
        feature_list = set(feature_list)
        return feature_list

    def get_single_feature(self, feature_name, store_name):
        # store_name 是单个特征保存的名字
        feature_index = []
        for feature in self.feature_name:
            if len(feature) > 10: # 跳过临床特征
                if feature.split("_")[-2] == feature_name:
                    feature_index.append(feature)
        pd_single = self.pd_feature[feature_index]
        pd_single = pd.concat([self.case_name, self.label, pd_single], axis=1)
        store_folder = os.path.join(self.store_path, feature_name)
        make_folder(store_folder)

        pd_single.to_csv(os.path.join(store_folder, feature_name + "_"+store_name+".csv"), index=None)


def get_single_feature(all_feature_path, store_name):
    get_single = GetSingleFeature(data_path=all_feature_path, store_path=os.path.dirname(all_feature_path))
    feature_list = get_single.get_feature_class()
    for feature in feature_list:
        get_single.get_single_feature(feature_name=feature, store_name=store_name)
    return feature_list  # 返回文件夹的名字


if __name__ == '__main__':
    # get_single_feature(all_feature_path=r"Y:\DYB\data_and_result\doctor tao\roi_2\test_numeric_feature.csv")
    pass
