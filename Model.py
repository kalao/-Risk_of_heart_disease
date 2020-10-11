import pandas as pd
from sklearn import preprocessing
class Model(object):
    def __init__(self,trainFile,testFile):
        self.x,self.y,self.testx,self.testy=self.datasolver(trainFile,testFile)
    def func1(STR):
        RE={"WPRA":0,"WPRB":1,"有":1,"无":0,"女":0,"男":1,"是":1,"否":0}    
        if STR in RE:
            return RE[STR]
        return STR
    def datasolver(self,trainFile,testFile):
        train_data=pd.read_excel(trainFile)
        test_data=pd.read_excel(testFile)

        CAL={"胆固醇":1,"收缩压":1,"年龄":1,"性别":1,"是否有糖尿病":1,"是否抽烟":1,"区域":1}

        features_columns=[col for col in train_data.columns if col  not in ["风险"]]
        for featrue in features_columns:
            train_data[featrue]=train_data[featrue].map(lambda x:Model.func1(x))
            #train_data[featrue]=train_data[featrue]*CAL[featrue]
            test_data[featrue]=test_data[featrue].map(lambda x:Model.func1(x))
            #test_data[featrue]=test_data[featrue]*CAL[featrue]
        sca=preprocessing.MinMaxScaler()
        x=pd.DataFrame(sca.fit(train_data[features_columns]).transform(train_data[features_columns]))
        self.tmp=sca.fit(train_data[features_columns])
        test_x=pd.DataFrame(self.tmp.transform(test_data[features_columns]))
        y=train_data['风险'].values
        test_y=test_data['风险'].values
        return (x,y,test_x,test_y)
    def Datasolver(self,x):
        return pd.DataFrame(self.tmp.transform([x]))
    def train(self):
        from sklearn import svm
        self.clf=svm.SVC(kernel='poly',C=1,degree=3,probability=True,decision_function_shape='crammer_singer')
        self.clf.fit(self.x,self.y)
    def predict(self,x):
        return round(self.clf.predict(self.Datasolver(x))[0])


