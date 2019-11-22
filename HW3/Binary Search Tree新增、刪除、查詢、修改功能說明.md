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
    def modify(self, root, target, new_val): #target為原來的值，new_val表示要修改的值。
        if root.val == target: #root的值等於原來的值
            root.val = new_val #將原來的值改成新的值
        else: #其他(未找到)
            Solution().insert(root,new_val) #去新增要修改後的值
            return Solution().delete(root,target) #刪除原來的值
```
