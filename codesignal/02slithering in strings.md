# Slithering in Strings
###### codesignal練習題目和解答，以及python中的函數或語法(放在Answers下)。
## 12 fixMessage
One of your friends has an awful writing style: he almost never starts a message with a capital letter, but adds uppercase letters in random places throughout the message. It makes chatting with him very difficult for you, so you decided to write a plugin that will change each message received from your friend into a more readable form.

Implement a function that will change the very first symbol of the given message to uppercase, and make all the other letters lowercase.

Example
```python
For message = "you'll NEVER believe what that 'FrIeNd' of mine did!!1",
the output should be
fixMessage(message) = "You'll never believe what that 'friend' of mine did!!1".

```
Answers
```python
def fixMessage(message):
    return message.capitalize()
```

    python 英文大小寫轉換
    .upper()         # 所有小寫換大寫 
    .lower()         # 所有大寫換小寫
    .capitalize()    # 第一個字母為大寫，其餘小寫
    .title())        # 所有單字的開頭為大寫，其餘小寫 EX:One Of Your Friends

## 13 catWalk
You've been working on a particularly difficult algorithm all day, and finally decided to take a break and drink some coffee. To your horror, when you returned you found out that your cat decided to take a walk on the keyboard in your absence, and pressed a key or two. Your computer doesn't react to letters being pressed when an unauthorized action appears, but allows typing whitespace characters and moving the arrow keys, so now your masterpiece contains way too many whitespace characters.

To repair the damage, you need to start with implementing a function that will replace all multiple space characters in the given line of your code with single ones. In addition, all leading and trailing whitespaces should be removed.

Example
```python
For
line = "def      m   e  gaDifficu     ltFun        ction(x):"
the output should be
catWalk(line) = "def m e gaDifficu ltFun ction(x):".

```
Answers
```python
def catWalk(code):
    return  ' '.join(code.split())
```
    split()去除中間空格
    join() 將序列中的元素以指定的字符切割。

## 14 convertTabs
You found an awesome customizable Python IDE that has almost everything you'd like to see in your working environment. However, after a couple days of coding you discover that there is one important feature that this IDE lacks: it cannot convert tabs to spaces. Luckily, the IDE is easily customizable, so you decide to write a plugin that would convert all tabs in the code into the given number of whitespace characters.

Implement a function that, given a piece of code and a positive integer x will turn each tabulation character in code into x whitespace characters.

Example
```python
For code = "\treturn False" and x = 4, the output should be
the output should be
convertTabs(code, x) = "    return False"
```
Answers
```python
def convertTabs(code, x):
    return code.replace('\t', ' '*x)
```
    .replace('\t',' ')，\t用空白取代

## 15 feedbackReview
You've launched a revolutionary service not long ago, and were busy improving it for the last couple of months. When you finally decided that the service is perfect, you remembered that you created a feedbacks page long time ago, which you never checked out since then. Now that you have nothing left to do, you would like to have a look at what the community thinks of your service.

Unfortunately it looks like the feedbacks page is far from perfect: each feedback is displayed as a one-line string, and if it's too long there's no way to see what it is about. Naturally, this horrible bug should be fixed. Implement a function that, given a feedback and the size of the screen, splits the feedback into lines so that:

each token (i.e. sequence of non-whitespace characters) belongs to one of the lines entirely;
each line is at most size characters long;
no line has trailing or leading spaces;
each line should have the maximum possible length, assuming that all lines before it were also the longest possible.

Example
```python
For feedback = "This is an example feedback" and size = 8,
the output should be
feedbackReview(feedback, size) = ["This is", 
                                  "an", 
                                  "example", 
                                  "feedback"]
```
Answers
```python
import textwrap

def feedbackReview(feedback, size):
    return textwrap.wrap(feedback, size)
```
    textwrap模塊提供wrap()、fill()、indent()、dedent()和以及TextWrapper類的函數。
    .wrap(feedback, size)：長度為size

## 16 isWordPalindrome
Given a word, check whether it is a palindrome or not. A string is considered to be a palindrome if it reads the same in both directions.

