class patient(object):
    def __init__(self,area,diabetes,sex,age,smoke,cholesterol=None,systolic_pressure=None):
        self.area=area
        self.diabetes=diabetes
        self.sex=sex
        self.smoke=smoke
        self.age=self.setAge(age)
        self.Cholesterol=self.setCholesterol(cholesterol)
        self.SystolicPressure=self.setSystolicPressure(systolic_pressure) 
        self.RE={"WPRA":0,"WPRB":1,"有":1,"无":0,"女":0,"男":1,"是":1,"否":0} 
#     def __init__(self,age,c,s):
#         self.age=self.setAge(age)
#         self.Cholesterol=self.setCholesterol(c)
#         self.SystolicPressure=self.setSystolicPressure(s)        
    def setAge(self,age):
        if isinstance(age,str):
            age=int(age)
        elif not isinstance(age,int):
            raise ValueError("age type  is invalid")
        if age<40 or age>70:
            raise ValueError("age is invalid")
        DIR=[40,50,60,70]
        index=(age-40+5)//10

        return DIR[index]
    def setCholesterol(self,Cholesterol):
        if isinstance(Cholesterol,str):
            Cholesterol=float(Cholesterol)
        elif not isinstance(Cholesterol,float) or not isinstance(Cholesterol,int) :
            raise ValueError("Cholesterol type  is invalid")
        if Cholesterol<4 or Cholesterol>8:
            raise ValueError("Cholesterol is invalid")
        DIR=[4,5,6,7,8]
        index=int(Cholesterol-4+0.5)
        return DIR[index]
    def setSystolicPressure(self,SystolicPressure):
        if isinstance(SystolicPressure,str):
            SystolicPressure=float(SystolicPressure)
        elif not isinstance(SystolicPressure,float) or not isinstance(SystolicPressure,int) :
            raise ValueError("SystolicPressure type  is invalid")
        DIR=[120,140,160,180]
        if SystolicPressure<120 or SystolicPressure>180:
            raise ValueError("SystolicPressure is invalid")
        index=int((SystolicPressure-120+10)/20)
        return DIR[index]
    def getX(self):
        d=[self.area,self.diabetes,self.sex,self.age,self.smoke,self.SystolicPressure,self.Cholesterol]
        def func1(STR):
               
            if STR in self.RE:
                return self.RE[STR]
            return int(STR)
        return [func1(i) for i in d]
    def getRX(self):
        return [self.area,self.diabetes,self.sex,self.age,self.smoke,self.SystolicPressure,self.Cholesterol]
    def show(self):
        print(self.age,self.Cholesterol,self.SystolicPressure)
