## 遺傳演算法  
* 演算法保存良好基因,藉由公式不斷改進  
>良好基因(父)+良好基因(母)=更好的個體  
在電腦裡基因都是0與1,我們扮演上帝的角色  
讓好基因與壞基因機率差兩倍-挑選好基因  
原理 : 取父母數列前後各半段組成新生代,繼續重複繁殖,加入機率讓新生兒有機會突變  

* keyGa.py
```
from geneticAlgorithm import GeneticAlgorithm
import random

class KeyGA(GeneticAlgorithm):
    def __init__(self, key):
        super().__init__()
        self.key = key

    def randomChromosome(self): # 隨機產生一個染色體 (一個 16 位元的 01 字串)
        bits=[]
        for _ in range(len(self.key)):
            bit = str(random.randint(0,1))
            bits.append(bit)
        return ''.join(bits)
  
    def calcFitness(self, c): # 分數是和 key 一致的位元個數
        fitness=0
        for i in range(len(self.key)):
            fitness += 1 if c[i]==self.key[i] else 0
        return fitness
  
    def crossover(self, c1, c2):
        cutIdx = random.randint(0, len(c1)-1)
        head   = c1[0:cutIdx]
        tail   = c2[cutIdx:]
        return head + tail
    
    def mutate(self, chromosome): # 突變運算
        i=random.randint(0, len(chromosome)-1) # 選擇突變點
        cMutate = chromosome[0:i]+random.choice(['0','1'])+chromosome[i+1:] # 在突變點上隨機選取 0 或 1
        return cMutate # 傳回突變後的染色體

# 執行遺傳演算法，企圖找到 key，最多執行一百代，每代族群都是一百人
kga = KeyGA("1010101010101010")
kga.run(100, 20)
```
>fitness key,跟key相符合的越多,基因越優良。  
>遺傳演算法的其中一個重點在於如果一開始的基因就是劣的，那無論如何都不會組成良好的新生代。  

## 凱薩密碼  
凱薩大帝當年與其將領溝通用的加密方法,取用於字母+相同位移量  
比如attackatdawn 取位移量1 = bubdlbuebxo  

## 維吉尼亞密碼--多位移量版本的凱薩密碼  
把單位移量1改 024循環  
attackatdawn  
```
a + 0 = a  
t + 2 = v  
t + 4 = x  
a + 0 = a  
c + 2 = e  
k + 4 = m  
a + 0 = a  
t + 2 = v  
d + 4 = h  
w + 0 = w  
n + 2 = p  
```
##  XOR加密
用XOR加密且解密,利用邏輯閘相同位元輸出1,不同位元輸出1,相同位元輸出0的特性  
讓位元做兩次XOR還是能輸出成原本的樣貌  
> X xor k xor k
> k xor k = 0  
> 輸出 x