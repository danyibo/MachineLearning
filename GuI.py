from tkinter import *
from tkinter import messagebox
# import tkinter as tk
from tkinter import filedialog
from get_every_feature_csv import get_single_feature
import os
import pandas as pd
from tkinter import  ttk



def get_feature_name(root_path, feature_group, store_model_name,
                 normalizer_name, dim_name, selecter_name,
                 model_name, feature_number):
    """
    :param feature_group: 特征的类别，如first order, GLCM等
    :param store_model_name: 存放结果的名字
    :param normalizer_name: 归一化的方法
    :param selecter_name: 特征选择方法的名字
    :param dim_name: 降维的名字
    :param model_name: 模型的名称
    :param feature_number: 选择几个特征
    :return: 返回建模的特征名字
    """
    feature_path = os.path.join(
        root_path, feature_group, store_model_name, normalizer_name, dim_name,
        selecter_name+"_"+str(feature_number), model_name, model_name+"_coef.csv"
    )
    pd_feature = pd.read_csv(feature_path)
    feature_name = list(pd_feature["Unnamed: 0"])
    return feature_name  # 建模特征的名字列表



class Application(Frame):
    """特征选择辅助器"""

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widget()

    def get_file_path(self):
        self.file_path = filedialog.askopenfilename()
        Label(self, text=self.file_path, background='pink').grid(row=2, column=1,columnspan=4)

    def get_single_feature(self):
        get_single_feature(all_feature_path=self.file_path, store_name=self.input_store_name.get())

    def create_widget(self):
        """创建组件"""
        column_list = ["*"] * 7
        feature_group_name = ["firstorder", "glcm", "gldm", "glszm", "glrlm", "ngtdm", "shape"]
        for i, g in zip(range(0, 7), column_list):
            Label(self, text=g, width=10).grid(row=0, column=i)
        # 进行单一特征拆分
        Label(self, text="▧进行特征拆分▧", font=("方正舒体", 15)).grid(row=1, column=3, columnspan=2)

        # 选择路径：
        self.button_get_file_path = Button(self, text="LoadCsv", font=("黑体", 10), command=self.get_file_path, width=10)
        self.button_get_file_path.grid(row=2, column=0)
        # 拆分的label
        self.store_name_label = Label(self, text="*请输入保存名字：", font=("黑体", 10))
        self.store_name_label.grid(row=4, column=0)

        # 输入拆分特征的保存名字
        store_name = StringVar()
        self.input_store_name = Entry(self, textvariable=store_name)
        self.input_store_name.grid(row=4, column=1, columnspan=2)

        # 拆分单独的特征
        self.button_get_single_feature = Button(self, text="SplitFeature", command=self.get_single_feature, )
        self.button_get_single_feature.grid(row=4, column=3, sticky=E)

        Label(self, text="▧进行特征选择▧", font=("方正舒体", 15)).grid(row=5, column=3, columnspan=2, pady=20)

        # 处理 firstorder
        Label(self, text="特征类别", borderwidth=1, relief="solid", width=9).grid(row=6, column=0)
        Label(self, text="存放名称", borderwidth=1, relief="solid", width=9).grid(row=6, column=1)
        Label(self, text="归一化", borderwidth=1, relief="solid", width=9).grid(row=6, column=2)
        Label(self, text="降维", borderwidth=1, relief="solid", width=9).grid(row=6, column=3)
        Label(self, text="特征选择", borderwidth=1, relief="solid", width=9).grid(row=6, column=4)
        Label(self, text="模型名称", borderwidth=1, relief="solid", width=9).grid(row=6, column=5)
        Label(self, text="特征数量", borderwidth=1, relief="solid", width=9).grid(row=6, column=6)

        for index, feature in enumerate(feature_group_name):
            Label(self, text=str(feature), font=("Centaur", 12)).grid(row=7+index, column=0)
        # 创建store_name
        self.Enty_list = []
        for i, f in enumerate(feature_group_name):
            self.mode_store_name = StringVar()
            self.mode_store_name.set("result")
            self.entry = Entry(self, width=9, textvariable=self.mode_store_name).grid(row=7+i, column=1)
            self.Enty_list.append(self.mode_store_name)
        self.Enty_Dict = dict(zip(feature_group_name, self.Enty_list))

        self.Normaliz_list = []
        for nor_i, nor_f in enumerate(feature_group_name):
            self.mean_value = StringVar()
            self.mean_value.set("Mean")
            self.Normaliz_list.append(self.mean_value)
            self.mean = Entry(self, width=8, textvariable=self.mean_value).grid(row=7+nor_i, column=2)
        self.Normaliz_Dict = dict(zip(feature_group_name, self.Normaliz_list))

        for p_i, p_f in enumerate(feature_group_name):
            self.pcc = Label(self, text="PCC").grid(row=7+p_i, column=3)

        self.Feature_select_list = []
        for nor_i, nor_f in enumerate(feature_group_name):
            self.feature = StringVar()
            self.feature.set("KW")
            self.Feature_select_list.append(self.feature)
            self.feature = Entry(self, width=8, textvariable=self.feature).grid(row=7 + nor_i, column=4)
        self.Feature_select_Dict = dict(zip(feature_group_name, self.Feature_select_list))

        self.Model_list = []
        for nor_i, nor_f in enumerate(feature_group_name):
            self.model_value = StringVar()
            self.model_value.set("SVM")
            self.Model_list.append(self.model_value)
            self.model = Entry(self, width=8, textvariable=self.model_value).grid(row=7 + nor_i, column=5)
        self.Model_Dict = dict(zip(feature_group_name, self.Model_list))

        self.Feature_number_list = []
        for nor_i, nor_f in enumerate(feature_group_name):
            self.feature_value = IntVar()
            self.feature_value.set(10)
            self.Feature_number_list.append(self.feature_value)
            self.feature = Entry(self, width=8, textvariable=self.feature_value).grid(row=7 + nor_i, column=6)
        self.Feature_number_Dict = dict(zip(feature_group_name, self.Feature_number_list))

        # 确定选择完毕弹出一个窗口
        Button(self, text="选择完毕", command=self.chose_finished).grid(row=15, column=0, columnspan=2)





        self.sure = Button(self, text="进行合并", width=20, background="Gainsboro", command=self.chose_feature)
        self.sure.grid(row=16, column=0, columnspan=2)

    def chose_finished(self):
        messagebox.showinfo("选择", "选择完毕！")

    def chose_feature(self):
        try:
            root_path = os.path.dirname(self.file_path)
            all_selected_feature = []
            for feature_group in ["firstorder", "glcm", "gldm", "glszm", "glrlm", "ngtdm", "shape"]:
                store_model_name = self.Enty_Dict[feature_group].get()
                normalizer_name = self.Normaliz_Dict[feature_group].get()
                select_name = self.Feature_select_Dict[feature_group].get()
                model_name = self.Model_Dict[feature_group].get()
                feature_number = self.Feature_number_Dict[feature_group].get()
                selected_feature_name = get_feature_name(root_path=root_path,
                                         feature_group=feature_group,
                                         store_model_name=store_model_name,
                                            normalizer_name=normalizer_name,
                                         dim_name="PCC", selecter_name=select_name,
                                         model_name=model_name,
                                         feature_number=feature_number)

                all_selected_feature.append(selected_feature_name)
            for i in all_selected_feature:
                print(i)
        except:
            pass


root = Tk()
root.geometry('700x450+200+300')
root.title("FAE特征选择辅助器")
app = Application(master=root)
root.mainloop()