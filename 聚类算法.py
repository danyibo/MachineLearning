from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
import os



from sklearn.preprocessing import StandardScaler, MinMaxScaler, Normalizer
from MachineLearning.load_data import LoadData, update_frame_by_data
from Tool.FolderProcress import make_folder


def get_k_means_label(data_path, store_path, store_name):
    data = pd.read_csv(data_path)
    data_load = LoadData()
    data_load.set_pd_data(data)
    case_name, label, feature_name, array = data_load.get_element()
    array = StandardScaler().fit_transform(array)
    array = np.transpose(array)
    k_means_model = KMeans(n_clusters=6).fit(array)
    labels = k_means_model.labels_
    # result = update_frame_by_data(case_name=feature_name, feature_name=case_name,
    #                               feature_value=array, label=labels)

    # result.to_csv(os.path.join(r"Y:\DYB\data_and_result\doctor tao\roi_3", "聚类.csv"),
    #               index=None)
    label_0_feature = ["CaseName", "label"] + []
    label_1_feature = ["CaseName", "label"] + []
    label_2_feature = ["CaseName", "label"] + []
    label_3_feature = ["CaseName", "label"] + []
    label_4_feature = ["CaseName", "label"] + []
    label_5_feature = ["CaseName", "label"] + []

    for feature, l in zip(feature_name, labels):
        if l == 0:
            label_0_feature.append(feature)
        elif l == 1:
            label_1_feature.append(feature)
        elif l == 2:
            label_2_feature.append(feature)
        elif l == 3:
            label_3_feature.append(feature)
        elif l == 4:
            label_4_feature.append(feature)
        elif l == 5:
            label_5_feature.append(feature)

    origin_feature = pd.read_csv(data_path)
    group_1_feature = origin_feature[label_0_feature]
    group_2_feature = origin_feature[label_1_feature]
    group_3_feature = origin_feature[label_2_feature]
    group_4_feature = origin_feature[label_3_feature]
    group_5_feature = origin_feature[label_4_feature]
    group_6_feature = origin_feature[label_5_feature]

    group_1_feature.to_csv(os.path.join(make_folder(os.path.join(store_path, "group_1")),
                                        store_name + ".csv"), index=None)
    group_2_feature.to_csv(os.path.join(make_folder(os.path.join(store_path, "group_2")),
                                        store_name + ".csv"), index=None)
    group_3_feature.to_csv(os.path.join(make_folder(os.path.join(store_path, "group_3")),
                                        store_name + ".csv"), index=None)
    group_4_feature.to_csv(os.path.join(make_folder(os.path.join(store_path, "group_4")),
                                        store_name + ".csv"), index=None)
    group_5_feature.to_csv(os.path.join(make_folder(os.path.join(store_path, "group_5")),
                                        store_name + ".csv"), index=None)
    group_6_feature.to_csv(os.path.join(make_folder(os.path.join(store_path, "group_6")),
                                        store_name + ".csv"), index=None)


data_path = r"Y:\DYB\data_and_result\doctor tao\Submodl20201124\train_and_test.csv"
store_path = r"Y:\DYB\data_and_result\doctor tao\Submodl20201124"
store_name = "train_and_test"
get_k_means_label(data_path, store_path, store_name)
