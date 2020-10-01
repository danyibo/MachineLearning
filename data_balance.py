import numpy as np
import os
from imblearn.over_sampling import SMOTE, RandomOverSampler

from FAE.DataContainer.data_container import LoadDataByPd, update_frame_by_data
import pandas as pd


def up_sampling(array, label):
    model = RandomOverSampler(random_state=0)
    new_data, new_label = model.fit_sample(array, label)
    return new_data, new_label


def smote(array, label):
    new_data, new_label = SMOTE().fit_sample(array, label)
    return new_data, new_label


class DoBalance:
    def __init__(self, raw_file_path):
        self.raw_file_path = raw_file_path
        self.raw_pd_data = pd.read_csv(self.raw_file_path)
        self.store_path = os.path.dirname(raw_file_path)

        self.pd_data = LoadDataByPd()
        self.pd_data.set_pd(self.raw_pd_data)
        self.array = self.pd_data.get_feature_value()
        self.label = self.pd_data.get_label()
        self.case_name = self.pd_data.get_case_name()
        self.feature_name = self.pd_data.get_feature_name()

    def do_sampling(self):
        new_data, new_label = up_sampling(array=self.array, label=self.label)
        new_case_name = np.asarray(["up_" + str(i) for i in range(new_data.shape[0])])
        pd_result = update_frame_by_data(feature_name=self.feature_name,
                                         label=new_label,
                                         case_name=new_case_name,
                                         feature_value=new_data)
        pd_result.to_csv(os.path.join(self.store_path, "train_up_sampling.csv"), index=None)

    def do_smote(self):
        new_data, new_label = smote(array=self.array, label=self.label)
        new_case_name = np.asarray(["smote_" + str(i) for i in range(new_data.shape[0])])
        pd_result = update_frame_by_data(feature_name=self.feature_name,
                                         label=new_label,
                                         case_name=new_case_name,
                                         feature_value=new_data)
        pd_result.to_csv(os.path.join(self.store_path, "train_up_smote.csv"), index=None)


def run_data_balance(raw_file_path):
    balance = DoBalance(raw_file_path)
    balance.do_sampling()
    balance.do_smote()


if __name__ == '__main__':
    raw_file_path = r"D:\my_fae_test\train.csv"
    run_data_balance(raw_file_path)
