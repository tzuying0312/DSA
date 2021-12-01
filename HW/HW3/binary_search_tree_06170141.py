# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
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
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode(inserted node)
        """
    

    def delete(self, root, target):
        if root == None:
            return None
        elif root.val < target:
            root.right = self.delete(root.right,target)
        elif root.val > target:
            root.left = self.delete(root.left,target)
        else:
            if root.left == None and root.right == None:
                root = None
                return self.delete(root,target)
            elif root.left != None and root.right == None:
                root = root.left
                return self.delete(root,target)
            elif root.left == None and root.right != None:
                root = root.right
                return self.delete(root,target)
            elif root.left != None and root.right != None:
                minval = Solution().findmin(root.right)
                self.delete(root, minval.val)
                root.val=minval.val
        return root

    """
    :type root: TreeNode
    :type target: int
    :rtype: TreeNode(the root of new completed binary search tree) (cannot search())   
    """
    def findmin(self,root):
        if root.left != None:
            root = root.left
            return Solution.findmin(root)
        else:
            return root


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

        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """

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


        """
        :type root: TreeNode
        :type target: int
        :type new_val: int
        :rtype:TreeNode(the root of new completed binary search tree) (cannot search())
        """
        
    def printest(self,root):
        if root:
            print(root.val)
            self.printest(root.left)
            self.printest(root.right)
#參考資料:
#http://alrightchiu.github.io/SecondRound/binary-search-tree-sortpai-xu-deleteshan-chu-zi-liao.html
#https://www.youtube.com/watch?v=YlgPi75hIBc
#https://www.youtube.com/watch?v=LSju119w8BE
