import numpy as np
import pandas as pd


class LoadDataByPd:
    def __init__(self):
        self._pd_data = None

    def set_pd(self, pd_data):
        self._pd_data = pd_data

    def _get_pd(self): return self._pd_data

    def get_case_name(self):
        return self._get_pd()["CaseName"]

    def get_feature_name(self):
        return self._get_pd().columns[2:]

    def get_label(self):
        return self._get_pd()["label"]

    def get_positive_number(self):
        return len([i for i in self.get_label() if i == 1])

    def get_negative_number(self):
        return len([i for i in self.get_label() if i == 0])

    def get_feature_value(self):
        feature_name = self.get_feature_name()
        pd_data = self._get_pd()
        feature_array = np.asarray(pd_data[feature_name].values, dtype=np.float64)
        return feature_array

    def show_information(self):
        print('The number of case is {}'.format(len(self.get_case_name())))
        print('The number of features is {}'.format(len(self.get_feature_name())))
        positive_number = self.get_positive_number()
        negative_number = self.get_negative_number()
        assert (positive_number + negative_number == len(self.get_case_name()))
        print('The number of positive samples is {}'.format(positive_number))
        print('The number of negative samples is {}'.format(negative_number))
        
        
class LoadData:
    def __init__(self):
        self._file_path = None

    def set_file_path(self, file_path):
        self._file_path = file_path

    def _get_pd_frame(self):
        return pd.read_csv(self._file_path)

    def get_case_name(self):
        """CaseName"""
        return self._get_pd_frame()["CaseName"]

    def get_feature_name(self):
        return self._get_pd_frame().columns[2:]

    def get_label(self):
        return self._get_pd_frame()["label"]

    def get_positive_number(self):
        return len([i for i in self.get_label() if i == 1])

    def get_negative_number(self):
        return len([i for i in self.get_label() if i == 0])

    def show_information(self):
        print('The number of case is {}'.format(len(self.get_case_name())))
        print('The number of features is {}'.format(len(self.get_feature_name())))
        positive_number = self.get_positive_number()
        negative_number = self.get_negative_number()
        assert (positive_number + negative_number == len(self.get_case_name()))
        print('The number of positive samples is {}'.format(positive_number))
        print('The number of negative samples is {}'.format(negative_number))


def update_frame_by_data(case_name, label, feature_name, feature_value):
    case_name = np.asarray(case_name)
    label = np.asarray(label)
    feature_name = feature_name
    feature_value = feature_value
    data = np.concatenate((case_name[..., np.newaxis], label[..., np.newaxis], feature_value), axis=1)
    header = ['CaseName', 'label'] + list(feature_name)
    pd_data_frame = pd.DataFrame(data=data, columns=header, index=None)
    return pd_data_frame


if __name__ == '__main__':
    pass