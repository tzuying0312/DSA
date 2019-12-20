from collections import defaultdict 
  

class Graph:
    def __init__(self): 
        self.graph = defaultdict(list) 

    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
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
      
#演算法圖鑑(包含原理、流程、比較)
#[BFS與DFS概念]https://www.youtube.com/watch?v=oLtvUWpAnTQ
#[BFS與DFS程式碼解說]https://www.youtube.com/watch?v=bD8RT0ub--0
 
