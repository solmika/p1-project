import requests
from flask import Flask, redirect, render_template, request

from parks import Parks
from weather import Weather

app = Flask(__name__)

def results_page(place="", country=None, city=None, wider=None, error=None):
    return render_template("index.html", place=place, country=country, city=city, wider=wider, error=error,
                           lesson_count=len(load_lesson()))
@app.route("/")
def home():
   return render_template("home.html")

@app.route("/results")
def results():
    typed = request.args.get("stateCode", "").strip()
    if not typed:
        return results_page(error="Type a state (in abbreviated form) to search.")
    try:
        here = find_state(typed)
        if here is None:
            return results_page(stateCode=typed, error=f"We couldn't find parks in \"{typed}\". Check the spelling or ensure that the state is in abbreviated form.")
        names = list(dict.fromkeys([typed, here["name"]]))
        city = artworks_about(names)                       
        wider = None
        if here["country"] and here["country"] not in names:
            shown = {art["link"] for art in city[1]}
            wider = artworks_about([here["country"]], skip=shown)
    except requests.RequestException:
        return results_page(stateCode=typed, error="Something's down. Please try again in a few minutes.")
    return results_page(stateCode=typed, country=here["country"], city=city, wider=wider)


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
