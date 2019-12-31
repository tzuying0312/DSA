# linebot語音辨識

```python
from linebot.models import *
from pydub import AudioSegment
import speech_recognition as sr
import os
import tempfile
from google.cloud import storage
from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
import soundfile

os.environ["GCLOUD_PROJECT"] = "XXX" #將XXX改為自己的專案名。
credential_path = r"C:\Users\tzuying0312\Desktop\python_hotel\hotel-41fc8e055f5b.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

line_bot_api = LineBotApi('YOUR_LineBot_Channel access token')
handler = WebhookHandler('YOUR_LineBot_Channel secret')

app = Flask(__name__)

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

```

* 處理音訊

>由於Linebot傳過去的音檔為.acc或.m4a，但cloud speech to text api 為 wav 檔，因此要先轉檔。
```python
@handler.add(MessageEvent,message=AudioMessage)
def handle_aud(event):

    message_content = line_bot_api.get_message_content(event.message.id)
    ext = ''
    try:
        with tempfile.NamedTemporaryFile(prefix=ext + '-',delete=False) as tf:
            for chunk in message_content.iter_content():
                tf.write(chunk)
            tempfile_path = tf.name
        path = tempfile_path 

        AudioSegment.converter = r"C:\Users\tzuying0312\Anaconda3\Lib\site-packages\pydub\bin\ffmpeg.exe"
        sound = AudioSegment.from_file_using_temporary_files(path)
        wavpath = os.path.splitext(path)[0]+'.wav'
        sound.export(wavpath, format="wav")

        head_tail = os.path.split(wavpath)
        f = head_tail[1]
        client = speech.SpeechClient()
        with io.open(wavpath, 'rb') as audio_file:
            content = audio_file.read()
            audio = types.RecognitionAudio(content=content)

        config = types.RecognitionConfig(
            encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=16000,
            enable_automatic_punctuation=True,#標點符號
            language_code='zh-TW')
        response = client.recognize(config, audio)     
        for result in response.results:
            text=result.alternatives[0].transcript


    except Exception as e:
        t = '錯誤:'+str(e.args)+wavpath
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=t))


    os.remove(path)
    os.remove(wavpath)
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=text))

```

* 結果
![](https://i.imgur.com/RXHxc5o.jpg)


參考資料:http://b0212066.pixnet.net/blog/post/213111885-linebot%E8%99%95%E7%90%86%E9%9F%B3%E6%AA%94
