## Hash Table
- 雜湊表示儲存成對數據的資料結構之一，數據為成對的鍵(key)和值(value)。
- 通過一個關於鍵值的函數，將所需查詢的數據映射到表中一個位置來查詢記錄。
- 資料庫的觀點：資料進行索引，以利管理。
- 密碼學的觀點：資料進行編碼，以求隱蔽。

> 以下圖為例來說明
> 1. 首先我們會考慮如何存入key(ex:John Smith)的數據
> 2. 使用hash function(可能依照編碼、16進為等等的方式進行加密)
> 3. 將求得的值除以buckets的總數，求得餘數
> 4. 將key的數據存入至求得餘數的buckets

![hash_table](https://github.com/tzuying0312/Learning-Code/blob/master/photo/hash_table.png)

## Hash Table function

- **hash function**
> 加密動作，將key經過加密並找到自己的buckets
```python
    def fineindex(self,key):
        from Crypto.Hash import MD5
        h = MD5.new()
        h.update(key.encode("utf-8"))
        x = int(h.hexdigest(),16) #轉為16進位
        return x % self.capacity  #除以buckets的總數，以求得key對應的位置
```

- **新增**
> 新增前先查詢是否有此key的存在

> 有就不必再次新增

> 沒有就去尋找適當的buckets位置
``` python
    def add(self, key):
        if self.contains(key): #為了避免重複值得問題，因此先去檢查是否有此key的存在
            return 若有，直接return    
        index = self.fineindex(key) #尋找加密後(hash function)對應到的buckets
        new_node = ListNode(key)
        if self.data[index] is None: #如果data[index]為空
            self.data[index] = new_node #直接放入
            return True
        else:
            node = self.data[index]
            while node.next != None: #在這裡我們要尋找空的位置，讓key放入
                node = node.next #若不為空，我們就跳下一位置，直到有空位
            new_node.next = self.data[index]
            self.data[index] = new_node #放入
```
- **刪除**
> -刪除前先查詢是否有此key的存在
> - 沒有就不必刪除
> - 有就去尋找key的buckets位置，並將它指向下一位(刪除完成)
``` python
    def remove(self, key):
        if self.contains(key): #先檢查是否有此key，有則尋找位置
            index = self.fineindex(key) #尋找加密後(hash function)對應到的buckets
            node = self.data[index] 
            if node.val == key: #若值等於key值
                self.data[index] = node.next #將值指向下一個(刪除完成)
                return
            else: #還沒找到繼續往後找
                while node.next != None and node.val != key :
                    node.next = node.next.next #node.next #再只向後一位，直到找到
            return True
        else:
            return False 若沒有直接回傳False
```
- **查詢**
> -查詢前先看位置是否有東西，沒有即可直接回傳False
> - 有東西就去做確認是否是key值
> - 若不是要找的key，往後找
``` python
    def contains(self, key):
        index = self.fineindex(key) #尋找加密後(hash function)對應到的buckets
        if self.data[index] is None: #若data[index]不存在或沒有值
            return False #直接回傳False
        else:
            node = self.data[index]
            while node: 
                if node.val == key: #若值等於key
                    return True #回傳True
                node = node.next #不等於，往後找
            return False
``` 


###### 參考資料
[圖片來源](https://www.wikiwand.com/en/Hash_table)

[維基百科](https://zh.wikipedia.org/wiki/%E5%93%88%E5%B8%8C%E8%A1%A8)

演算法圖鑑
