class ListNode: 
    
    def __init__(self, val):
        self.val = val
        self.next = None

class MyHashSet:  
    
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity   
        
    def findindex(self,key):
        from Crypto.Hash import MD5
        h = MD5.new()
        h.update(key.encode("utf-8"))
        h = int(h.hexdigest(),16)
        return h
    
    def add(self, key):
        if self.contains(key):
            return     
        key = self.findindex(key)
        index = key % self.capacity
        new_node = ListNode(key)
        if self.data[index] is None:
            self.data[index] = new_node
            return True
        else:
            node = self.data[index]
            while node.next != None:
                node = node.next
            # self.next = node.next
            new_node.next = self.data[index]
            self.data[index] = new_node
            
    def remove(self, key):
        if self.contains(key):
            key = self.findindex(key)
            index = key % self.capacity
            node = self.data[index]
            if node.val == key:
                self.data[index] = node.next
                return
            else:
                while node.next != None and node.val != key :
                    node.next = node.next.next
            return True
        else:
            return False
        
    def contains(self, key):
        key = self.findindex(key)
        index = key % self.capacity
        if self.data[index] is None:
            return False
        else:
            node = self.data[index]
            while node:
                if node.val == key:
                    return True
                node = node.next
            return False
        
#參考資料
#https://www.nosuchfield.com/2016/07/29/the-python-implementationp-of-HashTable/
