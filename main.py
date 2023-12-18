from flask import Flask #載入 Flask
app=Flask(__name__) #建立 Application

#建立網站首頁的回應
@app.route("/")
def index(): #用來回應網站首頁的內容
    return "Hello Flask" #回傳網站首頁的內容

#啟動網站伺服器
app.run()