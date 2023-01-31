from flask import Flask, render_template
import connexion

app = connexion.App(__name__, specification_dir="./")
app.add_api("swagger.yml")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/home")
def home_page():
    WELCOME_MESSAGE = {
        "greeting": {
        "welcome": "Hello world",
        },
    }
    return list(WELCOME_MESSAGE.values())

#if __name__ == "__main__":
    #app.run(host="0.0.0.0", port=8000, debug=True)