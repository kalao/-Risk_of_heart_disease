
import ipywidgets as widgets	# 控件库
from IPython.display import display	# 显示控件的方法
import pandas as pd
#前端显示界面
class InteractiveFigure(object):
    def __init__(self):
        self.iis = widgets.Dropdown(options=[("是否可测胆固醇",0),("可以", 1), ("不可以", 2)],label="是否可测胆固醇")
        self.area = widgets.Dropdown(options=[("区域",0),("WPRA", 1), ("WPRB", 2)],label="区域")
        self.ill= widgets.Dropdown(options=[("是否有糖尿病",0),("有", 1), ("无", 2)],label="是否有糖尿病")
        self.sex=widgets.Dropdown(options=[("性别",0),("男", 1), ("女", 2)],label="性别")
        self.age=widgets.Dropdown(options=[("年龄",0),("40", 1), ("50", 2),("60",3),("70",4)],label="年龄")
        self.smoke=widgets.Dropdown(options=[("是否抽烟",0),("是", 1), ("否", 2)],label="是否抽烟")
        self.btn = widgets.Button(description = "抽取子图", tooltip = 'this is a button')   
        self.op=[self.iis,self.area,self.ill,self.sex,self.age,self.smoke,self.btn]
    def Display(self):
        display(*self.op)
    def setButton(self,func):
        self.func=func
        self.btn.on_click(self.fuc)
    def fuc(self,_):
        self.func(self.op[1:6])
    def getPatient(self):
        
        pass
class SubInteractiveFigure(InteractiveFigure):
    def __init__(self):
        super().__init__()
        self.dan=widgets.Text("请输入胆固醇值")
        self.shou=widgets.Text("请输入收缩压值")
#         self.age=widgets.Text("请输入年龄")
#         self.op[4]=self.age
        op=self.op[0:-1]
        #为什么self.op[0:-1].append(self.dan)就错了
        op.extend([self.dan,self.shou,self.op[-1]])
        self.op=op

class SSubInteractiveFigure(SubInteractiveFigure):
    def __init__(self):
         super().__init__()
         self.btn_predict = widgets.Button(description = "预测", tooltip = 'this is a button1')  
         self.op.append(self.btn_predict)
    def setButtonPredict(self,func):
        self.funcP=func
        self.btn_predict.on_click(self.fuco)
        
    def fuco(self,_):
        self.funcP(self.op,self)
    def getPatient(self):
        return (self.area.label,self.ill.label,self.sex.label,self.age.label,self.smoke.label,self.dan.value,self.shou.value)

