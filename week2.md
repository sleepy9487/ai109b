## 爬山演算法
* hillClimbing.py
```
def hillClimbing(s, maxGens, maxFails):   # 爬山演算法的主體函數
    print("start: ", s.str())             # 印出初始解
    fails = 0                             # 失敗次數設為 0
    # 當代數 gen<maxGen，且連續失敗次數 fails < maxFails 時，就持續嘗試尋找更好的解。
    for gens in range(maxGens):
        snew = s.neighbor()               #  取得鄰近的解
        sheight = s.height()              #  sheight=目前解的高度
        nheight = snew.height()           #  nheight=鄰近解的高度
        if (nheight >= sheight):          #  如果鄰近解比目前解更好
            print(gens, ':', snew.str())  #    印出新的解
            s = snew                      #    就移動過去
            fails = 0                     #    移動成功，將連續失敗次數歸零
        else:                             #  否則
            fails = fails + 1             #    將連續失敗次數加一
        if (fails >= maxFails):
            break
    print("solution: ", s.str())          #  印出最後找到的那個解
    return s                              #    然後傳回。
```
>s是隨機設定一個值,MaxGens是最高執行次數,MaxFail是最高錯誤次數,超過即停止
neighbor為答案決定

* solution.py
```
class Solution: # 解答的物件模版 (類別)
    def __init__(self, v, step = 0.01):
        self.v = v       # 參數 v 為解答的資料結構
        self.step = step # 每一小步預設走的距離

    # 以下兩個函數至少需要覆蓋掉一個，否則會無窮遞迴
    def height(self): # 爬山演算法的高度函數
        return -1*self.energy()               # 高度 = -1 * 能量

    def energy(self): # 尋找最低點的能量函數
        return -1*self.height()               # 能量 = -1 * 高度
```
>能量與高度為相反函數,當尋找的高度越高,要取得的能量越低(物理學角度)  

* solutionNumber.py
```
from hillClimbing import hillClimbing # 引入解答類別
from solution import Solution
import random

class SolutionNumber(Solution):
    def neighbor(self): # 單變數解答的鄰居函數。
        x = self.v
        dx= self.step               # x:解答 , dx : 移動步伐大小
        xnew = x+dx if random.random() > 0.5 else x-dx # 用亂數決定向左或向右移動
        return SolutionNumber(xnew) # 建立新解答並傳回。

    def energy(self):               # 能量函數
        x = self.v                  # x:解答
        return abs(x*x-4)           # 能量函數為 |x^2-4|

    def str(self): # 將解答轉為字串，以供印出觀察。
        return "energy({:.3f})={:.3f}".format(self.v, self.energy())
```

* hillClimginNumber.py
```
from hillClimbing import hillClimbing # 引入爬山演算法類別
from solutionNumber import SolutionNumber # 引入平方根解答類別

# 執行爬山演算法 (從「解答=0.0」開始尋找, 最多十萬代、失敗一千次就跳出。
hillClimbing(SolutionNumber(0.0), 100000, 1000)
```
* result1
```
start:  energy(0.000)=4.000
0 : energy(-0.010)=4.000 
1 : energy(-0.020)=4.000 
6 : energy(-0.030)=3.999 
7 : energy(-0.040)=3.998 
8 : energy(-0.050)=3.998 
10 : energy(-0.060)=3.996
11 : energy(-0.070)=3.995
.
.
.
401 : energy(-1.940)=0.236
403 : energy(-1.950)=0.197
406 : energy(-1.960)=0.158
407 : energy(-1.970)=0.119
408 : energy(-1.980)=0.080
409 : energy(-1.990)=0.040
410 : energy(-2.000)=0.000
solution:  energy(-2.000)=0.000
```
* result2
```
start:  energy(0.000)=4.000
0 : energy(0.010)=4.000
2 : energy(0.020)=4.000
4 : energy(0.030)=3.999
6 : energy(0.040)=3.998
9 : energy(0.050)=3.998
.
.
.
397 : energy(1.930)=0.275
399 : energy(1.940)=0.236
402 : energy(1.950)=0.197
406 : energy(1.960)=0.158
407 : energy(1.970)=0.119
410 : energy(1.980)=0.080
414 : energy(1.990)=0.040
416 : energy(2.000)=0.000
```

