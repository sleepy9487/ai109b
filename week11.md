## 科學函式庫
* numpy - 矩陣、向量運算(很重要的套件)  
* numpy  
```
>>> import numpy as np
>>> a = np.arange(0,4)  
>>> b = np.arange(1,5)
>>> np.add(a,b)
array([1, 3, 5, 7])
>>> a = np.arange(0,4)
>>> a
array([0, 1, 2, 3])
>>> b = np.arange(1,5)
>>> b
array([1, 2, 3, 4])
>>> b>a
array([ True,  True,  True,  True])
>>> a*b
array([ 0,  2,  6, 12])
>>> a.shape
(4,)
>>> a.shape = (2,2)
>>> a
array([[0, 1],
       [2, 3]])
>>> a.shape = (4,)
>>> a
array([0, 1, 2, 3])
>>> a[2:4]
array([2, 3])
>>> a[1:4:2]
array([1, 3])
>>> a[::-1]
array([3, 2, 1, 0])
>>> quit()
```  
>運用numpy : import numpy as np  
>np.arange(x,y) : 設立 起始點x~y-1的數值  
>np.add(x,y) : 兩矩陣相加(相對應的位置) 比如 a = [1,2], b = [2,3] ,那麼add就是array[1+2,2+3]  
>.shape : 知道矩陣為幾乘幾 .shape(x,y)重設為幾x幾  
>可以使用簡單的a+b a*b等 前者回傳數值,後者回傳True or False  
>a[x:y:z] : a矩陣裡大於等於x,小於y,隨機取z個  
>np.linspace(x,y,z) : 從x~y分成z個  
>np.random.randint(0,20,7) 數字0~20取隨機7個  
>np.linalg.det(x) X矩陣的行列式
* matplotlib - 繪圖工具
> subplot(numRows,numCols ,plotNum) 列(橫)x行(直)的圖選第plotNum個
  > subplot(222) : 意思是有兩列第二行第二個圖
* scupy - numpy的擴充版
>from scipy import linalg , linalg.solve(A,B),解出A,B矩陣的特徵向量  
* sympy - 符號運算
>x,y = symbols('x y') : 建立變數x y  
>diff(x,y) : 對x做y微分
>integrate(x,y,z) 對x做積分，範圍是y~z  
>factor(x) : x做因式分解  
>expand(x) : 將x乘開  
>simplify(x) : 如果x有同類項將其合併  
>solve(x) : 求解x  
>sympy.sqrt(x) :將x開根號
* 其他
>eval() : ()內塞ax+b的表達式 並回傳結果  
>exp() :　指數函數  

