# meet python
## 5 count bits
Implement a function that, given an integer n, uses a specific method on it and returns the number of bits in its binary representation.

Example
```
For n = 50, the output should be
countBits(n) = 6.
5010 = 1100102, a number that consists of 6 digits. Thus, the output should be 6.
```

```python
def countBits(n):
    return n.bit_length()
```
`bit_length()為回傳n的二進位形式佔多少長度`

## 6 modulus

It frustrates you more than you'd like to admit that the modulus operator in Python can be applied to non-integer values. When you write code, you expect the result of the modulus operator to always be an integer, but thanks to Python this isn't always the case.

To fix this, you've decided to write your own modulus operator as a function. Your task is to implement a function that, given a number n, returns -1 if this number is not an integer and n % 2 otherwise. It is guaranteed that if the number represents an integer, it will be written without a decimal point.

Example
```
For n = 15, the output should be
modulus(n) = 1;

For n = 23.12, the output should be
modulus(n) = -1.
```

```python
def modulus(n):
    if isinstance(n,int):
        return n % 2
    else:
        return -1
```
