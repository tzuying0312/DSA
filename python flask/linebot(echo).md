## Linebot
>建立一個echo bot (傳什麼回什麼)
## 建立 linebot 帳號
[Line Business](https://account.line.biz/login?scope=line&redirectUri=https%3A%2F%2Fdevelopers.line.biz%2Fconsole%2Fchannel%2F1653584465%2Fmessaging-api)

>點擊使用LINE帳號登入

![](https://i.imgur.com/nadV1Rr.jpg)

>到Providers，按下create
 
![](https://i.imgur.com/rzuB0JA.jpg)

>Create a channel選擇Create a Messaging API channel，並填寫資料。

![](https://i.imgur.com/0vD2UW9.jpg)

>到Messaging API，把不需要的關閉。

![](https://i.imgur.com/0zd0qfP.jpg)


>到Messaging API把webhook打開。

**架設webhook方法:**

1. herku [範例](https://github.com/tzuying0312/Learning-Code/blob/master/python%20flask/deploy%20to%20heroku.md)
2. ngrok [範例](https://github.com/tzuying0312/Learning-Code/blob/master/python%20flask/ngrok.md)

![](https://i.imgur.com/QnYiL18.jpg)

**特別注意**，下列兩個會在程式碼中放入。

>* 在Basic settings底下，有叫Channel secret。
>* 在Messaging API底下，有叫Channel access token，若沒看到請按issue即會顯示。

## 程式碼
```python
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)


line_bot_api = LineBotApi('YOUR_LineBot_Channel access token')
handler = WebhookHandler('YOUR_LineBot_Channel secret')

@app.route("/", methods=['GET'])
def hello():
    return "Hello World!"

@app.route("/", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    print("Request body: " + body, "Signature: " + signature)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
       abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    print(msg)
    msg = msg.encode('utf-8')
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))

if __name__ == "__main__":
    app.run(debug=True)
```

程式碼來源:https://ithelp.ithome.com.tw/articles/10195014

## 架設webhook，在此我使用ngrok來測試。
![](https://i.imgur.com/KzWnsGp.jpg)
