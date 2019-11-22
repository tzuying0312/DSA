#### 根據BST原理，大的往右，其餘往左。
## 新增
``` python
def insert(self,root,val):
    newNode=TreeNode(val) #newnode為等一下要新增的值
    if root.val == None: 若root為空，root的值就為input進來的val
        root.val = val 
        return root
    else: #若root不為空
        if root.val < val : #val的值較大，往右走
            if root.right == None: #往右走如果為空
                root.right = newNode #加入值
                return root.right 
            else: 
                return Solution().insert(root.right, val) #如果跑完一次還沒找到位置(None)，則返回insert找
        else: #其他:val的值較小或等於root往右走
            if root.left == None: 往左走如果為空
                root.left = newNode #加入值
                return root.left
            else: 
                return Solution().insert(root.left, val)
```

## 刪除

## 查詢

## 修改
