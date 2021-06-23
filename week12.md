教材 [語言理論](https://programmermedia.org/root/%E9%99%B3%E9%8D%BE%E8%AA%A0/%E8%AA%B2%E7%A8%8B/%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7/10-lang/rule/01-basic/)
## 自然語言與人造語言
* 自然語言為歷史衍生出來的語言,沒有人刻意去創造,僅由人們溝通而創造,被稱作自然語言  
* 某些語言是被人們刻意去創造的"人造語言",比如C、Ruby、Python
* 電腦對於語言文字的處理方式,在程式語言上面已經非常成熟,編譯器很容易把高階語言程式轉換成組合語言或機器瑪。
* 但是電腦對自然語言非常力不從心，儘管從2015年開始深度學習RNN與LSTM循環神經網路,但離人類自己翻譯的程度還有一大差距!  
* 電腦可以將指令串進行解譯執行,作為電腦語言的語意,但自然語言的語意式甚麼?要如何翻譯成指令動作?
## 語言的層次
* 無倫何種語言,都可以分成"詞彙,語句,文章"三個層次
* 語言處理可分為以下幾個層次
1. 詞彙掃描: 詞彙層次
2. 語法解析: 語句層次
3. 語意解析: 文章層次
4. 語言合成: 回應階段，將詞彙組成語句、再將語句組合成文章呈現出來  
  * 一個翻譯系統需要具備上面四種以上功能
## Chomsky Hierarchy (喬姆斯基語言階層）
![image](https://github.com/sleepy9487/ai109b/blob/main/ai-image/Chomsky%20Hierarchy%20(%E5%96%AC%E5%A7%86%E6%96%AF%E5%9F%BA%E8%AA%9E%E8%A8%80%E9%9A%8E%E5%B1%A4%EF%BC%89.png)
* 他們的關係是Type3 ⊂ Type2 ⊂ Type1 ⊂Type0  
* Type1 語言的語法有點限制，因為每個規則的左邊至少要有一個非終端項目 A，但其前後可以連接任意規則，這種語法所能描述的語言稱為「對上下文敏感的語言」 (Context-Sensitive)，因為 可以決定之後到底是否要接 ，所以前後文之間是有關係的，因此才叫做「對上下文敏感的語言」。這種語言在計算理論上可以對應到「線性有界的非決定性圖靈機」，也就是一台「記憶體有限的電腦」  
* Type2 語言的語法限制更大，因為規則左邊只能有一個非終端項目 (以 A 代表)，規則右邊則沒有限制這種語言被稱為「上下文無關的語言」(Context Free) ，在計算理論上可以對應到 「非決定性的堆疊機」(non-deterministic pushdown automaton)。  
* Type3 的語法限制是最多的，其規則的左右兩邊都最多只能有一個非終端項目 (以 A, B 表示) ，而且右端的終端項目 (以 a 表示) 只能放在非終端項目 B 的前面。這種語言稱為「正規式」(Regular)，可以用程式設計中常用的「正規表達式」(Regular Expression) 表示，對應到計算理論中的有限狀態機(Finite State Automaton)  
![image](https://github.com/sleepy9487/ai109b/blob/main/ai-image/Chomsky%20hierarchy.JPG)
* 大多數程式語言為Type2類型,以下是一個Type2所不能處理的經典範例  
![image](https://github.com/sleepy9487/ai109b/blob/main/ai-image/Type1%E5%8F%AF%E4%BB%A52%E4%B8%8D%E8%A1%8C.JPG)
## BNF與生成語法
* 語法  
![image](https://github.com/sleepy9487/ai109b/blob/main/ai-image/BNF%E7%94%9F%E6%88%90%E8%AA%9E%E6%B3%95.JPG)  
* 語法範例  
![image](https://github.com/sleepy9487/ai109b/blob/main/ai-image/BNF%E7%AF%84%E4%BE%8B.JPG)
* 語法的剖析 
![image](https://github.com/sleepy9487/ai109b/blob/main/ai-image/%E8%AA%9E%E8%A8%80%E5%89%96%E6%9E%90%E7%AF%84%E4%BE%8B.JPG)
