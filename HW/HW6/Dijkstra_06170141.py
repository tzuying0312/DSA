from collections import defaultdict  
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

#原理、程式碼
#https://zh.wikipedia.org/wiki/%E6%9C%80%E5%B0%8F%E7%94%9F%E6%88%90%E6%A0%91
#https://zh.wikipedia.org/wiki/%E5%85%8B%E9%B2%81%E6%96%AF%E5%85%8B%E5%B0%94%E6%BC%94%E7%AE%97%E6%B3%95
#https://zh.wikipedia.org/wiki/%E6%88%B4%E5%85%8B%E6%96%AF%E7%89%B9%E6%8B%89%E7%AE%97%E6%B3%95
#https://high-python-ext-3-algorithms.readthedocs.io/ko/latest/chapter9.html
#圖片來源
#https://zh.wikipedia.org/wiki/%E5%85%8B%E9%B2%81%E6%96%AF%E5%85%8B%E5%B0%94%E6%BC%94%E7%AE%97%E6%B3%95#/media/File:Kruskal_Algorithm_6.svg
#https://docs.google.com/presentation/d/e/2PACX-1vTgHO5AkHJS6iN6bnnBMMdHv6E4rabnrC0KwyTRfjad8Ab3IQjbnGvZuQOjDC9t7nKqeroiwcuasJrI/pub?start=false&loop=false&delayms=3000&slide=id.g7b9afdb0e7_0_15
#書籍
#演算法圖鑑