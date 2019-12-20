## 何謂圖形?
機算機科學或離散數學所用的圖形與圓餅圖、長條圖不一樣。
- 離散數學中的圖形
>畫成圓形的地方稱為**頂點(節點)**。
>連接頂點和頂點的線稱為**邊**。
- 圖形可用來表現各種事物
- 有向圖
- 圖形的好處
>找出行經各編的最小合計權重。
>找出最短路徑。
## BFS
廣度優先搜尋演算法(Breadth-First-Search,BFS)
- 圖形搜尋演算法。
- 流程
>1.假設自己在某個頂點(起點)。
>2.從起點經由邊搜尋頂點。
>3.直到找到指定的頂點(目標頂點)。
- **廣度優先搜尋在搜尋頂點時，優先搜尋離起點較近的頂點**
- 頂點選項是用**先進先出(FIFO)** 的方式管理。
- 流程圖
![](https://i.imgur.com/jY39H3L.jpg)
>設立G為起點位置。
>首先G能走到F位置，因此將F放入第一個List。
>再來換F，先確認F能走到的位置為E、B，將它們放入第一個List，而F放入第二個，並將第一個List中的F刪除。
>直到所有點皆進入到第二個List。
>**放入到第一個List前，需先確認是否已經存在在List1或List2。**
```python
def BFS(self, s):
    q1 = [] #建立list，為最終的
    q2 = [] #建立list，為流程圖中的first list
    q2.append(s)#將起始點放入first list
    while q2: #若有東西
        node = q2.pop(0) #把第一位取出
        if node not in q1: #確認最終的list是否已經包含在內
            q1.append(node)#沒有則放入到最終的
            nodes = self.graph[node]#找出s對應的其他頂點
            for i in nodes:#將這些點一一放入q2
                q2.append(i)
    return q1

```
```python
def BFS(self, s):
    q1=[]
    q1.append(s)
    q2=[]
    q2.append(s)

    if len(q1)>0:
        vertex = q1.pop(0)
        nodes = self.graph[vertex]
        for i in nodes:
            if i not in q2:
                q1.append(i)
                q2.append(i)
        return q2
```
>使用if最結果為[2, 0, 3]，因為只跑一次。2對應到0和3就將它們append進去，完成。
## DFS
深度優先搜尋演算法(Depth-First-Search,DFS)
- 圖形搜尋演算法。
- 目的從起點抵達指定頂點(目標頂點)。
- 流程
>1.選擇起點。
>2.探查單一路徑，直到無法繼續前進。
>3.折返找下一個選項的路徑。
- 頂點選項是用**後進先出(LIFO)** 的方式管理。
- 流程圖
![](https://i.imgur.com/Ch0Tvp2.jpg)
>設立2為起點。
>指向0，接者0成為頂點，繼續往下走，直到無法連接。
>0指向1，1無法繼續延伸，返回0。
>0指向2，但2已經連接過，因此再返回2。
>2指向3，完成。
```python
def DFS(self, s):
    stack=[] 
    stack.append(s)
    q2=[]#最終的list
    while (len(stack)>0): #有東西
        node=stack.pop() #刪除第一個list
        q2.append(node) #加入至最終的list
        nodes = self.graph[node]#找出s對應的其他頂點
        for i in nodes:
            if i not in q2:#確認是否還未存進至
                stack.append(i) 

    return q2
```
```python
def lenx(self,stack):
    return len(stack)
def DFS(self, s):
    stack=[]
    stack.append(s)
    q2=[]
    x=self.lenx(stack)
    while (x>0):
        node=stack.pop()
        q2.append(node)
        nodes = self.graph[node]
        for i in nodes:
            if i not in q2:
                stack.append(i) 

    return q2
```
>結果為pop from empty list。因為已將len(stack)固定住，無法再變動，因此list中無東西可刪除。

## BFS VS DFS 
- 頂點選項
> BFS採用**先進先出**的方式管理，可以用**queue**的資料結構。
> DFS採用**後進先出**的方式管理，可以用**stack**的資料結構。
- 搜尋順序
> BFS，優先搜尋最早被加入選項的頂點(先從距離起點較近的頂點開始搜尋)。
> DFS，優先搜尋具有深入單一路徑往下探查的特徵。

## 參考資料
演算法圖鑑(包含原理、流程、比較)
[BFS與DFS概念]https://www.youtube.com/watch?v=oLtvUWpAnTQ
[BFS與DFS程式碼解說]https://www.youtube.com/watch?v=bD8RT0ub--0
