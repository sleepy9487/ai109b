## 前言  
* 人工智慧涵蓋機器學習,機器學習涵蓋深度學習  

# [蒙地卡羅法](https://zh.wikipedia.org/wiki/%E8%92%99%E5%9C%B0%E5%8D%A1%E7%BE%85%E6%96%B9%E6%B3%95)  
* 常運用於金融運算、空氣熱力學、動力學等等  
* 粗略分成兩種  
  * 求解問題本身存在的隨機性,藉由電腦運算直接類比這種隨機的過程  
  * 求解問題可以轉化為某種隨機分布的特徵點(圖)  
![蒙地卡羅法](https://github.com/sleepy9487/ai109b/blob/main/ai-image/%E8%92%99%E5%9C%B0%E5%8D%A1%E7%BE%85.png)  
# [黎曼積分](https://zh.wikipedia.org/wiki/%E9%BB%8E%E6%9B%BC%E7%A7%AF%E5%88%86)  
* 黎曼函數
![黎曼積分公式](https://github.com/sleepy9487/ai109b/blob/main/ai-image/%E9%BB%8E%E6%9B%BC%E7%A9%8D%E5%88%86%E5%85%AC%E5%BC%8F.png)  
* 黎曼取出的面積  
![黎曼積分](https://github.com/sleepy9487/ai109b/blob/main/ai-image/%E9%BB%8E%E6%9B%BC%E7%A9%8D%E5%88%86.png)  
>通常會分割成小區塊  
# [馬可夫鏈](https://zh.wikipedia.org/zh-tw/%E9%A9%AC%E5%B0%94%E5%8F%AF%E5%A4%AB%E9%93%BE)  
* 討論不是互相獨立的一些事件。
* 下一狀態的機率分布只能由當前狀態決定，在時間序列中它前面的事件均與之無關。
* 具有狀態的隨機過程(馬可夫隨機系統)
![馬可夫](https://github.com/sleepy9487/ai109b/blob/main/ai-image/%E9%A6%AC%E5%8F%AF%E5%A4%AB.png)
# [吉布斯採樣](https://zh.wikipedia.org/wiki/%E5%90%89%E5%B8%83%E6%96%AF%E9%87%87%E6%A0%B7)  
* 吉布斯採樣是統計學中用於馬爾科夫蒙特卡洛的一種算法，用於在難以直接採樣時從某一多變量概率分布中近似抽取樣本序列。該序列可用於近似聯合分布、部分變量的邊緣分布或計算積分（如某一變量的期望值）。某些變量可能為已知變量，故對這些變量並不需要採樣。  
* 演算法  
  * 確定初始值  
  * 不斷取初始值演算的下一個值直到收斂為止  
 ![吉布斯](https://github.com/sleepy9487/ai109b/blob/main/ai-image/%E5%90%89%E5%B8%83%E6%96%AF.png)  
# [隱藏式馬可夫模型](https://zh.wikipedia.org/zh-tw/%E9%9A%90%E9%A9%AC%E5%B0%94%E5%8F%AF%E5%A4%AB%E6%A8%A1%E5%9E%8B)
* 隱藏式馬可夫模型（Hidden Markov Model；縮寫：HMM）或稱作隱性馬可夫模型，是統計模型，它用來描述一個含有隱含未知參數的馬可夫過程。其難點是從可觀察的參數中確定該過程的隱含參數。然後利用這些參數來作進一步的分析。
* 沒辦法直接觀察他的狀態,但可以觀察狀態反映出來的現象,去猜測原本的馬可夫模型機率原本是多少
* ex : 鄉村診所生病,透過詢問病人感覺做診斷
![隱藏馬可夫](https://github.com/sleepy9487/ai109b/blob/main/ai-image/%E9%9A%B1%E8%97%8F%E9%A6%AC%E5%8F%AF%E5%A4%AB.png)
# [維特比演算法](https://zh.wikipedia.org/wiki/%E7%BB%B4%E7%89%B9%E6%AF%94%E7%AE%97%E6%B3%95)
* 原本是通訊領域發展出來的
* 維特比演算法是一種動態規劃演算法。它用於尋找最有可能產生觀測事件序列的維特比路徑——隱含狀態序列，特別是在馬可夫資訊源上下文和隱藏式馬可夫模型中。
![維特比](https://github.com/sleepy9487/ai109b/blob/main/ai-image/%E7%B6%AD%E7%89%B9%E6%AF%94.png)

# [EM演算法](https://programmermedia.org/root/%E9%99%B3%E9%8D%BE%E8%AA%A0/%E8%AA%B2%E7%A8%8B/%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7/06-learn/05-em/em.md)
* 上述 EM 演算法問題的背後，其實是一種「最大概似估計」，只是加入了「隱變數」的概念，這種「最大概似估計」企圖最大化下列算式中的θ值。
* 這個範例探討的是兩個「不公正的銅板」 A 與 B，兩者正面的機率分別是  與  ，當我們用這兩的銅板進行一系列的抽樣時，得到了下列的結果。
![EM演算法1](https://github.com/sleepy9487/ai109b/blob/main/ai-image/EM1.png)
![EM演算法2](https://github.com/sleepy9487/ai109b/blob/main/ai-image/EM2.png)
* θA和θB之初值可隨便設，雖不知實驗時是A還是B但可算出期望值。
   ex: 第一次的期望值  
![EM演算法3](https://github.com/sleepy9487/ai109b/blob/main/ai-image/EM3.png)
* 再利用此機率去計算銅板正面及反面的期望值。
    * ex: P(A) (#H, #T) = 0.45 (5H, 5T) = (2.25 H, 2.25T) ~ (2.2H, 2.2T) 
* 將H和T加總可求出新的θA和θB
![EM演算法4](https://github.com/sleepy9487/ai109b/blob/main/ai-image/EM4.png) 
* 按照循環可找出最後的結果
# [K-近鄰演算法](https://zh.wikipedia.org/wiki/K-%E8%BF%91%E9%82%BB%E7%AE%97%E6%B3%95)
* 在圖型識別領域中，最近鄰居法（KNN演算法，又譯K-近鄰演算法）是一種用於分類和迴歸的無母數統計方法。在這兩種情況下，輸入包含特徵空間（Feature Space）中的k個最接近的訓練樣本。
![K-近鄰](https://github.com/sleepy9487/ai109b/blob/main/ai-image/K-%E8%BF%91%E9%84%B0.png)
# [決策樹](https://medium.com/jameslearningnote/%E8%B3%87%E6%96%99%E5%88%86%E6%9E%90-%E6%A9%9F%E5%99%A8%E5%AD%B8%E7%BF%92-%E7%AC%AC3-5%E8%AC%9B-%E6%B1%BA%E7%AD%96%E6%A8%B9-decision-tree-%E4%BB%A5%E5%8F%8A%E9%9A%A8%E6%A9%9F%E6%A3%AE%E6%9E%97-random-forest-%E4%BB%8B%E7%B4%B9-7079b0ddfbda)
* [決策樹2](https://zh.wikipedia.org/wiki/%E5%86%B3%E7%AD%96%E6%A0%91)
* 決策論中 （如風險管理），決策樹（Decision tree）由一個決策圖和可能的結果（包括資源成本和風險）組成， 用來創建到達目標的規劃。決策樹建立並用來輔助決策，是一種特殊的樹結構。決策樹是一個利用像樹一樣的圖形或決策模型的決策支持工具，包括隨機事件結果，資源代價和實用性。
![決策樹](https://github.com/sleepy9487/ai109b/blob/main/ai-image/%E6%B1%BA%E7%AD%96%E6%A8%B9.png)
# sklearn
```
pip install sklearn
```
