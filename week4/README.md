## Insertion Sort (插入排序法)

###### 簡介
Insertion Sort是一種簡單容易理解的排序演算法，概念是利用另一個數列來存放已排序部分，逐一取出未排序數列中元素，從已排序數列由後往前找到適當的位置插入。

###### 運算流程
1.將資料分成已排序、未排序兩部份
2.依序由未排序中的第一筆(正處理的值)，插入到已排序中的適當位置
3.插入時由右而左比較，直到遇到一個比處理值小的值，再插入
4.若遇到的值比處理的值大或相等，則將值往右移

###### 流程流程示意圖
![GITHUB](https://github.com/tzuying0312/Learning-Code/blob/master/photo/insertion%20sort.gif)

###### 時間複雜度
Best Case：Ο(1)
當資料的順序恰好為由小到大時，每回合只需比較1次
Worst Case：Ο(n2)
當資料的順序恰好為由大到小時，第i回合需比i次
Average Case：Ο(n2)
第n筆資料，平均比較n/2次

###### python程式碼
```python
def insert_sort(lst):
    n=len(lst)
    if n==1: return lst
    for i in range(1,n):
        for j in range(i,0,-1):
            if lst[j]<lst[j-1]: 
                lst[j],lst[j-1]=lst[j-1],lst[j]
            else:
                break
    return lst
```
