## Dijkstra
* 使用了廣度優先搜尋(BFS)解決賦權有向圖的單源最短路徑問題。
* 用以解決最短路徑的演算法
>最短路徑問題是賦予邊權重的**加權圖形**裡，指定**起點**和**終點**，求出從起點到終點之間，邊權重總和最小的路徑。
* 圖中的頂點表示城市，而邊上的權重表示城市間開車行經的距離，該演算法可以用來找到兩個城市之間的最短路徑。
> ex:
> ![](https://i.imgur.com/kAMusO7.gif)
* 時間複雜度為O(V+E)。
>其中E和V分別是圖的邊集和點集。

## 流程
1. 設定各頂點的權重初始值。假設起點為0，其他的頂點設為無限大。
2. 從起點開始。
>下圖，假設起點0。
3. 搜尋連接目前頂點且尚未被檢視的頂點。
>下圖，連接頂點的為1、7。
4. 計算各選項頂點的權重。
> * 計算方法**目前位置的頂點權重+從該頂點到選項頂點的權重。**
> * 下圖，0到1的距離為4、0到7的距離為8。
5. 選擇較小的值
>下圖，選擇1。
6. 計算所得的結果比現況值小時，權重更新。
>* 下圖，當有0、1、7時，可以走到8，且距離為15。
>* 但當等到有2加入時，可以透過0-1-2走到8，且距離為14。
>* 因此更新。

## 流程圖
>範例題目
>
![](https://i.imgur.com/Yo87tCX.jpg)

>解題流程

![](https://i.imgur.com/M5NN57F.jpg)

## Kruskal
* Kruskal演算法是一種用來尋找最小生成樹的演算法。
>最小生成樹是一副連通加權無向圖中一棵權值最小的生成樹。
* 平均時間複雜度為O(V+E)。
>其中E和V分別是圖的邊集和點集。
* 在無向圖有權重的連通圖中找尋以下
>這些邊的權重和最小。

>可以連通所有點且不形成循環。

## 流程
1. 先計算各點之間的權重。
>* A-B:7
>* A-D:5
>* B-C:8
>* B-D:9
>* B-E:7
>* C-E:5
>* D-E:15
>* D-F:6
>* E-F:8
>* E-G:9
>* F-G:11
2. 由大到小排序好。
>* A-D:5
>* C-E:5
>* D-F:6
>* A-B:7
>* B-E:7
>* B-C:8
>* E-F:8
>* B-D:9
>* E-G:9
>* F-G:11
>* D-E:15
3. 由最小的邊出發。
>A-D:5或C-E:5，擇1。
4. 依序大小找出最小不形成循環的邊。
5. 直到邊的個數為點的個數少1。
## 流程圖
>* A-D:5，將A-D連接起來。
>* C-E:5，將C-E連接起來。
>* D-F:6，將D-F連接起來。
>* A-B:7，將A-B連接起來。
>* B-E:7，將B-E連接起來。
>* B-C:8，BC連接會導致BCE循環，跳過。
>* E-F:8，EF連接會導致BFABE循環，跳過。
>* B-D:9，BD連接會導致ABD循環，跳過。
>* E-G:9，將E-G連接起來。
>* F-G:11，FG連接會導致FDABEG循環，跳過。
>* D-E:15，DE連接會導致DABE循環，跳過。

![](https://i.imgur.com/X657D9t.png)

## 程式碼
```python
from collections import defaultdict 

#Class to represent a graph 
class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 

    def Dijkstra(self, s): 
        dist = [float("inf")] * self.V #s至各點的距離(先設無窮大)
        dist[s] = 0 #s與自己的距離為0
        done = [False] * self.V #設立一個list，當該點被走過就會變True
        
        for i in range(self.V):
            u = self.findmindist(dist,done) #尋找距離最小的點
            done[u] = True #找到該點，因此改成true
            
            for v in range(self.V): #去看前面的點是否有更短的              
                if self.graph[u][v] > 0 and done[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
                   
        y=self.todict(dist)
        return y
    
    def findmindist(self,dist,done):
        min_dist = float("inf") #先假設距離為無窮大
        for v in range(self.V): 
            if dist[v] < min_dist and done[v] == False: #若該點還未被走過
                min_dist = dist[v] #當for回圈跑完，及距離最短
                min_index = v #找到該點
        return min_index    
    
    def todict (self,dist):
        dictionary = {} #新增字典
        j = 0 
        x = len(dist)
        for i in range(x):
            x = str(i)
            dictionary[x] = dist[j]
            j += 1
        return dictionary
```
## 參考資料

原理、程式碼、概念
https://zh.wikipedia.org/wiki/%E6%9C%80%E5%B0%8F%E7%94%9F%E6%88%90%E6%A0%91
https://zh.wikipedia.org/wiki/%E5%85%8B%E9%B2%81%E6%96%AF%E5%85%8B%E5%B0%94%E6%BC%94%E7%AE%97%E6%B3%95
https://zh.wikipedia.org/wiki/%E6%88%B4%E5%85%8B%E6%96%AF%E7%89%B9%E6%8B%89%E7%AE%97%E6%B3%95
https://high-python-ext-3-algorithms.readthedocs.io/ko/latest/chapter9.html

圖片來源
https://zh.wikipedia.org/wiki/%E5%85%8B%E9%B2%81%E6%96%AF%E5%85%8B%E5%B0%94%E6%BC%94%E7%AE%97%E6%B3%95#/media/File:Kruskal_Algorithm_6.svg
https://docs.google.com/presentation/d/e/2PACX-1vTgHO5AkHJS6iN6bnnBMMdHv6E4rabnrC0KwyTRfjad8Ab3IQjbnGvZuQOjDC9t7nKqeroiwcuasJrI/pub?start=false&loop=false&delayms=3000&slide=id.g7b9afdb0e7_0_15

書籍
演算法圖鑑
