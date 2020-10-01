from tkinter import *
from FAE.Main import run_normalization, run_split, run_data_balance, run_select_feature_by_std
import os


root = Tk()
root.wm_title("机器学习软件")
root.geometry('600x400')

file_path = r"D:\my_fae_test\train_and_test.csv"


def do_normalization():
    global file_path, root
    label = Label(root, text='归一化完成，请查看数据！', background='pink')
    label.pack()
    run_normalization(file_path)


def do_select_feature():
    global file_path, root
    for i in ['mean_min_max', 'min_max', 'z_score']:
        store_path = os.path.dirname(file_path)
        normal_file_path = os.path.join(store_path, i, i+'_normalization.csv')
        run_select_feature_by_std(normal_file_path)
    label = Label(root, text='特征选择完成，请查看数据！', background='pink')
    label.pack()


def do_split():
    global file_path, root
    store_path = os.path.dirname(file_path)
    for i in ['mean_min_max', 'min_max', 'z_score']:
        select_file_path = os.path.join(store_path, i, 'FeatureSelectedByStd', 'elected_train_and_test.csv')
        run_split(select_file_path)
    label = Label(root, text='数据拆分完成，请查看数据！', background='pink')
    label.pack()


def do_balance():
    global file_path, root
    store_path = os.path.dirname(file_path)
    for i in ['mean_min_max', 'min_max', 'z_score']:
        train_path = os.path.join(store_path, i, 'FeatureSelectedByStd', 'train.csv')
        run_data_balance(train_path)
    label = Label(root, text='数据平衡完成，请查看数据！', background='pink')
    label.pack()


normalization_button = Button(root, text='归一化', command=do_normalization)
normalization_button['width'] = 40


select_feature_button = Button(root, text='特征选择', command=do_select_feature)
select_feature_button['width'] = 40

split_data_button = Button(root, text='拆分数据', command=do_split)
split_data_button['width'] = 40

data_balance_button = Button(root, text='数据平衡', command=do_balance)
data_balance_button['width'] = 40

normalization_button.pack()
select_feature_button.pack()
split_data_button.pack()
data_balance_button.pack()
root.mainloop()