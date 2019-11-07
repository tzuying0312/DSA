class Solution(object):
    def heap_sort(mylist):
        for i in range(len(mylist),-1,-1):
            root=i
            left=2*i+1
            right=2*i+2
            if left<len(mylist):
                if mylist[root]>mylist[left]: 
                    mylist[i],mylist[2*i+1]=mylist[2*i+1],mylist[i]
            if right<len(mylist):
                if mylist[root]>mylist[right]:
                    mylist[i],mylist[2*i+2]=mylist[2*i+2],mylist[i]
        done(mylist)
    
    ok=[]


    def done (mylist):
    
        ok.append(mylist[0])
        mylist[0]=mylist[-1]
        mylist.pop(-1)
        print(ok)
    
        if len(mylist)>0:
            mylist=heap_sort(mylist)