>亂數決定向左或向右(數字來看為正or負),最終會呈現2or-2兩種結果
>每一次步伐為0.01
-----------------
* solutionArray.py
```
from solution import Solution
from random import random, randint

class SolutionArray(Solution):
    def neighbor(self):    #  多變數解答的鄰居函數。
        nv = self.v.copy()                   #  nv=v.clone()=目前解答的複製品
        i = randint(0, len(nv)-1) #  隨機選取一個變數
        if (random() > 0.5):                    #  擲骰子決定要往左或往右移
            nv[i] += self.step
        else:
            nv[i] -= self.step
        return SolutionArray(nv)                    #  傳回新建的鄰居解答。

    def energy(self):      #  能量函數
        x, y, z =self.v
        return x*x+3*y*y+z*z-4*x-3*y-5*z+8         #  (x^2+3y^2+z^2-4x-3y-5z+8)

    def str(self):    #  將解答轉為字串的函數，以供列印用。
        return "energy({:s})={:f}".format(str(self.v), self.energy())
```
>尋找三個函數組成三個維度的最低點  

* hillClimbingArray.py
```
from hillClimbing import hillClimbing # 引入爬山演算法類別
from solutionArray import SolutionArray # 引入平方根解答類別

# 執行爬山演算法 (最多十萬代、失敗一千次就跳出)。
hillClimbing(SolutionArray([1,1,1]), 100000, 1000)
```
* result
```
start:  energy([1, 1, 1])=1.000000
2 : energy([1.01, 1, 1])=0.980100
3 : energy([1.01, 0.99, 1])=0.950400
5 : energy([1.01, 0.99, 1.01])=0.920500
6 : energy([1.02, 0.99, 1.01])=0.900800
8 : energy([1.02, 0.99, 1.02])=0.871100
9 : energy([1.03, 0.99, 1.02])=0.851600
.
.
.

722 : energy([2.000000000000001, 0.49999999999999956, 2.459999999999991])=-2.998400
729 : energy([2.000000000000001, 0.49999999999999956, 2.469999999999991])=-2.999100
742 : energy([2.000000000000001, 0.49999999999999956, 2.4799999999999907])=-2.999600
744 : energy([2.000000000000001, 0.49999999999999956, 2.4899999999999904])=-2.999900
746 : energy([2.000000000000001, 0.49999999999999956, 2.4999999999999902])=-3.000000
solution:  energy([2.000000000000001, 0.49999999999999956, 2.4999999999999902])=-3.000000
```
>呼叫solutionArray.py並以1.1.1為起點,尋找最低點
---------------------
* solutionEquation
```
"""
A X = B ，求 X 是多少？

範例：題目來源: http://mail.im.tku.edu.tw/~idliaw/LinTup/99ie/99IEntu.pdf

4a+3b+6c=1
1a+1b+2c=2
2a+1b+3c=-1
"""

from random import random, randint
import numpy as np
from numpy import linalg as LA
from solution import Solution

A = np.array([[4,3,6],[1,1,2],[2,1,3]])
B = np.array([[1,2,-1]]).transpose()

class SolutionEquation(Solution):
    def neighbor(self):    #  多變數解答的鄰居函數。
        nx = self.v.copy()              #  複製目前解的矩陣
        rows = nx.shape[0]
        #  修改了這裡：最多改變 n 個維度(只是某些 n 維的例子可以，無法確定一定可以，除非能證明能量函數只有一個低點)
        for _ in range(rows):         #  原本只改一維，會找不到！
            i = randint(0, rows-1) #  隨機選取一個變數
            if (random() > 0.5):                    #  擲骰子決定要往左或往右移
                nx[i][0] += self.step * random()  #  原本是 nx.m[i][0] += self.step 
            else:
                nx[i][0] -= self.step * random()  #  原本是 nx.m[i][0] -= self.step 

        return SolutionEquation(nx)                    #  傳回新建的鄰居解答。

    def energy(self):      #  能量函數:計算 ||AX-B||，也就是 ||Y-B||
        X = self.v
        Y = A.dot(X)
        return LA.norm(Y-B, 2)

    def str(self):    #  將解答轉為字串的函數，以供列印用。
        return "energy({:s})={:f}".format(str(self.v.transpose()), self.energy())

    @classmethod
    def zero(cls):
        return SolutionEquation(np.zeros((3,1)))
```
>numpy用於建立陣列函數  
>Y=A.dot(X)->因為A是一個矩陣所以要取AX作為向量  
>norm=向量的長度
>LA.norm(Y-B,2) 為何是2? X"平方"+Y"平方"再"開根號"

