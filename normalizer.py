import os
import numpy as np
from FAE.DataContainer.data_container import LoadDataByPd, update_frame_by_data
import pandas as pd


def make_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


def min_max_normalization(array):
    """(x - min)/(max - min)"""
    slop = np.max(array, axis=0) - np.min(array, axis=0)
    interception = np.min(array, axis=0)
    new_array = (array - interception)/slop
    return new_array


def z_score_normalization(array):
    """(x-mean)/std"""
    slop = np.std(array, axis=0)
    interception = np.mean(array, axis=0)
    new_array = (array - interception) / slop
    return new_array


def mean_max_min_normalization(array):
    """(x-mean)/(max-min)"""
    slop = np.max(array, axis=0) - np.min(array, axis=0)
    interception = np.mean(array, axis=0)
    new_array = (array - interception) / slop
    return new_array


def run_normalization(raw_file_path):
    store_path = os.path.dirname(raw_file_path)

    raw_pd_data = pd.read_csv(raw_file_path)
    
    pd_data = LoadDataByPd()
    pd_data.set_pd(raw_pd_data)
    
    case_name = pd_data.get_case_name()
    label = pd_data.get_label()
    feature_name = pd_data.get_feature_name()
    raw_array = pd_data.get_feature_value()

    min_max_array = min_max_normalization(raw_array)
    z_score_array = z_score_normalization(raw_array)
    mean_min_max_array = mean_max_min_normalization(raw_array)

    pd_min_max = update_frame_by_data(case_name=case_name, label=label, feature_name=feature_name,
                                      feature_value=min_max_array)
    pd_z_score = update_frame_by_data(case_name=case_name, label=label, feature_name=feature_name,
                                      feature_value=z_score_array)
    pd_mean_min_max = update_frame_by_data(case_name=case_name, label=label, feature_name=feature_name,
                                           feature_value=mean_min_max_array)

    min_max_folder_path = os.path.join(store_path, "min_max")
    make_folder(min_max_folder_path)
    z_score_folder_path = os.path.join(store_path, "z_score")
    make_folder(z_score_folder_path)
    mean_min_max_folder_path = os.path.join(store_path, "mean_min_max")
    make_folder(mean_min_max_folder_path)

    pd_min_max.to_csv(os.path.join(min_max_folder_path, "min_max_normalization.csv"), index=None)
    pd_z_score.to_csv(os.path.join(z_score_folder_path, "z_score_normalization.csv"), index=None)
    pd_mean_min_max.to_csv(os.path.join(mean_min_max_folder_path, "mean_min_max_normalization.csv"), index=None)


if __name__ == '__main__':
    file_path = r"D:\my_fae_test\train_and_test.csv"
    run_normalization(raw_file_path=file_path)
    pass



