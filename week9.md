圖片取自[人工神經網路](https://zh.wikipedia.org/wiki/%E4%BA%BA%E5%B7%A5%E7%A5%9E%E7%BB%8F%E7%BD%91%E7%BB%9C)

## 神經網路
* [人工神經網路](https://zh.wikipedia.org/wiki/%E4%BA%BA%E5%B7%A5%E7%A5%9E%E7%BB%8F%E7%BD%91%E7%BB%9C)
* 電腦模擬人類神經系統所設計的程式,用來模擬人類視覺、聽覺等行為,企圖讓電腦也具有人類智慧的方法,不過人類的神經系統相當複雜(圖),所以設計起來也十分困難,目前無法真正模擬出真正的人類神經。  
![image](https://github.com/sleepy9487/ai109b/blob/main/ai-image/%E4%BA%BA%E9%A1%9E%E7%A5%9E%E7%B6%93%E5%85%83.jpg)
* 但!,我們不需要設計出高基氏體、細胞膜等人類的細胞胞，我們的目的就是設計出類似行為的程式,人類可以透過抽象化將細胞結構簡化成下圖(單一神經元,單一神經網路)。  
![image](https://github.com/sleepy9487/ai109b/blob/main/ai-image/%E7%A5%9E%E7%B6%93%E5%85%83.png)
![image](https://github.com/sleepy9487/ai109b/blob/main/ai-image/%E5%96%AE%E5%B1%A4%E7%A5%9E%E7%B6%93%E5%85%83.png) 

## 梯度下降法
* diff.py
```
def f(x):
    # return x*x
    return x**3

dx = 0.001

def diff(f, x):
    df = f(x+dx)-f(x)
    return df/dx

print('diff(f,2)=', diff(f, 2))

```
* result  
```
diff(f,2)= 12.006000999997823

```
* e.py
```
def e(n):
	return (1+1.0/n)**n

for i in range(100):
	n = (i+1)*100.0
	print('n=', n, 'e(n)=', e(n))

```
* result
```  
n= 100.0 e(n)= 2.7048138294215285
n= 200.0 e(n)= 2.711517122929317  
n= 300.0 e(n)= 2.7137651579427837 
n= 400.0 e(n)= 2.7148917443812293 
n= 500.0 e(n)= 2.715568520651728  
n= 600.0 e(n)= 2.7160200488806514 
 
.
.
.
n= 9700.0 e(n)= 2.718141724076723
n= 9800.0 e(n)= 2.718143153583405
n= 9900.0 e(n)= 2.718144554210053
n= 10000.0 e(n)= 2.7181459268249255
```
## 梯度下降法
* 梯度就是斜率最大的方向,所謂的梯度下降法就是朝斜率最大的地方走
* 梯度下降法讓深度學習就極高的進展  
![image](https://github.com/sleepy9487/ai109b/blob/main/ai-image/%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D%E6%B3%95.jpg)  
* vecGradient.py
```
step = 0.01

# 我們想找函數 f 的最低點
def f(p):
    [x,y] = p
    return x * x + y * y

# df(f, p, k) 為函數 f 在點P對變數 k 的偏微分: df / dp[k]
# 例如在上述 f 範例中 k=0, df/dx, k=1, df/dy
def df(f, p, k):
    p1 = p.copy()
    p1[k] += step
    return (f(p1) - f(p)) / step

# 函數 f 在點 p 上的梯度
def grad(f, p):
    gp = p.copy()
    for k in range(len(p)):
        gp[k] = df(f, p, k)
    return gp

[x,y] = [1,3]
print('x=', x, 'y=', y)
print('df(f(x,y), 0) = ', df(f, [x, y], 0))
print('df(f(x,y), 1) = ', df(f, [x, y], 1))
print('grad(f)=', grad(f, [x,y]))

```
* result
```
x= 1 y= 3
df(f(x,y), 0) =  2.009999999999934
df(f(x,y), 1) =  6.009999999999849
grad(f)= [2.009999999999934, 6.009999999999849]
```
* npGradient.py
```
import numpy as np

step = 0.01

# 我們想找函數 f 的最低點
def f(p):
    [x,y] = p
    # print('x,y=', x, y)
    return x*x + y*y

# # 函數 f 對變數 p[k] 的偏微分: df / dp[k]
def df(f, p, k):
    p1 = p.copy()
    p1[k] = p[k]+step
    return (f(p1) - f(p)) / step

# 函數 f 在點 p 上的梯度
def grad(f, p):
    gp = p.copy()
    for k in range(len(p)):
        gp[k] = df(f, p, k)
    return gp

p = np.array([1.0,3.0])
print('df(f, p, 0) = ', df(f, p, 0))
print('df(f, p, 1) = ', df(f, p, 1))
print('grad(f)=', grad(f, p))

```
* result
``` 
df(f, p, 0) =  2.009999999999934
df(f, p, 1) =  6.009999999999849
grad(f)= [2.01 6.01]
```
* gdTest.py
```
import gd1 as gd

def f(p):
    [x,y] = p
    return x*x + y*y

p = [1.0, 3.0]
gd.gradientDescendent(f, p)

```
* result
```
1:p=[1.0, 3.0] f(p)=10.000 gp=[2.009999999999934, 6.009999999999849] glen=6.33721
2:p=[0.9799 2.9399] f(p)=9.603 gp=[1.9698 5.8898] glen=6.21046
3:p=[0.960202 2.881002] f(p)=9.222 gp=[1.930404 5.772004] glen=6.08625
4:p=[0.94089796 2.82328196] f(p)=8.856 gp=[1.89179592 5.65656392] glen=5.96453 
5:p=[0.92198    2.76671632] f(p)=8.505 gp=[1.85396    5.54343264] glen=5.84524  
.
.
.
660:p=[-0.00499834 -0.00499504] f(p)=0.000 gp=[3.32031998e-06 9.92792193e-06] glen=0.00001
661:p=[-0.00499837 -0.00499514] f(p)=0.000 gp=[3.25391358e-06 9.72936349e-06] glen=0.00001
662:p=[-0.00499841 -0.00499523] f(p)=0.000 gp=[3.18883531e-06 9.53477622e-06] glen=0.00001
663:p=[-0.00499844 -0.00499533] f(p)=0.000 gp=[3.1250586e-06 9.3440807e-06] glen=0.00001
```
* gd1.py
```
import numpy as np
from numpy.linalg import norm

# 函數 f 對變數 k 的偏微分: df / dk
def df(f, p, k, step=0.01):
    p1 = p.copy()
    p1[k] = p[k]+step
    return (f(p1) - f(p)) / step

# 函數 f 在點 p 上的梯度
def grad(f, p, step=0.01):
    gp = p.copy()
    for k in range(len(p)):
        gp[k] = df(f, p, k, step)
    return gp

# 使用梯度下降法尋找函數最低點
def gradientDescendent(f, p0, step=0.01):
    p = p0.copy()
    i = 0
    while (True):
        i += 1
        fp = f(p)
        gp = grad(f, p) # 計算梯度 gp
        glen = norm(gp) # norm = 梯度的長度 (步伐大小)
        print('{:d}:p={:s} f(p)={:.3f} gp={:s} glen={:.5f}'.format(i, str(p), fp, str(gp), glen))
        if glen < 0.00001:  # 如果步伐已經很小了，那麼就停止吧！
            break
        gstep = np.multiply(gp, -1*step) # gstep = 逆梯度方向的一小步
        p +=  gstep # 向 gstep 方向走一小步
    return p # 傳回最低點！

```
* gdNumber.py
```
import gd2 as gd

def f(p):
    [x] = p
    return abs(x*x-4) # 能量函數為 |x^2-4|

p = [1.0]
gd.gradientDescendent(f, p)
```
* result
```
1:p=[1.0, 3.0] f(p)=10.000 gp=[2.009999999999934, 6.009999999999849] glen=6.33721
2:p=[0.9799 2.9399] f(p)=9.603 gp=[1.9698 5.8898] glen=6.21046
3:p=[0.960202 2.881002] f(p)=9.222 gp=[1.930404 5.772004] glen=6.08625
4:p=[0.94089796 2.82328196] f(p)=8.856 gp=[1.89179592 5.65656392] glen=5.96453 
5:p=[0.92198    2.76671632] f(p)=8.505 gp=[1.85396    5.54343264] glen=5.84524 
6:p=[0.9034404  2.71128199] f(p)=8.167 gp=[1.8168808  5.43256399] glen=5.72833
.
.
.
33:p=[1.8889633] f(p)=0.432 gp=[-3.78792659] glen=3.78793
34:p=[1.92684256] f(p)=0.287 gp=[-3.86368512] glen=3.86369
35:p=[1.96547941] f(p)=0.137 gp=[-3.94095882] glen=3.94096
36:p=[2.004889] f(p)=0.020 gp=[4.019778] glen=4.01978
37:p=[1.96469122] f(p)=0.140 gp=[-3.93938244] glen=3.93938
```
* result
```
import numpy as np
import math
import gd3 as gd

def sig(t):
    return 1.0/(1.0+math.exp(-t))

o = [0,0,0,1] # and gate outputs
# o = [0,1,1,1] # or gate outputs
# o = [0,1,1,0] # xor gate outputs
def loss(p, dump=False):
    [w1,w2,b] = p
    o0 = sig(w1*0+w2*0+b)
    o1 = sig(w1*0+w2*1+b)
    o2 = sig(w1*1+w2*0+b)
    o3 = sig(w1*1+w2*1+b)
    delta = np.array([o0-o[0], o1-o[1], o2-o[2], o3-o[3]])
    if dump:
        print('o0={:.3f} o1={:.3f} o2={:.3f} o3={:.3f}'.format(o0,o1,o2,o3))
    return np.linalg.norm(delta, 2)

p = [0.0, 0.0, 0.0] # [w1,w2,b] 
plearn = gd.gradientDescendent(loss, p, max_loops=3000)
loss(plearn, True)

```
* result
``` 
2999:p=[ 1.70833465  1.70833465 -2.7326384 ] f(p)=0.506 gp=[-0.04493286 -0.04493286  0.06420767] glen=0.09034
o0=0.061 o1=0.264 o2=0.264 o3=0.66
```
