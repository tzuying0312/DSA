# Lurking in Lists
###### codesignal練習題目和解答，以及python中的函數或語法(放在Answers下)。
## 22 listsConcatenation
Given two lists lst1 and lst2, your task is to return a list formed by the elements of lst1 followed by the elements of lst2.

Note: this is a bugfix task, which means that the function is already implemented but there is a bug in one of its lines. Your task is to find and fix it.

Example
```python
For lst1 = [2, 2, 1] and lst2 = [10, 11], the output should be
listsConcatenation(lst1, lst2) = [2, 2, 1, 10, 11].

```
Answers
```python
def listsConcatenation(lst1, lst2):
    res = lst1
    res.extend(lst2)
    return res
```

## 23 twoTeams
There are some students standing in a row, each has some number written on their back. The students are about to divide into two teams by counting off by twos: those standing at the even positions (0-based) will go to team A, and those standing at the odd position will join the team B.

Your task is to calculate the difference between the sums of numbers written on the backs of the students that will join team A, and those written on the backs of the students that will join team B.

Example
```python
For students = [1, 11, 13, 6, 14], the output should be
twoTeams(students) = 11.

Students with numbers 1, 13 and 14 will join team A, and students with numbers 11 and 6 will join team B. Thus, the answer is (1 + 13 + 14) - (11 + 6) = 11.

```
Answers
```python
def twoTeams(students):
    return sum([item for item in students[::2]]) - sum([item for item in students[1::2]])
```
    [start:end:step]
    EX: range(100)[5:18:2] 輸出為 [5, 7, 9, 11, 13, 15, 17]
    
## 24 removeTasks
Today is a good day: it's the kth year since you started to work at the company, which means you have to have a party today. In order to get home earlier and prepare for the jamboree, you need to get home early. You decided to remove each kth tasks from your toDo list, since today is your day and you can do whatever you please.

Given the list of task ids in your toDo list, remove each kth task from it and return the list of remaining tasks.

Example
```python
For k = 3 and toDo = [1237, 2847, 27485, 2947, 1, 247, 374827, 22],
the output should be
removeTasks(k, toDo) = [1237, 2847, 2947, 1, 374827, 22].

```
Answers
```python
def removeTasks(k, toDo):
    del toDo[k-1::k]
    return toDo
```
    [start:end:step]
    EX: range(100)[5:18:2] 輸出為 [5, 7, 9, 11, 13, 15, 17]
