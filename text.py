from flask import Flask
app =Flask(__name__)
@app.route("/")
def jenkins():
    return '<h1>jenkins测试项目</h1>'

if __name__ == "__main__":
    app.run('0.0.0.0')
    