import os
import numpy as np
from FAE.DataContainer.data_container import LoadDataByPd
import pandas as pd
from FAE.statistics import get_p_value_by_feature
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import GradientBoostingClassifier
from FAE.DataContainer.data_container import update_frame_by_data


class ChoseFeature:
    """
    先保证特征在两个类别之间有差异
    再进行方差分析
    """
    def __init__(self, raw_file_path):
        self.raw_file_path = raw_file_path
        self.raw_pd_data = pd.read_csv(raw_file_path)
        self.pd_data = LoadDataByPd()
        self.pd_data.set_pd(self.raw_pd_data)
        self.case_name = self.pd_data.get_case_name()
        self.feature_name = self.pd_data.get_feature_name()
        self.label = self.pd_data.get_label()
        self.array = self.pd_data.get_feature_value()

    def _get_feature_by_label(self):
        """两个类别之间有差异"""
        pd_label_1 = self.raw_pd_data.loc[self.raw_pd_data["label"] == 1]
        pd_label_0 = self.raw_pd_data.loc[self.raw_pd_data["label"] == 0]
        selected_feature = []
        for feature in self.feature_name:
            if get_p_value_by_feature(pd_label_1, pd_label_0, feature) < 0.05:
                selected_feature.append(feature)
        return selected_feature

    def get_feature_by_std(self):
        """选择方差最大的特征"""
        feature_number = int(len(self.case_name)/10)
        std_list = [np.std(self.raw_pd_data[i]) for i in self._get_feature_by_label()]
        std_feature_dict = dict(zip(self._get_feature_by_label(), std_list))
        std_feature_list = []
        for k in sorted(std_feature_dict, key=std_feature_dict.__getitem__, reverse=True):
            std_feature_list.append(k)
        header = ["CaseName", "label"] + std_feature_list[:feature_number]
        return std_feature_list[:feature_number], self.raw_pd_data[header]

    def get_feature_by_GradientBoosting(self):
        new_array = SelectFromModel(GradientBoostingClassifier()).fit_transform(self.array, self.label)
        feature_name = ["feature_"+str(i) for i in range(new_array.shape[1])]
        pd_result = update_frame_by_data(case_name=self.case_name,
                                         feature_name=feature_name,
                                         feature_value=new_array,
                                         label=self.label)
        return pd_result


def run_select_feature_by_std(raw_file_path):
    store_path = os.path.join(os.path.dirname(raw_file_path), 'FeatureSelectedByStd')
    if not os.path.exists(store_path):
        os.makedirs(store_path)
    chose_feature = ChoseFeature(raw_file_path=raw_file_path)
    selected_feature, pd_result = chose_feature.get_feature_by_std()
    pd_result.to_csv(os.path.join(store_path, 'elected_train_and_test.csv'), index=None)


def run_select_feature_by_GradientBoosting(raw_file_path):
    store_path = os.path.join(os.path.dirname(raw_file_path), 'FeatureSelectedByGBT')
    if not os.path.exists(store_path):
        os.makedirs(store_path)
    chose_feature = ChoseFeature(raw_file_path=raw_file_path)
    pd_result = chose_feature.get_feature_by_GradientBoosting()
    pd_result.to_csv(os.path.join(store_path, 'elected_train_and_test.csv'), index=None)


if __name__ == '__main__':
    file_path = r"E:\my_fea\train_and_test.csv"
    run_select_feature_by_GradientBoosting(file_path)