* hillClimbingEquation
```
from hillClimbing import hillClimbing # 引入爬山演算法類別
from solutionEquation import SolutionEquation # 引入平方根解答類別

# 執行爬山演算法 (最多十萬代、失敗一千次就跳出)
hillClimbing(SolutionEquation.zero(), 100000, 1000)
```
* result
```
1203 : energy([[-1.42529587  1.93158769  0.18095713]])=1.304732
1205 : energy([[-1.41829124  1.93158769  0.1706058 ]])=1.304407
1206 : energy([[-1.41829124  1.93883757  0.16550204]])=1.302323
1208 : energy([[-1.41829124  1.94357257  0.15953453]])=1.300621
1209 : energy([[-1.41829124  1.94517164  0.15953453]])=1.300355
1214 : energy([[-1.41829124  1.95506303  0.15953453]])=1.299184
.
.
.
5949 : energy([[-4.9892791   3.0055213   1.99060407]])=0.004176
5981 : energy([[-4.9892791   2.99915406  1.99357157]])=0.003710
5990 : energy([[-4.98954993  2.99915406  1.99357157]])=0.003413
5993 : energy([[-4.99717523  2.99872894  1.99882006]])=0.001232
6658 : energy([[-4.99891107  3.00126221  1.99882006]])=0.001067
6754 : energy([[-4.99886389  3.00078811  1.99882006]])=0.000670
7749 : energy([[-4.99973472  3.00078811  1.99948185]])=0.000395
solution:  energy([[-4.99973472  3.00078811  1.99948185]])=0.000395
```
---------------------------------
* solutionScheduling.py
```
from random import random, randint, choice
from solution import Solution
import numpy as np

courses = [
{'teacher': '  ', 'name':'　　', 'hours': -1},
{'teacher': '甲', 'name':'機率', 'hours': 2},
{'teacher': '甲', 'name':'線代', 'hours': 3},
{'teacher': '甲', 'name':'離散', 'hours': 3},
{'teacher': '乙', 'name':'視窗', 'hours': 3},
{'teacher': '乙', 'name':'科學', 'hours': 3},
{'teacher': '乙', 'name':'系統', 'hours': 3},
{'teacher': '乙', 'name':'計概', 'hours': 3},
{'teacher': '丙', 'name':'軟工', 'hours': 3},
{'teacher': '丙', 'name':'行動', 'hours': 3},
{'teacher': '丙', 'name':'網路', 'hours': 3},
{'teacher': '丁', 'name':'媒體', 'hours': 3},
{'teacher': '丁', 'name':'工數', 'hours': 3},
{'teacher': '丁', 'name':'動畫', 'hours': 3},
{'teacher': '丁', 'name':'電子', 'hours': 4},
{'teacher': '丁', 'name':'嵌入', 'hours': 3},
{'teacher': '戊', 'name':'網站', 'hours': 3},
{'teacher': '戊', 'name':'網頁', 'hours': 3},
{'teacher': '戊', 'name':'演算', 'hours': 3},
{'teacher': '戊', 'name':'結構', 'hours': 3},
{'teacher': '戊', 'name':'智慧', 'hours': 3}
]

teachers = ['甲', '乙', '丙', '丁', '戊']

rooms = ['A', 'B']

slots = [
'A11', 'A12', 'A13', 'A14', 'A15', 'A16', 'A17',
'A21', 'A22', 'A23', 'A24', 'A25', 'A26', 'A27',
'A31', 'A32', 'A33', 'A34', 'A35', 'A36', 'A37',
'A41', 'A42', 'A43', 'A44', 'A45', 'A46', 'A47',
'A51', 'A52', 'A53', 'A54', 'A55', 'A56', 'A57',
'B11', 'B12', 'B13', 'B14', 'B15', 'B16', 'B17',
'B21', 'B22', 'B23', 'B24', 'B25', 'B26', 'B27',
'B31', 'B32', 'B33', 'B34', 'B35', 'B36', 'B37',
'B41', 'B42', 'B43', 'B44', 'B45', 'B46', 'B47',
'B51', 'B52', 'B53', 'B54', 'B55', 'B56', 'B57',
]

cols = 7

def randSlot() :
    return randint(0, len(slots)-1)

def randCourse() :
    return randint(0, len(courses)-1)


class SolutionScheduling(Solution) :
    def neighbor(self):    # 單變數解答的鄰居函數。
        fills = self.v.copy()
        choose = randint(0, 1)
        if choose == 0: # 任選一個改變 
            i = randSlot()
            fills[i] = randCourse()
        elif choose == 1: # 任選兩個交換
            i = randSlot()
            j = randSlot()
            t = fills[i]
            fills[i] = fills[j]
            fills[j] = t
        return SolutionScheduling(fills)                  # 建立新解答並傳回。

    def height(self) :      # 高度函數
        courseCounts = [0] * len(courses)
        fills = self.v
        score = 0
        # courseCounts.fill(0, 0, courses.length)
        for si in range(len(slots)):
            courseCounts[fills[si]] += 1
            #                        連續上課:好                   隔天:不好     跨越中午:不好
            if si < len(slots)-1 and fills[si] == fills[si+1] and si%7 != 6 and si%7 != 3:
                score += 0.1
            if si % 7 == 0 and fills[si] != 0: # 早上 8:00: 不好
                score -= 0.12
        
        for ci in range(len(courses)):
            if (courses[ci]['hours'] >= 0):
                score -= abs(courseCounts[ci] - courses[ci]['hours']) # 課程總時數不對: 不好
        return score

    def str(self) :    # 將解答轉為字串，以供印出觀察。
        outs = []
        fills = self.v
        for i in range(len(slots)):
            c = courses[fills[i]]
            if i%7 == 0:
                outs.append('\n')
            outs.append(slots[i] + ':' + c['name'])
        return 'score={:f} {:s}\n\n'.format(self.energy(), ' '.join(outs))
    
    @classmethod
    def init(cls):
        fills = [0] * len(slots)
        for i in range(len(slots)):
            fills[i] = randCourse()
        return SolutionScheduling(fills)
```
* hilClimginScheduling.py
```
from hillClimbing import hillClimbing # 引入爬山演算法類別
from solutionScheduling import SolutionScheduling # 引入平方根解答類別

# 執行爬山演算法 (最多3萬代、失敗一千次就跳出)
hillClimbing(SolutionScheduling.init(), 30000, 1000)
```
* result
```
solution:  score=-3.860000
 A11:電子 A12:電子 A13:電子 A14:電子 A15:系統 A16:系統 A17:系統
 A21:　　 A22:　　 A23:機率 A24:機率 A25:結構 A26:結構 A27:結構
 A31:　　 A32:演算 A33:演算 A34:演算 A35:離散 A36:離散 A37:離散
 A41:　　 A42:　　 A43:行動 A44:行動 A45:計概 A46:計概 A47:計概
 A51:　　 A52:線代 A53:線代 A54:線代 A55:視窗 A56:視窗 A57:視窗
 B11:　　 B12:工數 B13:工數 B14:工數 B15:軟工 B16:軟工 B17:軟工
 B21:　　 B22:媒體 B23:媒體 B24:媒體 B25:動畫 B26:動畫 B27:動畫
 B31:　　 B32:網路 B33:網路 B34:網路 B35:智慧 B36:智慧 B37:智慧
 B41:　　 B42:網站 B43:網站 B44:網站 B45:網頁 B46:網頁 B47:網頁
 B51:嵌入 B52:嵌入 B53:嵌入 B54:行動 B55:科學 B56:科學 B57:科學
```
>一開始運算時(上)有許多空格但經過多次運算後(下),空格都填滿了 
solution:  score=-3.900000
 A11:　　 A12:工數 A13:工數 A14:工數 A15:視窗 A16:視窗 A17:視窗
 A21:　　 A22:智慧 A23:智慧 A24:智慧 A25:動畫 A26:動畫 A27:動畫
 A31:　　 A32:嵌入 A33:嵌入 A34:嵌入 A35:演算 A36:演算 A37:演算
 A41:　　 A42:網路 A43:網路 A44:網路 A45:機率 A46:機率 A47:電子
 A51:　　 A52:計概 A53:計概 A54:計概 A55:媒體 A56:媒體 A57:媒體
 B11:　　 B12:軟工 B13:軟工 B14:軟工 B15:線代 B16:線代 B17:線代
 B21:　　 B22:離散 B23:離散 B24:離散 B25:網頁 B26:網頁 B27:網頁
 B31:　　 B32:行動 B33:行動 B34:行動 B35:網站 B36:網站 B37:網站
 B41:　　 B42:科學 B43:科學 B44:科學 B45:電子 B46:電子 B47:電子
 B51:　　 B52:系統 B53:系統 B54:系統 B55:結構 B56:結構 B57:結構
