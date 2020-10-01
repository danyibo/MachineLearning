import os
import pandas as pd
from sklearn.model_selection import train_test_split
from FAE.DataContainer.data_container import LoadData, LoadDataByPd


class SplitData:
    def __init__(self):
        self._file_path = None

    def set_file_path(self, file_path):
        self._file_path = file_path

    def do_split(self):
        store_path = os.path.dirname(self._file_path)
        pd_data = pd.read_csv(self._file_path)
        pd_train, pd_test = train_test_split(pd_data, train_size=0.7, test_size=0.3)
        train = LoadDataByPd()
        train.set_pd(pd_train)
        train_p = train.get_positive_number()
        test = LoadDataByPd()
        test.set_pd(pd_test)
        test_p = test.get_positive_number()

        if round((train_p / len(train.get_case_name())), 1) != round((test_p / len(test.get_case_name())), 1):
            self.do_split()
        else:
            pd_train.to_csv(os.path.join(store_path, "train.csv"), index=None)
            pd_test.to_csv(os.path.join(store_path, "test.csv"), index=None)
            train = LoadData()
            train.set_file_path(os.path.join(store_path, "train.csv"))
            test = LoadData()
            test.set_file_path(os.path.join(store_path, "test.csv"))
            print("-----TRAIN INFORMATION-----")
            train.show_information()
            print("-----TEST INFORMATION-----")
            test.show_information()


def run_split(raw_file_path):
    split_data = SplitData()
    split_data.set_file_path(file_path=raw_file_path)
    split_data.do_split()
    print("Split train and test finished!")


if __name__ == '__main__':
    file_path = r"E:\my_fea\GradientBoosting\elected_train_and_test.csv"
    run_split(file_path)
