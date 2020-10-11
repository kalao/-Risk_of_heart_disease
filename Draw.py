import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import seaborn as sns
class Draw(object):
    def __init__(self):
        pass
    def show(self):
        pass
class Draw_subp(Draw):
    def __init__(self,data):
        self.data=data
    def show(self):
        '''
        创建绘制对象，ax1是外层,ax2,ax3是内部左右两层
        '''
        data=self.data
        fig = plt.figure()
        # ax = plt.axes()  # standard axes
        ax1,ax2,ax3=  fig.add_axes([0,0,2.9,2.3]),fig.add_axes([0.1,0.1,1.3,2.1]),fig.add_axes([1.5,0.1,1.3,2.1])
        axes=[[0 for j in range(4) ] for i in range(4)]
        for i in range(4):
            for j in range(4):
                axes[i][j]=fig.add_axes([0.2+j*0.7,1.7-0.5*i,0.4,0.4])

        ax1.set_title(u'Residents of wprA subregion with diabetes mellitus')
        ax1.set_xlabel(u'\ncholesterol(mmol/l)')
        ax1.set_xticks([])
        ax1.set_yticks([])


        ax2.set_title(u'man')
        ax3.set_title(u'female')
        for ax in [ax2,ax3]:
            ax.spines['right'].set_color('none')
            ax.spines['bottom'].set_color('none') 
            ax.spines['left'].set_color('none') 
            ax.set_xticks([])
            ax.set_yticks([])

        my_colormap = LinearSegmentedColormap.from_list(
            "", ["#8cd40f", "#f8fb12", "#f66c06", "#fd1414", "#98011a"])
        def drawHeatMap(axes, my_colormap):
                    # # 绘制热力图
            
            age = 70   
            for i in range(4):
                for j in range(4):
                    xTick = False
                    yTick = False
                    # 胆固醇
                    if i == 3:
#                         if iis.index==2:
#                             xTick=False
#                         if iis.index==1:
                        xTick = [4,5,6,7,8]
                        # axes[i, j].set_xticks([4, 5, 6, 7, 8])

                    # 收缩压
                    if j == 3:
                        # axes[i, j].set_yticks([120, 140, 160, 180])
                        yTick = [180, 160, 140, 120]

                    sns.heatmap(data[i][j],
                                vmin=1,
                                vmax=5,
                                linewidths=0.5,
                                cbar=False,
                                xticklabels=xTick,
                                yticklabels=yTick,
                                ax=axes[i][j],
                                linecolor='black',
                                cmap=my_colormap)
                    axes[i][j].yaxis.set_ticks_position('right')
                    # 吸烟与不吸烟
                    if i == 0:
                        if j % 2 == 0:
                            axes[i][j].set_title(u'Non-smoking')
                        else:
                            axes[i][j].set_title(u'smoking')
                    # 年龄
                    if j == 0:
                        axes[i][j].set_ylabel(str(age))
                        age -= 10
        drawHeatMap(axes, my_colormap)

class DataExtract(object):
    def __init__(self,op,data):
        self.oop=list(map(lambda x: x if x.index!=0 else None ,op)) 
        self.data=data
        self.CL=True
        self.grouped=self.preSolve()
        
    def preSolve(self):
        v=['区域','是否有糖尿病','性别','年龄','是否抽烟']
        Fl=True
        C=False
        for index,o in enumerate(self.oop):
            if o!=None:
                C=True
                if index==3:
                    if Fl:
                        con=self.data[v[index]]==int(o.label)
                        Fl=False
                    else:    
                        con=(con)&(self.data[v[index]]==int(o.label))
                else:
                    if Fl:
                        con=self.data[v[index]]==o.label
                        Fl=False
                    else:
                        con=(con)&(self.data[v[index]]==o.label)
            else:
                self.CL=False
        self.data= self.data[con] if C else self.data
        return self.data.groupby(v)
    def solve(self):
        d1={'70':0,'60':1,'50':2,'40':3}
        d2={'男否':0,'男是':1,'女否':2,'女是':3}
        if not self.CL:
            Data=[[ 0 for j in range(4)] for i in range(4)]
            for i,(index,data) in  enumerate(self.grouped):
                ii=d1[str(data.iloc[0]['年龄'])]
                jj=d2[str(data.iloc[0]['性别'])+str(data.iloc[0]['是否抽烟'])]
                Data[ii][jj]=data.sort_values(by=['收缩压','胆固醇'],ascending=[False,True])['风险'].values.reshape(4,5)
            return Data

