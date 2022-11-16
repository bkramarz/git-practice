from flask import Flask

with open("text-to-read", "w") as file:
    file.write("<h1>Hello world<h1>")

app = Flask(__name__)

with open("text-to-read") as file:
    web_text = file.read()


@app.route("/")
def home():
    return web_text


if __name__ == "__main__":
    app.run(debug=True)
