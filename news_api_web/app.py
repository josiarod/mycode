import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return hello
    # NEWSURL = requests.get("https://newsapi.org/v2/everything?q=tesla&from=2022-07-15&sortBy=publishedAt&apiKey=70ea2326e2764aa4bc9300677bc3ff6f")

    # data = NEWSURL.json()
    # articles = data["articles"]

    # title = article['title']
    # description = article['description']
    # Url = article["url"]
    # return render_template('index.html', **variables())


if __name__ == "__main__":
    app.run()