# meet python
## 5 count bits
Implement a function that, given an integer n, uses a specific method on it and returns the number of bits in its binary representation.
Example
```python
For n = 50, the output should be
countBits(n) = 6.
5010 = 1100102, a number that consists of 6 digits. Thus, the output should be 6.
```
Answers
```python
def countBits(n):
    return n.bit_length()
```
    bit_length()為回傳n的二進位形式佔多少長度    

## 6 modulus
It frustrates you more than you'd like to admit that the modulus operator in Python can be applied to non-integer values. When you write code, you expect the result of the modulus operator to always be an integer, but thanks to Python this isn't always the case.

To fix this, you've decided to write your own modulus operator as a function. Your task is to implement a function that, given a number n, returns -1 if this number is not an integer and n % 2 otherwise. It is guaranteed that if the number represents an integer, it will be written without a decimal point.

Example
```python
For n = 15, the output should be
modulus(n) = 1;

For n = 23.12, the output should be
modulus(n) = -1.
```
Answers
```python
def modulus(n):
    if isinstance(n,int):
        return n % 2
    else:
        return -1
```
    isinstance(object, classinfo)    
    如果參數object是classinfo，返回True。如果不是，返回结果False。  
    
## 7 simpleSort
To understand how efficient the built-in Python sorting function is, you decided to implement your own simple sorting algorithm and compare its speed to the speed of the Python sorting. Write a function that, given an array of integers arr, sorts its elements in ascending order.
Example
```python
For arr = [2, 4, 1, 5], the output should be
simpleSort(arr) = [1, 2, 4, 5].
```
Answers
```python
def simpleSort(arr):

    n = len(arr)

    for i in range(n):
        j = 0
        stop = n - i
        while j < stop - 1:
            if arr[j] > arr[j + 1]:
                arr[j],arr[j+1]= arr[j+1],arr[j] 
            j += 1
    return arr

```
## 8 baseConversion
Your university professor decided to have a little fun and asked the class to implement a function that, given a number n and a base x, converts the number from base x to base 16. To make things more interesting, he announced that the first student to write the solution will have to answer fewer question than the rest of the class during the final exam.

Laughing devilishly, you asked if it was okay to use a language of your choice, and the unsuspecting professor answered "yes". It's settled then: Python is your language of choice!

Now you're bound to win. Implement a function that, given an integer number n and a base x, converts n from base x to base 16.
Example
```python
For n = "1302" and x = 5, the output should be
baseConversion(n, x) = "ca".

Here's why:
13025 = 20210 = ca16.
```
Answers
```python
def baseConversion(n, x):
    return hex(int(n,x))[2:]
```
如果只打return hex(int(n,x))答案會出現
