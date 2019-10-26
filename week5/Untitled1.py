#!/usr/bin/env python
# coding: utf-8

#    ## 程式碼

# In[458]:


def quicksort(list):
    if len(list)<2: #長度小於2回傳
        return list
    else:
        k=-1
        i=len(list)-1 #從最後一元素開始比較
        pivot=list[k]
        while (i<len(list) and i>=0): 
        #while跑元素，因為i為遞減，因此設立i不能為負
            j=list[i]
            if j>pivot:
                list.insert(len(list),list.pop(i))
                #若元素大於基準點，直接在list中移動位置，移至最後一位(基準點的右方)
                k=k-1
                #由於將元素移動至最後，因此基準點往前一位
            i-=1
            #從最後一位開始往前比較
    return quicksort(list[0:k])+quicksort(list[k:])


# In[459]:


lista=[7,3,8,30,15]
quicksort(lista)


# In[460]:


listb=[2,43,56,12,65,90,23]
quicksort(listb)


# ## 以下為想法以及錯誤的過程及原因

# 只創建一個list
# 若比基準大，就變動位置(移至基準點的右方)
# 若比基準小，就移除此元素，新增到sort[]

# In[451]:


#比基準大
#理解移動位置(insert(增加)，pop(刪除))
lista=[3,5,8,7,5,6,2]
lista.insert(len(lista), lista.pop(0))
lista


# In[452]:


#比基準小
#pop(刪除)、append(增加)
sorta=[]
lista=[3,5,8,7]
i=0
while i<len(lista): 
    j=lista[i]
    lista_pop=lista.pop(i)
    sorta.append(j)
i+=1
sorta


# In[453]:


#在while中進行移動
lista=[3,5,8,7,6,2]
# a=len(list)
for i in range(len(lista)-1):     
    lista.insert(len(lista), lista.pop(0))
lista


# 合併想法
# 錯誤原因:當list改變後，i仍然加1。代表會友元素沒跑到。
# ex:[3,5,8,7,6]
# 1.此時pivot為6，i=0，j=3。
# 2.接下來會移除3，並append到sort。
# 3.list變為[5,8,7,6]
# 4.i+1，i=1，此時比較元素為8
# 5.略過5，因此錯誤

# In[454]:


#合併自己的想法
def quicksort(list):
    sort=[]
    i=0
    while i<len(list):
        pivot=list[-1]
        j=list[i]
        if j>pivot:
            list.insert(len(list),list.pop(0))
        else:
            list_pop=list.pop(i)
            sort.append(j)
        i+=1
    #       return sort+list
        print(sort+[list])   


# In[455]:


a=[7,8,30,2,15]
quicksort(a)


# 詢問同學後，他建議不要創建新的list，直接在list中移動。
# 錯誤原因
# 1.i一直-1，因此不會有低於長度的可能
# 2.quicksort(list[k+1:])，若k為-1，k+1=0，也就是回到最原始的list

# In[456]:


def quicksort(list):
    if len(list)<2: 
        return list
    else:
        k=-1
        i=len(list)-1
        pivot=list[k]
        while i<len(list):
            j=list[i]
            if j>pivot:
                list.insert(len(list),list.pop(i))
                k=k-1
            i-=1
    return quicksort(list[0:k])+[pivot]+quicksort(list[k+1:])


# In[457]:


lista=[7,3,8,30,15]
quicksort(lista)


# In[ ]:




