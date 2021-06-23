## 反傳遞演算法
* 反傳遞演算法套用在 梯度下降法+微積分的鏈鎖規則
* [Hacker's guide to Neural Networks](http://karpathy.github.io/neuralnets/)
  * Karpathy (特斯拉的技術總監)  
  * 先假設f(x,y)=xy
  * 將x和y偏微分,兩個合起來的向量就是梯度
  * 把f(x)偏微分最後剩下常數y ->梯度下降法最後取得的答案
![xyz圖](https://github.com/sleepy9487/ai109b/blob/main/ai-image/xyz%E5%9C%96.png)
![公式1](https://github.com/sleepy9487/ai109b/blob/main/ai-image/%E5%85%AC%E5%BC%8F1.JPG)
![公式2](https://github.com/sleepy9487/ai109b/blob/main/ai-image/%E5%85%AC%E5%BC%8F2.JPG)
>f(q,z)=qz被偏微分取得q,z  
>f(x,y)=x+y被偏微分取得1
>之後就取得下圖了
![公式3](https://github.com/sleepy9487/ai109b/blob/main/ai-image/%E5%85%AC%E5%BC%8F3.JPG)  
>下圖的1 是偏微分的f/f=1 然後開始做回推
>對q微分會取得z 對z微分會取得q 所以上下-4,3對調
>1 乘回去 -4 所以梯度得到-4 -4 3
* 更複雜的案例  
![更複雜的案例](https://github.com/sleepy9487/ai109b/blob/main/ai-image/%E6%9B%B4%E8%A4%87%E9%9B%9C%E7%9A%84%E6%A1%88%E4%BE%8B.png)  
![更複雜的案例-解](https://github.com/sleepy9487/ai109b/blob/main/ai-image/%E6%9B%B4%E8%A4%87%E9%9B%9C%E7%9A%84%E6%A1%88%E4%BE%8B.png)  

## Pytorch  
* 由Facebook釋出
* 跟google的tensorflow競爭
* ten工業用居多,pytorch則是學術界
* 擁有現成的框架做梯度下降法、自動求微分
# 實作  
* 安裝 : pip install torch
* x.norm: x函數中的變數值相加平方開根號
* torch.tensor: 單一數據類型元素的多维矩陣
* x.grad: 該節點的梯度
* f.backward: 求出函式f的反傳遞
* x.item(): 從張量x中找出元素值

