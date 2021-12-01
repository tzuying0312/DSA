class Solution(object):
    #分割
    def merge_sort(self,list): 
        self.list=list
        if len(list)<2:#list小於2，表示都已切至成單一個元素。
            return list
        else:
            left=list[:len(list)//2] #從長度的一半開始切，分成左右
            right=list[len(list)//2:]
        left=Solution().merge_sort(left)
        right=Solution().merge_sort(right)
        return Solution().merge(left,right) #不斷切割至list小於2。
        
    #合併
    def merge(self,left,right):
        i=0 #代表左邊元素的第幾個位置
        j=0 #代表右邊元素的第幾個位置
        done=[]
        while i<len(left) and j<len(right) : #左右兩邊的低一個元素開始比較

            if left[i]>right[j]: #左大於右，將右邊的元素放置到done(排好)
                done.append(right[j])
                j+=1 #由於右邊的第一位元素以排列完成，因此下一次比較的元素為右邊的第二位。

            else:
                done.append(left[i]) 
                i+=1
    
        return done+left[i:]+right[j:] 
