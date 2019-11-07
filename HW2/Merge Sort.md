## Merge Sort 

## 簡介
快速排序使用分治法（Divide and conquer）策略來把一個序列（list）分為較小和較大的2個子序列，然後遞迴地排序兩個子序列。

## 運算流程
分為2個步驟:分割、合併

* 分割
1. 分割方法為:從長度的一半開始切割，分為左與右。
2. 不斷重複(1)，切至長度小於2停止。
3. 此時list中的元素只有1個。

* 合併
1. 合併的同時，比較大小。
2. 假如right元素中有[1,5]、left中有[3]。
3. 開時比較時，為left與right的第一位元素。
4. 有被變動到的list，下一回被比較的元素為第二位。
5. ex:right的1與left的3比較，因此下一位比較為5與3。

## 流程示意圖
![mergesort](https://github.com/tzuying0312/Learning-Code/blob/master/photo/mergesort.png)

## 學習歷程
```python

```


###### 參考資料
[merge sort](https://zh.wikipedia.org/wiki/%E5%BD%92%E5%B9%B6%E6%8E%92%E5%BA%8F#Python)