---------------------------------
## 模擬退火法
```
import math
import random

def P(e, enew, T): # 模擬退火法的機率函數
    if (enew < e):
        return 1
    else:
        return math.exp((e-enew)/T)

def annealing(s, maxGens) : # 模擬退火法的主要函數
    sbest = s                              # sbest:到目前為止的最佳解
    ebest = s.energy()                     # ebest:到目前為止的最低能量
    T = 100                                # 從 100 度開始降溫
    for gens in range(maxGens):            # 迴圈，最多作 maxGens 這麼多代。
        snew = s.neighbor()                # 取得鄰居解
        e    = s.energy()                  # e    : 目前解的能量
        enew = snew.energy()               # enew : 鄰居解的能量
        T  = T * 0.995                     # 每次降低一些溫度
        if P(e, enew, T)>random.random():  # 根據溫度與能量差擲骰子，若通過
            s = snew                       # 則移動到新的鄰居解
            print("{} T={:.5f} {}".format(gens, T, s.str())) # 印出觀察

        if enew < ebest:                 # 如果新解的能量比最佳解好，則更新最佳解。
            sbest = snew
            ebest = enew
    
    print("solution: {}", sbest.str())     # 印出最佳解
    return sbest                           # 傳回最佳解

```
>退火-例子可以舉金門菜刀製作(敲刀-高溫敲擊可以很堅固)  
>一種改變材料微結構且進而改變如硬度和強度等機械性質的熱處理
>爬山演算法跟模擬退火法的其中一個差別在於爬山是高度,退火是能量
>退火法把最佳解比喻為彈珠,即使遇到第一次窪地也不斷努力往上爬,用溫度與機率讓他能夠克服高地落下另一個窪地
>跟爬山的差別是爬山利用失敗次數控制,而退火是溫度與機率

* 模擬退火參考資料
![模擬退火法](https://zh.wikipedia.org/wiki/%E6%A8%A1%E6%8B%9F%E9%80%80%E7%81%AB)
