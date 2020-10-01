import pandas as pd
import numpy as np
import os

old_path = r"E:\my_fea\train_and_test.csv"
new_path = r"E:\my_fea\GradientBoosting\elected_train_and_test.csv"

pd_old = pd.read_csv(old_path)
pd_new = pd.read_csv(new_path)

new_feature_name = pd_new.columns[2:]

feature_name = pd_old.columns[2:]


