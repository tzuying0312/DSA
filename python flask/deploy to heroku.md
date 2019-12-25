## 部屬至 Heroku 範例

#### 前置作業
>首先，因為在push上去時，不斷發生錯誤，後來發現是因為conda環境導致。因此點擊settings，往下滑到Buildpacks。

![](https://i.imgur.com/2VpnlVX.jpg)

>按下 Add buildpack，把https://github.com/kennethreitz/conda-buildpack.git 加入 Enter Buildpack URL。

![](https://i.imgur.com/xKbr4Iv.jpg)

> 可以點擊左上HEROKU，可以看到自己所有的app，右邊會多了conda，此時 git push 就不會有問題。

![](https://i.imgur.com/WzcuN95.jpg)

#### 專案底下有的檔案
* flask_test.py
* Procfile (**檔名就為Procfile，不是.txt**)
* requirements.txt
* runtime.txt

>flask_test.py
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello World!'

```
>Procfile (flask_test換成自己的檔名)
```python
web gunicorn flask_test:app
```
>requirements.txt (套件名稱及版本)，可以透過下方指令，查看已安裝的套件。
```
$ pip freeze > requirements.txt
```
>runtime.txt (python版本)
```
name: myenv
python=3.7.5
```

#### 部屬
```
$ git add .
$ git commit -am "make it better"
$ git push heroku master
```
#### 打開網址
>將[your app name]換成你的app名稱即可。
```
網址為:https://[your app name].herokuapp.com/
```
>開啟網頁

![](https://i.imgur.com/xAa2ftW.jpg)
