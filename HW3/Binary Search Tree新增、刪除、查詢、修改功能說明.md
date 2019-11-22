## 新增
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
```python
    def delete(self, root, target):
        if root == None: #root為空
            return None #返回
        if root.val < target: #若要刪除的值比root值大
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
參考資料:https://emn178.pixnet.net/blog/post/94574434
