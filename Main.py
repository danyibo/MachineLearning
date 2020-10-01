import os
from FAE.DataContainer.data_balance import run_data_balance
from FAE.DataContainer.data_split import run_split
from FAE.DataContainer.normalizer import run_normalization
from FAE.DataContainer.select_feature import run_select_feature_by_GradientBoosting
from FAE.DataContainer.select_feature import run_select_feature_by_std


def run_select_feature():
    root_path = r"Y:\DYB\data_and_result\doctor tao"
    roi_list = ['roi_1', 'roi_2', 'roi_3', 'roi_4', 'roi_5', 'roi_6', 'roi_7', 'roi_8']
    for roi in roi_list:
        train_test_path = os.path.join(root_path, roi, 'new_train_test.csv')
        run_select_feature_by_std(train_test_path)

run_select_feature()