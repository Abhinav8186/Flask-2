from flask import Flask

app = Flask(__name__) 
@app.route("/")
def index():
    return "index"
if __name__ == "__name__":
    app.run()