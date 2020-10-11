from InteractiveFigure import *
from Model import *
from Patient import *
from Draw import *
import pandas as pd
def funcc(_):
    op=_
    df=pd.read_excel("可测胆固醇地区_4.xlsx")
    s=DataExtract(op,df)
    data=s.solve()
#     print(data)
    d=Draw_subp(data)
    d.show()
model=Model("train.xlsx","test.xlsx")
model.train()

total_data=pd.read_excel("可测胆固醇地区_4.xlsx")
def getRealValue(con):
    global total_data
    res=(total_data['区域']==con[0])&(total_data['是否有糖尿病']==con[1])&(total_data['性别']==con[2])
    res=res&(total_data['年龄']==con[3])&(total_data['是否抽烟']==con[4])&(total_data['收缩压']==con[5])
    res=res&(total_data['胆固醇']==con[6])
    return total_data[res]['风险'].values
def predict(_,sub):
    global model 
#     print(patient)
    Patient=sub.getPatient()
    person=patient(*Patient)
    x=person.getX()
    print(person.getRX())
    print("真实值:{}".format(getRealValue(person.getRX())))
    print("预测风险值:{}".format(model.predict(x)))
    
sub=SSubInteractiveFigure()
sub.setButton(funcc)
sub.setButtonPredict(predict)
sub.Display()

