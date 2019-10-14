## Quick Sort 

## 簡介
快速排序使用分治法（Divide and conquer）策略來把一個序列（list）分為較小和較大的2個子序列，然後遞迴地排序兩個子序列。

## 運算流程
1.挑選基準值：從數列中挑出一個元素，稱為「基準」（pivot）

2.分割：重新排序數列，所有比基準值小的元素擺放在基準前面，所有比基準值大的元素擺在基準後面（與基準值相等的數可以到任何一邊。在這個分割結束之後，對基準值的排序就已經完成

3.遞迴排序子序列：遞迴地將小於基準值元素的子序列和大於基準值元素的子序列排序。

## 流程流程示意圖
![GITHUB](https://github.com/tzuying0312/Learning-Code/blob/master/photo/insertion%20sort.gif)

## 時間複雜度
Best Case：Ο(1)
當資料的順序恰好為由小到大時，每回合只需比較1次

Worst Case：Ο(n2)
當資料的順序恰好為由大到小時，第i回合需比i次

Average Case：Ο(n2)
第n筆資料，平均比較n/2次

## python程式碼
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

