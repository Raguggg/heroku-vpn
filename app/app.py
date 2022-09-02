from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<!DOCTYPE html><html lang="en"><head> <meta charset="UTF-8"> <meta http-equiv="X-UA-Compatible" content="IE=edge"> <meta name="viewport" content="width=device-width, initial-scale=1.0"> <title>Invalid UrL</title> <style> body { background: #000; } .title { text-align: center; font-family:arial black; font-size:50px; background-image: linear-gradient(to right, red,orange,yellow,green,blue,indigo,violet); -webkit-background-clip: text; -webkit-text-fill-color: transparent; animation: move 70s linear infinite; } @keyframes move { to { background-position: 3500vh; } } .title .btn:hov{ text-align: center; font-family:arial black; font-size:50px; background-image: linear-gradient(to right, red,orange,yellow,green,blue,indigo,violet); -webkit-background-clip: text; -webkit-text-fill-color: transparent; animation: move 70s linear infinite; } @keyframes move { to { background-position: 3500vh; } } .btn{ align-items: center; text-align: center; } .btn a h1{ font-size: 70px; } .btn{ padding-top: 90px; } .btn button{ background-color: rgba(64, 255, 0, 0.633); width: 600px; border-radius: 30%; } .btn button:hover { color: rgb(0, 252, 0); } </style></head><body> <div class="title">Ragu VPN server</div> <div class="btn"> <a href="https://raguggg.github.io/Ragu-G/"><button><h1 class="title">Starting server</h1> </button></a></div></body></html>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
