## Heap Sort 

## 簡介
用堆積資料結構設計的一種演算法。堆積是一個近似完全二元樹的結構，並同時滿足堆積的性質：即子節點的鍵值或索引總是小於（或者大於）它的父節點。

## 運算流程
1. 將list中的直，按照樹的排列方式，依序放進。
2. 父節點與左右兩的子節點做比較。
3. 完成第一輪時，將最上面的root(為list中最大或最小的值)取出，並放置新的list。
4. 直到原始list的長度小於0。

## 流程示意圖
![heapsort](https://github.com/tzuying0312/Learning-Code/blob/master/photo/heapsort.png)

## 學習歷程
    在上課演練流程時，就有想法:需要有個list(給排列好的第一位元素append至此)，需要有兩個位置互換的程式碼(因為比較大小)。
```python
def hs(list):
    i=0
    while i<len(list)/2:
        left=2*i+1
        right=2*i+2
        root=list[i]
        if root>left:
            list[i],list[2*i+1]=list[2*i+1],list[i]
            if root>right:
                list[i],list[2*i+2]=list[2*i+2],list[i]
        i+=1
        return list
```
    簡單的寫一個，卻鄧是否可以交換成功。
    
```python
def hs(list):
    i=0
    while i <len(list)//2 and len(list)>2:

        left=2*i+1
        right=2*i+2
        root=list[i]
        if root>list[left]:
            list[i],list[2*i+1]=list[2*i+1],list[i]
            root=list[i]
            if root>list[right]:
                list[i],list[2*i+2]=list[2*i+2],list[i]
        i+=1
        return done(list)
    if list[0]>list[1]:
        list[0],list[1]=list[1],list[0]
        print(list)
    
def done(list):
    print(list)
    a=[]
    a.append(list.pop(0))
    list.insert(0,list.pop(-1))
    print(list)
    print(a)
    return hs(list)
```
    在這裡有許多print，是為了給自己確認每次mylist、a的變化。同時，在這邊發現了一個問題:a=[]若放置在done(list)中，會導致從hs(list)下來時a=[]不斷重新變成空list。因此應該放置在外面。
    
```python
def hs(mylist):
    i=0
    a=[]
    while i <len(mylist)//2 and len(mylist)>2:

        left=2*i+1
        right=2*i+2
        root=mylist[i]
        if root>mylist[left]:
            mylist[i],mylist[2*i+1]=mylist[2*i+1],mylist[i]
            root=mylist[i]
            if root>mylist[right]:
                mylist[i],mylist[2*i+2]=mylist[2*i+2],mylist[i]
        i+=1
        a.append(mylist.pop(0))
        mylist.insert(0,mylist.pop(-1))

        
        
    if mylist[0]>mylist[1]:
        mylist[0],mylist[1]=mylist[1],mylist[0]

        
    done=[]
    done=a+mylist
    print(done)
```
    在這裡由於自己的測試成功，原本以為對了，結果新的測試值錯誤。
    在這我才發現一個大錯誤，應該從後面開始比較，因為當元素往下比較時，上面的順序不會在跟者變動。
    由於這樣太長又不清楚，於是決定將排列完一次(也就是說，最小值已經在第一位)丟進done(mylist)。
 
```python
def heap_sort(mylist):
    for i in range(len(mylist),-1,-1):
        root=mylist[i-1]
        left=2*i+1
        right=2*i+2
        if left<len(mylist):
            if root>mylist[left]: 
                mylist[i],mylist[2*i+1]=mylist[2*i+1],mylist[i]
        if right<len(mylist):
            if root>mylist[right]:
                mylist[i],mylist[2*i+2]=mylist[2*i+2],mylist[i]
    done(mylist)
    
ok=[]

def done (mylist):
    
    ok.append(mylist[0])
    mylist[0]=mylist[-1]
    mylist.pop(-1)
    if len(mylist)>0:
        mylist=heap_sort(mylist)
    print(ok) 
```
    在此與上面一樣沒跑出錯誤，但結果是錯的，原因為root不該先被定義為哪個元素的值，應在比較大小時出現。
    補充:這邊不能寫mylist.insert(0,mylist.pop(-1))，由於當剩餘最後一值是會產生錯誤。
    原本想要try，但一樣產生錯誤，應再理解。
    

###### 
[heap sort 維基百科](https://zh.wikipedia.org/wiki/%E5%A0%86%E6%8E%92%E5%BA%8F)

