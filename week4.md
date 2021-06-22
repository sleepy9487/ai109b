## 線性規劃  
* [參考資料](https://zh.wikipedia.org/wiki/%E7%BA%BF%E6%80%A7%E8%A7%84%E5%88%92)  
* 線性規劃（Linear Programming，簡稱LP）特指目標函數和約束條件皆為線性的最佳化問題。  
* 具有兩種特性  
  * 可加性 : L(x+t) = L(x) + L (t)  
  * 一次齊次性 : L(mx) = mL(x)  
* 種類  
  * 標準型  
  * 增廣矩陣 - [單純形法](https://zh.wikipedia.org/wiki/%E5%8D%95%E7%BA%AF%E5%BD%A2%E6%B3%95)  
  * 對偶  

## 整數規劃  
  * 要求所有未知數必須為整數
  *  

## 整數規劃 vs 線性規劃
  * 整數規劃較難
  * 單純形法(線性規劃)最差也是用2的n次方在推,目前最快也是n的三次方,但整數規劃目前還沒有可以以2的n次方做解決的方法
## [NP complete](https://zh.wikipedia.org/wiki/NP%E5%AE%8C%E5%85%A8)
  * [bigO](https://zh.wikipedia.org/wiki/%E5%A4%A7O%E7%AC%A6%E5%8F%B7)
    * [泡沫排序法](https://en.wikipedia.org/wiki/Integer_programming)
      >時間複雜度 = n的2次方 
    * [循序搜尋法](http://ms2.ctjh.ntpc.edu.tw/~luti/108bc-al-search.htm)
      >時間複雜度 = n
## 深度優先搜尋
  [image]()
>優先往路徑最短且沒拜訪過的節點移動

## 廣度優先搜尋
  [image]()
>由淺入深的最短路徑拜訪 如圖 1的分支為2.5 2路徑最短先拜訪 然後再去拜訪同一層的5

