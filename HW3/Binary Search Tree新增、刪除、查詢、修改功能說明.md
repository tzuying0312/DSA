## 新增

``` python
def insert(self,root,val):
    newNode=TreeNode(val) #newnode為等一下要新增的值
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
```

## 刪除

## 查詢

## 修改
