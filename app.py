from flask import Flask, render_template
import config
from models import Person

app = config.connexion_app
app.add_api(config.base_directory / "swagger.yml")

@app.route("/")
def home():
    people = Person.query.all()
    return render_template("home.html", people=people)

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=8000, debug=True)