Example
```python
For word = "aibohphobia", the output should be
isWordPalindrome(word) = true;

For word = "hehehehehe", the output should be
isWordPalindrome(word) = false.
```
Answers
```python
def isWordPalindrome(word):
    return word == word[::-1]
```
    [::-1]順序相反
    EX:
    a=[1,2,3,4,5]
    b=a[::-1]
    b為[5,4,3,2,1]
    
## 17 permutationCipher
You found your very first laptop in the attic, and decided to give in to nostalgia and turn it on. The laptop turned out to be password protected, but you know how to crack it: you have always used the same password, but encrypt it using permutation ciphers with various keys. The key to the cipher used to protect your old laptop very conveniently happened to be written on the laptop lid.

Here's how permutation cipher works: the key to it consists of all the letters of the alphabet written up in some order. All occurrences of letter 'a' in the encrypted text are substituted with the first letter of the key, all occurrences of letter 'b' are replaced with the second letter from the key, and so on, up to letter 'z' replaced with the last symbol of the key.

Given the password you always use, your task is to encrypt it using the permutation cipher with the given key.

Example
```python
For password = "iamthebest" and
key = "zabcdefghijklmnopqrstuvwxy", the output should be
permutationCipher(password, key) = "hzlsgdadrs".
```
Answers
```python
def permutationCipher(password, key):
    table = str.maketrans(string.ascii_lowercase, key)
    return password.translate(table)
```
    .translate為根據table給出256個字符轉換
    table為通過maketrans轉換而來
    string.ascii_lowercase:小寫字母'abcdefghijklmnopqrstuvwxyz'
    
## 18 competitiveEating
The World Wide Competitive Eating tournament is going to be held in your town, and you're the one who is responsible for keeping track of time. For the great finale, a large billboard of the given width will be installed on the main square, where the time of possibly new world record will be shown.

The track of time will be kept by a float number. It will be displayed on the board with the set precision precision with center alignment, and it is guaranteed that it will fit in the screen. Your task is to test the billboard. Given the time t, the width of the screen and the precision with which the time should be displayed, return a string that should be shown on the billboard.

Example
```python
For t = 3.1415, width = 10, and precision = 2,
the output should be
competitiveEating(t, width, precision) = "   3.14   "
```
Answers
```python
def competitiveEating(t, width, precision):
    return "{0:.{1}f}".format(t,precision).center(width)
```
    {:.2f}小數後兩位

## 19 newStyleFormatting
You came to work in a big company as a Senior Python Developer. Unfortunately your team members seem to be quite old-school: you can see old-style string formatting everywhere in the code, which is not too cool. You tried to force the team members to start using the new style formatting, but it looks like it will take some time to persuade them: old habits die hard, especially in old-school programmers.

To show your colleagues that the new style formatting is not that different from the old style, you decided to implement a function that will turn the old-style syntax into a new one. Implement a function that will turn the old-style string formating s into a new one so that the following two strings have the same meaning:

s % (*args)
s.format(*args)

Example
```python
For s = "We expect the %f%% growth this week", the output should be
newStyleFormatting(s) = "We expect the {}% growth this week".
```
Answers
```python
def newStyleFormatting(s):
    s = re.sub('%%', '{%}', s)
    s = re.sub('%[dfFgeEGnnxXodcbs]', '{}', s)
    return re.sub('{%}','%',s)
```

## 20 getCommit
The Abanamama Version System (AVS) is a software versioning and revision control system used in highly secure environments. In this system, each commit is assigned a unique name, the first part of which consists of the username encrypted in the base-4 system using symbols '0', '?', '+', and '!', and the second part consists of symbols of English alphabet.

Given such commit, your task is go remove the username part from it and return the second part as an answer.

Example
```python
For commit = "0??+0+!!someCommIdhsSt", the output should be
getCommit(commit) = "someCommIdhsSt".
```

Answers
```python
def getCommit(commit):
    return  commit.lstrip('0?+!')
``` 

    .strip用於去除字符串的首尾字符
    .lstrip用於去除左邊的字符
    .rstrip用於去除右邊的字符。
