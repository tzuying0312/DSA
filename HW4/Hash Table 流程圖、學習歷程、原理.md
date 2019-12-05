## Hash Table
- 雜湊表示儲存成對數據的資料結構之一，數據為成對的鍵(key)和值(value)。
- 通過一個關於鍵值的函數，將所需查詢的數據映射到表中一個位置來查詢記錄。
- 資料庫的觀點：資料進行索引，以利管理。
- 密碼學的觀點：資料進行編碼，以求隱蔽。

> 以下圖為例來說明
> 1. 首先我們會考慮如何存入key的數據(ex:John Smith)
> 2. 使用hash function(可能依照編碼、16進為等等的方式進行加密)
> 3. 將求得的值除以buckets，求得餘數
> 4. 將key的數據存入至求得餘數的buckets

![hash_table](https://github.com/tzuying0312/Learning-Code/blob/master/photo/hash_table.png)

###### 參考資料
[圖片來源](https://www.wikiwand.com/en/Hash_table)

[維基百科](https://zh.wikipedia.org/wiki/%E5%93%88%E5%B8%8C%E8%A1%A8)

演算法圖鑑
