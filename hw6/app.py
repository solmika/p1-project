import os
from dotenv import load_dotenv
import requests
from flask import Flask, redirect, render_template, request

from parks import parks_by_state
from weather import Weather

load_dotenv()
NPS_KEY = os.getenv("NPS_API_KEY")
app = Flask(__name__)

@app.route("/")
def home():
   return render_template("home.html")

@app.route("/results")
def results():
    typed_state = request.args.get("stateCode", "").strip()
    if not typed_state:
        return render_template("home.html", error="Type a state (in abbreviated form) to search.")
    try:
        parks = parks_by_state(typed_state)
        if parks is None:
            return render_template("home.html", error=f"We couldn't find parks in \"{typed_state}\". Check the spelling or ensure that the state is in abbreviated form.")
    except requests.RequestException:
        return render_template("home.html", error="Something's down. Please try again in a few minutes.")
    return render_template("results.html", state=typed_state, parks=parks)


@app.route("/save", methods=["POST"])
def save():
    art = {key: request.form.get(key, "") for key in ["title", "artist", "made_in", "date", "image", "link"]}
    if art["link"]:
        add_to_lesson(art)
    return redirect("/lesson")


@app.route("/remove", methods=["POST"])
def remove():
    remove_from_lesson(request.form.get("link", ""))
    return redirect("/lesson")


@app.route("/lesson")
def lesson():
    return render_template("lesson.html", artworks=load_lesson())


if __name__ == "__main__":
    app.run(debug=True)
