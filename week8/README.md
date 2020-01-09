## BST
二元搜尋樹（Binary Search Tree），是一棵空樹或具有下列性質的二元樹：

* 若任意節點的左子樹不空，則左子樹上所有節點的值均小於它的根節點的值。

* 若任意節點的右子樹不空，則右子樹上所有節點的值均大於它的根節點的值。

* 任意節點的左、右子樹也分別為二元搜尋樹。

BST的優勢在於相比於其他資料結構的優勢在於尋找、插入的時間複雜度較低。為 O(log n)。二元搜尋樹是基礎性資料結構，用於構建更為抽象的資料結構，如集合、多重集、關聯陣列等。

以下圖為例:
node = 30，左邊的子節點15(node.left)會小於30，右邊的子節點60(node.right)會大於30。

![BST](https://github.com/tzuying0312/Learning-Code/blob/master/photo/binary-search-tree.png)

## 流程圖
![BST](https://github.com/tzuying0312/Learning-Code/blob/master/photo/BST.jpg)
[繪圖工具--draw.io](https://www.draw.io/)

## 學習歷程
* insert
```python
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def insert(self,root,val):
        newNode=TreeNode(val)
        if root.val == None: 
            root.val = val 
            return root
        else: 
            if root.val < val :
                if root.right == None: 
                   root.right = newNode
                   return root.right
                else: 
                    return Solution().insert(root.right, val) 
            else: 
                if root.left == None: 
                    root.left = newNode 
                    return root.left
                else: 
                    return Solution().insert(root.left, val)

node1=TreeNode(10)
Solution().insert(node1,30)
print(node1.right==30)
```
    print出來為false，原因:print應該要打node1.right.val，才表示他的值
    
* delete
```python
   def delete(self, root, target):
        if root == None: 
            return None
        elif root.val < target:
            root = root.right
            return root
        elif root.val > target:
            root = root.left
            return root
```
    
    錯誤:root = root.right，應該要用root.right=去跑delete。
    
在此參考 https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/
    
```python
    def delete(self, root, target):
        if root == None:
            return None
        elif root.val < target:
            root.right = self.delete(root.right,target)

        elif root.val > target:
            root.left = self.delete(root.left,target)
```
接著進入到刪除的部分，首先必須了解有3種情況
* 該刪除的點，沒有左右子節點
* 該刪除的點，只有一個子節點(左or右)
* 該刪除的點，包含兩個子節點

#### 沒有左右子節點
    做法很簡單，將root指向none，刪除完成。
```python
            if root.left == None and root.right == None:
                root = None
                return root
```
    在此是正確的，但是這種情況只能在該刪除點不為重複值時才能進行。

因此將程式是改為:
```python
            if root.left == None and root.right == None:
                root = None
                return self.delete(root,target)
```
    表示刪除完一個後，再回去檢查，因此可以解決重複值的問題。
#### 只有一個子節點(左or右)
    作法也容易想，將root指向該子節點。
```python
            elif root.left != None and root.right == None:
                root = root.left
                return self.delete(root,target)
            elif root.left == None and root.right != None:
                root = root.right
                return self.delete(root,target)
```
#### 包含兩個子節點
 在此我思考了許久如何達成，因此參考:http://alrightchiu.github.io/SecondRound/binary-search-tree-sortpai-xu-deleteshan-chu-zi-liao.html ，此篇有說明當遇到兩個子節點的情況。我選擇了一個做法:找right最小的節點。
```python
            elif root.left != None and root.right != None:
                root = Solution().findmin(root.right)
    def findmin(self,root):
        if root.left != None:
            root = root.left
            return Solution.findmin(root)
        else:
            return root
```
    錯誤: 在root的左節點跟著刪除!!!
    
因此我命名minval，將此值表示root.right進到findmin回傳回來的值，在將root的值指向它。
```python
            elif root.left != None and root.right != None:
                minval = Solution().findmin(root.right)
                self.delete(root, minval.val)
                root.val=minval.val
```

* search
search與insert作法很像，當root的值比target大，往右走，並將root指向root.right，反之指向left。若沒有該值，返回None。
```python
    def search(self, root, target):
        if target > root.val:
            if root.right == None:
                return None
            else:
                root = root.right
                return Solution().search(root,target) 

        elif target < root.val:
            if root.left == None:
                return None           
            else:
                root = root.left
                return Solution().search(root,target)

        else:
            return root
```

* modify
剛開始的想法很簡單，將原值做delete，將要修改後的值做insert，如下:
```python
     def modify(self, root, target, new_val):
         if root.val == target:
             root.val = new_val
         else:
             Solution().delete(root,target)
             Solution().insert(root,new_val)
             return root
```
    但有這個想法時，delete未能打出來，再加上delete有多種的情況，並不保證一定為正確的，因此決定針對modify本身。
```python
    def modify(self, root, target, new_val):
        if root != None:
            if root.val == target:
                root.val = new_val
                return root  
            elif root.val<target:
                root=root.right
                return Solution().modify(root, target, new_val)
            else:
                root=root.left
                return Solution().modify(root, target, new_val)       
        else:
            return False
```
## 新增
###### 註1.:若遇到重複值情況，將insert到左邊。
```python
    def insert(self,root,val):
        newNode=TreeNode(val) #newnode為等一下要新增的值
        if root.val == None: #若root為空，root的值就為要新增進來的val
            root.val = val 
            return root
        else: 
            if root.val < val : #val的值較大，往右走
                if root.right == None: #往右走如果為空
                   root.right = newNode #加入值
                   return root.right
                else: 
                    return Solution().insert(root.right, val) #如果跑完一次還沒找到位置(None)，則返回insert找
            else: #其他:val的值較小或等於root往右走
                if root.left == None: #往左走如果為空
                    root.left = newNode #加入值
                    return root.left
                else: 
                    return Solution().insert(root.left, val)
```
## 刪除
分為3種情況:
* root沒有子節點
* root只有一個子節點(right or left)
* root有兩個子節點

```python
    def delete(self, root, target):
        if root == None: #root為空
            return None #返回
        elif root.val < target: #若要刪除的值比root值大
            root.right = self.delete(root.right,target) #root=root.right，繼續往左找
        elif root.val > target: #若要刪除的值比root值小
            root.left = self.delete(root.left,target) #root=root.left，繼續往右找
        else: #root的值等於target(表示找到此值)
            if root.left == None and root.right == None: #若root沒有子節點
                root = None #root直接變空值(刪除完成)
                return self.delete(root,target) #由於可能有重複值，因此繼續找
            elif root.left != None and root.right == None: #若root只有左節點
                root = root.left #將root指向左節點
                return self.delete(root,target)
            elif root.left == None and root.right != None: #若root只有右節點
                root = root.right #將root指向右節點
                return self.delete(root,target)
            elif root.left != None and root.right != None: 若root有兩個左右子節點
                minval = Solution().findmin(root.right) #找右邊最小的，並將值取為minval
                self.delete(root, minval.val) 
                root.val=minval.val 
        return root
```

## 查詢
###### 註1.:若找不到該值，回傳None。
```python
    def search(self, root, target): #target為要查詢的值
        if target > root.val: #target的值比root的值大往右走
            if root.right == None: #如果往右走沒有東西
                return None #表示target不存在於tree裡，返回None
            else:
                root = root.right #若有值，root就會為root的右節點
                return Solution().search(root,target) #返回繼續找

        elif target < root.val: #target的值比root的值小往左走
            if root.left == None: #如果往左走沒有東西
                return None #表示target不存在於tree裡，返回None
            else:
                root = root.left #若有值，root就會為root的左節點
                return Solution().search(root,target) #返回繼續找

        else: #target的值等於root的值
            return root  #表示找到了，返回root
```

## 修改
```python
    def modify(self, root, target, new_val):
        if root != None: #root必須要有東西
            if root.val == target: #若root的值為要修改得值
                root.val = new_val #將原值換成新值
                return root  
            elif root.val<target: #若原值大於root值(表示要往右找)
                root=root.right
                return Solution().modify(root, target, new_val) #若沒找到返回繼續
            else:
                root=root.left #若原值小於root值(表示要往左找)
                return Solution().modify(root, target, new_val) #若沒找到返回繼續
        else: #若root為空，回傳false
            return False
```
 
###### 參考資料
[BST維基百科](https://zh.wikipedia.org/wiki/%E4%BA%8C%E5%85%83%E6%90%9C%E5%B0%8B%E6%A8%B9)

[BST圖片來源](https://www.javatpoint.com/binary-search-tree)
