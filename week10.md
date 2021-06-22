## 笛摩根定律
* 1. -(x｜ y) = -x & -y
* 2. -(x & y) = -x｜-y
## 謂詞函數
* 布林邏輯只有代表真假值的簡單變數
  * P & (P=>Q) => Q.
* 命題邏輯沒有函數的概念,只有簡單的命題,故被稱作命題邏輯
* 而在謂詞邏輯裏，則有「布林函數」的概念，因此其表達能力較強，例如以下是一些謂詞邏輯的範例。  
  * Parent(x,y) <= Father(x,y). ->如果x是y的父親,x就是y的家人

## 一階邏輯
* 加上 (對於所有)∀或∃(存在) 這兩個變數限定符號，而其中的謂詞不可以是變項，而必須要是常項，這種邏輯就稱為一階邏輯。  
  *∀People(x) => Mortal(x);人都會死
  *people(Socrates);蘇格拉底是人
  *Mortal(Socrates);所以蘇格拉底會死

## 二階邏輯
* 一階邏輯中的謂詞，放寬成可以是變項的話 (這些變項可以加上 ∀\forall∀ 與 ∃\exists∃ 等符號的約束)，那就變成了二階邏輯
  * ∃P(P(x)∧P(y)).
  * ∀P∀x(x∈P∣x∈/P).
  * ∀P(P(0)∧∀y(P(y)=>P(succ(y)))=>∀yP(y)). ->數學歸納法規則

##Prolog
* 安裝 : choco install swi-prolog
* 進入系統 : swipl
* 輸出hello world
```
[1] 1 ?- write("hello world ").
hello world 
true.
```
* 檔案執行 : [檔案名稱]. 例如[gcd].  
  * 回傳檔案的判斷式 : 例如 gcd(36,63,N).  
* 退出系統 : halt.  
* 所有語句句尾都要加 .   
* nl可以換行  

## 集合與悖論
[數學危機](https://gitlab.com/ccc109/ai/-/blob/master/04-logic/%E9%9B%86%E5%90%88%E8%88%87%E6%82%96%E8%AB%96.md)  
