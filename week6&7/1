## Heap Sort 

## 簡介
用堆積資料結構設計的一種演算法。堆積是一個近似完全二元樹的結構，並同時滿足堆積的性質：子節點的鍵值或索引總是小於（或者大於）它的父節點。

## 運算流程
1. 將list中的直，按照樹的排列方式，依序放進。
2. 父節點與左右兩的子節點做比較。
3. 完成第一輪時，將最上面的root(為list中最大或最小的值)取出，並放置新的list。
4. 直到原始list的長度小於0。

## 流程示意圖
![heapsort](https://github.com/tzuying0312/Learning-Code/blob/master/photo/heapsort.png)

## Merge Sort 

## 簡介
Merge Sort屬於Divide and Conquer演算法，把問題先拆解(divide)成子問題，並在逐一處理子問題後，將子問題的結果合併(conquer)。

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

## 比較
![heapsort vs heapsort](https://github.com/tzuying0312/Learning-Code/blob/master/photo/mergevsheap.jpg)

由上圖可以知道，其實整體的時間是一樣的。兩者差異在於排序方式。
* heap使用堆積方法，要將n個元素儲存到堆積中，每回合取出最大或最小值，再重新排列堆積。
* merge先分割再合併，數的分割不需耗費執行時間，合併時只需反覆比較第一個數。



參考資料:
[圖片來源](https://tingtseng.pixnet.net/blog/post/39924871-algorithm-time-complexity-%E6%BC%94%E7%AE%97%E6%B3%95%E6%99%82%E9%96%93%E8%A4%87%E9%9B%9C%E5%BA%A6%E6%95%B4%E7%90%86)、演算法圖鑑

###### 參考資料:
[heap sort 維基百科](https://zh.wikipedia.org/wiki/%E5%A0%86%E6%8E%92%E5%BA%8F)
[merge sort 維基百科](https://zh.wikipedia.org/wiki/%E5%BD%92%E5%B9%B6%E6%8E%92%E5%BA%8F#Python)
[merge sort 內容介紹](http://alrightchiu.github.io/SecondRound/comparison-sort-merge-sorthe-bing-pai-xu-fa.html)

