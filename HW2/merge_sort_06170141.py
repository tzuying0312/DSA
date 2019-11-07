class Solution(object):
    
    def spilt(list):    
        if len(list)<2:
            return list
        else:
            left=list[:len(list)//2]
            right=list[len(list)//2:]
            return merge_sort(spilt(left),spilt(right))
        
    def merge_sort(left,right):
        i=0
        j=0
        done=[]
        while i<len(left) and j<len(right) :

            if left[i]>right[j]:
                done.append(right[j])
                j+=1

            else:
                done.append(left[i])
                i+=1
    
        return done+left[i:]+right[j:]
