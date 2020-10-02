from tkinter import *
from tkinter import messagebox
# import tkinter as tk
from tkinter import filedialog
from get_every_feature_csv import get_single_feature
import os




class Application(Frame):
    """特征选择辅助器"""
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widget()
        

    def get_file_path(self):
        self.file_path = filedialog.askopenfilename()
        Label(self, text=self.file_path, background='pink').grid(row=1, column=1)



    def get_single_feature(self):
        get_single_feature(all_feature_path=self.file_path, store_name=self.input_store_name.get())

    def create_widget(self):
        """创建组件"""



        # 选择路径

        Label(self, text="请选择特征路径", background='Lavender').grid(row=1, column=0)
        self.button_get_file_path = Button(self, text="LoadCsv",command=self.get_file_path, )
        self.button_get_file_path.grid(row=1, column=2)

        # Label(self, text=" ").grid(row=2, colunm=0)


        # # 拆分的label
        self.store_name_label = Label(self, text="请输入保存名字", background='Lavender')
        self.store_name_label.grid(row=3, column=0)
        #
        # # # 输入拆分特征的保存名字
        store_name = StringVar()
        self.input_store_name = Entry(self, textvariable=store_name, width=10)
        self.input_store_name.grid(row=3, column=1)
        #
        # # # 拆分单独的特征
        self.button_get_single_feature = Button(self, text="SplitFeature",
                                                command=self.get_single_feature,)
        self.button_get_single_feature.grid(row=3, column=2)
        #
        Label(self, text="特征选择", font=("方正舒体")).grid(row=4, column=0)
        Label(self, text="选择特征类别", background='Lavender').grid(row=5, column=0)


        # 创建复选框
        self.v1 = IntVar()
        self.v1.set(1)
        self.c1 = Checkbutton(self, text="firstorder", onvalue=1, offvalue= 0, variable=self.v1)
        self.c1.grid(row=5, column=1)

        self.v2 = IntVar()
        self.v2.set(1)
        self.c2 = Checkbutton(self, text="glcm", onvalue=1, offvalue= 0, variable=self.v2)
        self.c2.grid(row=5, column=2)

        self.v3 = IntVar()
        self.v3.set(1)
        self.c3 = Checkbutton(self, text="gldm", onvalue=1, offvalue=0, variable=self.v3)
        self.c3.grid(row=5, column=3)

        self.v4 = IntVar()
        self.v4.set(1)
        self.c4 = Checkbutton(self, text="glrlm", onvalue=1, offvalue=0, variable=self.v4)
        self.c4.grid(row=5, column=4)

        self.v5 = IntVar()
        self.v5.set(1)
        self.c5 = Checkbutton(self, text="glszm", onvalue=1, offvalue=0, variable=self.v5)
        self.c5.grid(row=5, column=5)

        self.v6 = IntVar()
        self.v6.set(1)
        self.c6 = Checkbutton(self, text="ngtdm", onvalue=1, offvalue=0, variable=self.v6)
        self.c6.grid(row=5, column=6)

        self.v7 = IntVar()
        self.v7.set(1)
        self.c7 = Checkbutton(self, text="shape", onvalue=1, offvalue=0, variable=self.v7)
        self.c7.grid(row=5, column=7)


        # 特征类别确定
        self.button_fature_group = Button(self, text="确定", command=self.sure_feature_group)
        self.button_fature_group.grid(row=5, column=8)
        
        Label(self, text="输入保存模型名称").grid(row=6, column=0)
        self.store_model_name = StringVar()
        self.store_model_enty = Entry(self, textvariable=self.store_model_name, width=10)
        self.store_model_enty.grid(row=6, column=1)

        # 降维方法选择
        Label(self, text="降维方法").grid(row=7, column=0)
        self.dim_value = IntVar()
        self.dim_value.set(1)
        self.dim = Radiobutton(self, text="PCC", value=1)
        self.dim.grid(row=7, column=1)

        # 特征选择方法选择
        Label(self, text="特征选择方法").grid(row=8, column=0)
        self.f_v1 = IntVar()
        self.f1 = Checkbutton(self, text="Mean", )


    def sure_feature_group(self):
        feature_group = []
        if self.v1.get() == 1:
            feature_group.append("firstorder")
        if self.v2.get() == 1:
            feature_group.append("glcm")
        if self.v3.get() == 1:
            feature_group.append("gldm")
        if self.v4.get() == 1:
            feature_group.append("glrlm")
        if self.v5.get() == 1:
            feature_group.append("glszm")
        if self.v6.get() == 1:
            feature_group.append("ngtdm")
        if self.v7.get() == 1:
            feature_group.append("shape")
        for g in feature_group:
            store_model_path = os.path.join(g, self.store_model_name.get())
            if self.dim_value.get() == 1:
                sub_path = os.path.join(store_model_path, "PCC")
                print(sub_path)




root = Tk()
root.geometry('700x300+200+300')
root.title("FAE特征选择辅助器")
app = Application(master=root)
root.mainloop()