
## google cloud speech to text api
* 事前準備
1. 登入 [google platfrom](https://accounts.google.com/signin/v2/identifier?service=cloudconsole&passive=1209600&osid=1&continue=https%3A%2F%2Fconsole.cloud.google.com%2F%3Fhl%3Dzh-TW%26ref%3Dhttps%3A%2F%2Fwww.google.com%2F&followup=https%3A%2F%2Fconsole.cloud.google.com%2F%3Fhl%3Dzh-TW%26ref%3Dhttps%3A%2F%2Fwww.google.com%2F&hl=zh-TW&flowName=GlifWebSignIn&flowEntry=ServiceLogin) 設立專案

2. 到左邊主選單選擇API和服務，按下**啟用API和服務**。![](https://i.imgur.com/zm7xADO.png)

3. 搜尋cloud speech to text，並按下啟用。![](https://i.imgur.com/f3fhDho.png)

4. 到左邊選單選擇憑證，按下建立憑證，並選擇服務帳戶。![](https://i.imgur.com/Kl94sqC.png)

5. 下載 JSON 格式的私密金鑰。

6. 安裝並初始化 [Cloud SDK](https://cloud.google.com/sdk/docs/)。


* 程式碼
 
1. 轉檔問題(.m4a->.wav)
> 若是直接轉檔換發生**FileNotFoundError: [WinError 2] 系统找不到指定的文件。** 錯誤是少安裝了ffmpeg ，但下載此套件也沒用，因此直接到官網下載[ffmpeg](http://www.ffmpeg.org/download.html#build-windows)，並以**AudioSegment.converter** 給他指定路徑。
```python
import ffmpeg
from pydub import AudioSegment

AudioSegment.converter = r"C:\Users\tzuying0312\Anaconda3\Lib\site-packages\pydub\bin\ffmpeg.exe"

file_name='d4zyheh3.m4a'# your file name
m4a_version = AudioSegment.from_file(file_name)
m4a_version.export("C:\\Users\\tzuying0312\\Desktop\\SPA_2_11_24.wav", format="wav") #存入的路徑及檔名
```

2. wav(32bit->16bit)
>在 cloud speech to txet 的 wav 檔中，只能為16bit。
```python
data, samplerate = sf.read(file_name)
sf.write(file_name, data, samplerate, subtype='PCM_16')

```

3. 轉成文字
>**note** : 若client = speech.SpeechClient()，出現錯誤或警告時，加上credential_path，給他剛剛下載json檔的金鑰即可。
```python
#導入Google Cloud客戶端庫
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

credential_path = r"C:\Users\tzuying0312\Desktop\python_hotel\hotel-41fc8e055f5b.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

client = speech.SpeechClient()

with io.open(file_name, 'rb') as audio_file:
    content = audio_file.read()
    audio = types.RecognitionAudio(content=content)

config = types.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
    enable_automatic_punctuation=True,#標點符號
    sample_rate_hertz=16000,#取樣率
    language_code='zh-TW')
    
response = client.recognize(config, audio)
for result in response.results:
    print('Transcript: {}'.format(result.alternatives[0].transcript))
    
```

參考資料:https://cloud.google.com/speech-to-text/docs/quickstart-client-libraries#client-libraries-usage-python
