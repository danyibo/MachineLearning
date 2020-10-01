import os
import numpy as np

import pandas as pd
from scipy import stats
from scipy.stats import ttest_ind, levene
from scipy.stats import chi2_contingency
from scipy.stats import mannwhitneyu
from collections import Counter


def get_p_value_by_feature(pd_train, pd_test, feature_name):
    """
    对特征进行统计检验，保证在两个类别之间的特征是有差异的，没有差异的特征去除掉

    :param pd_train: 可以是train 可以是label 为 1
    :param pd_test: 可以是test 可以是label 为 0
    :param feature_name: 特征的名字
    :return: p值  小于 0.05 是有差异  大于 0.05 是无差异
    """
    # pd_train = pd.read_csv(train_path)
    # pd_test = pd.read_csv(test_path)

    train_feature = pd_train[feature_name]
    test_feature = pd_test[feature_name]

    train_feature_class = len(set(train_feature))
    test_feature_class = len(set(test_feature))

    if train_feature_class > 2 and test_feature_class > 2:
        # 说明这是连续变量，就使用T检验或者是Ｕ检验
        train_feature_mean = np.mean(train_feature)
        test_feature_mean = np.mean(test_feature)

        train_feature_std = np.std(train_feature)
        test_feature_std = np.std(test_feature)

        # 进行正态性和方差齐性检验
        sta_value, p_value = levene(train_feature, test_feature)  # 方差齐性
        sta_train, p_value_train = stats.kstest(train_feature, "norm", (train_feature_mean, train_feature_std))
        sta_train, p_value_test = stats.kstest(test_feature, "norm", (test_feature_mean, test_feature_std))
        # print(p_value_train, p_value_test, p_value)
        if p_value_train >= 0.05 and p_value_test >= 0.05 and p_value >= 0.05:

            statistic, pvalue_t = ttest_ind(train_feature, test_feature)

            # print(feature_name + " t检验:", round(pvalue_t, 3))
            return round(pvalue_t, 3)
        else:

            stat_num, p_m_value = mannwhitneyu(train_feature, test_feature)

            # print(feature_name + " u检验:", round(p_m_value, 3))
            return round(p_m_value, 3)

    if train_feature_class == 2 and test_feature_class == 2:
        # 进行卡方检验
        train_class_1, train_class_2 = Counter(train_feature).most_common()
        test_class_1, test_class_2 = Counter(test_feature).most_common()

        kf_data = np.array(
            [[np.array(train_class_1[-1]), np.array(test_class_1[-1])], [np.array(train_class_2[-1]), np.array(test_class_2[-1])]])
        # print(kf_data)
        a, p_value, b, c = chi2_contingency(kf_data)
        # print(feature_name+"卡方检验: p_value={:.4f}".format(p_value))
        return round(p_value,3)

if __name__ == '__main__':
    pass