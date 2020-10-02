import pandas as pd
import os
from chose_feature import chose_feature
"""
    选择特征 selected_feature
    总的特征表格含有label clinical_feature.csv
    挑选特征后保存的名字：train_and_test.csv


"""


class GetCombineFeature:
    def __init__(self, root_path):
        self.root_path = root_path

    def get_feature_name(self, feature_group, store_model_name,
                         normalizer_name, dim_name, selecter_name,
                         model_name, feature_number):
        """

        :param feature_group: 特征的类别，如first order, GLCM等
        :param store_model_name: 存放结果的名字
        :param normalizer_name: 归一化的方法
        :param selecter_name: 特征选择方法的名字
        :param dim_name: 降维的名字
        :param model_name: 模型的名称
        :param feature_number: 选择几个特征
        :return: 返回建模的特征名字
        """
        feature_path = os.path.join(
            self.root_path, feature_group, store_model_name, normalizer_name, dim_name,
            selecter_name+"_"+str(feature_number), model_name, model_name+"_coef.csv"
        )
        pd_feature = pd.read_csv(feature_path)
        feature_name = list(pd_feature["Unnamed: 0"])
        return feature_name  # 建模特征的名字列表


if __name__ == '__main__':
    get = GetCombineFeature(root_path=r'E:\Data\doctor tao\max_and_min\log_wave_original')
    feature_group= "glcm"
    store_model_name = "svm_result"
    normalizer_name = "Mean"
    dim_name = "PCC"
    selecter_name = "KW"
    model_name = "SVM"
    feature_number = 6
    x = get.get_feature_name(feature_group, store_model_name,
                         normalizer_name, dim_name, selecter_name,
                         model_name, feature_number)
    print(x)







# def get_feature_names(all_data_path, feature_class_name, index):
#     feature_folder_path = os.path.join(all_data_path, feature_class_name)
#     feature_model_path = os.path.join(feature_folder_path, "result")
#     sub_path = os.path.join(feature_model_path, "Mean")
#     sub_path_2 = os.path.join(sub_path, "PCC")
#     sub_folder_path = os.path.join(sub_path_2, "KW_" + str(index))
#     sub_folder_path_2 = os.path.join(sub_folder_path, "SVM")
#     feature_csv_path = os.path.join(sub_folder_path_2, "SVM_coef.csv")
#     pd_feature = pd.read_csv(feature_csv_path)
#     feature_name = pd_feature["Unnamed: 0"]
#     return list(feature_name)
#
#
# all_data_path = r'Y:\DYB\data_and_result\doctor tao\roi_2'
#
#
# info = {
#         "firstorder": 2,
#         "glcm": 3,
#         "gldm": 2,
#         "glrlm": 1,
#         "glszm": 4,
#         "ngtdm": 1,
#       }
#
#
# select_feature_name = []
# for feature_class_name, index in zip(info.keys(), info.values()):
#     feature_name = get_feature_names(all_data_path, feature_class_name, index)
#     for name in feature_name:
#         select_feature_name.append(name)
#
# data = {"feature_name":select_feature_name}
#
# select_feature = pd.DataFrame(data=data)
#
# select_feature.to_csv(os.path.join(all_data_path, "selected_feature_info.csv"), index=None)
#
#
# data_path = os.path.join(all_data_path, "train_numeric_feature.csv")  # 总的特征表格，必须含有label
# store_name = "selected_train"  # 特征挑选后保存的名字
#
# chose_feature(feature_path=os.path.join(all_data_path, "selected_feature.csv"),
#               data_path=data_path, store_path=all_data_path, store_name=store_name)
#
#
# def combine_feature(root_path, old_feature_name, store_name):
#     pass
