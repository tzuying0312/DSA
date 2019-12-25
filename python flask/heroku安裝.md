## Heroku
>Heroku是一個支援多種程式語言的雲平台即服務(PaaS)。
可以將程式碼推播上去，佈署各種網站。
可以呼叫此網址做事情，ex : Webhook。
## 安裝流程
1. 申請Heroku帳號
>[Heroku官網](https://www.heroku.com/)
按下**SIGN UP FOR FREE**，來申請免費帳號

![](https://i.imgur.com/knYjJEn.jpg)

2. 安裝Heroku Cli
>[安裝Heroku Cli](https://devcenter.heroku.com/articles/getting-started-with-python#set-up)
>選擇自己的選擇自己的作業系統
>Heroko Cli是一個用來管理、創建、提交等命令的工具

![](https://i.imgur.com/ICIlvze.jpg)

3. 創建app
>如下圖，右上角有個new，點擊並create new app。

![](https://i.imgur.com/nMsoUJq.jpg)

4. 設定名字及區域
>App name 不得重複，區域只有Europe或United States，我選擇United States。

![](https://i.imgur.com/EutF68S.jpg)

## 執行命令
* 登入，以下兩種
1.跑出指令請你輸入email，輸入即可。
2.跳轉到網頁請你登入。
```
$ heroku login
```
* 到自己專案名稱底下
```
cd  你的專案名稱
```
* deploy(使用git方法)
```
$ git add .
$ git commit -am "make it better"
$ git push heroku master
```
* 查看日誌
```
heroku logs --tail
```

參考資料:
https://xiaosean.github.io/server/2018-04-11-Flask_Heroku/
