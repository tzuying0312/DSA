## Ngrok

* 可以提供一個https的Server，與heroku一樣。
* push的速度比heroku簡單且快速。
* 網址不固定:重新啟動後，網址會變動，heroku為固定的。

## 註冊
[ngrok官網](https://ngrok.com/)
>按下之後，點擊get started for free 

![](https://i.imgur.com/8Ruks2i.jpg)

>點擊後，會跳到以下畫面，
1. download 自己的作業系統
2. 解壓縮
3. 記住自己的authtoken

![](https://i.imgur.com/oTQQ4Ic.jpg)


## 範例
>開啟解壓縮後的ngrok.exe
```
./ngrok authtoken -YOUR_AUTH_TOKEN-
```
>再打上下面那行，5000可以更改自己要的port。
```
ngrok http 5000
```
>成功的話會看到以下畫面，此時你的網址 https://b08cb5e1.ngrok.io

![](https://i.imgur.com/CMAw0SZ.jpg)

>不要關閉ngrok，在終端機打上python flask_test.py

flask_test.py
```python
from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/')
def homepage():
    return 'Hello World!'

if __name__ == "__main__":
    app.run()
```

>會出現以下畫面，代表跑在5000 port，因此剛剛在ngrok才會打5000。

![](https://i.imgur.com/00OmAm5.jpg)

>最後到網址查看

![](https://i.imgur.com/jzdG4dP.jpg)

參考資料:https://xiaosean.github.io/server/2018-04-18-Flask_Ngrok/
