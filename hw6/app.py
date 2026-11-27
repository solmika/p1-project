import requests
from flask import Flask, redirect, render_template, request

from parks import Parks
from weather import Weather

app = Flask(__name__)

@app.route("/")
def home():
   return render_template("home.html")

@app.route("/results")
def results():
    typed = request.args.get("stateCode", "").strip()
    if not typed:
        return search_page(error="Type a place to search.")
    try:
        here = find_place(typed)                              # API 1: what is this place?
        if here is None:
            return search_page(stateCode=typed, error=f"We couldn't find \"{typed}\". Check the spelling, or try a nearby city.")
        names = list(dict.fromkeys([typed, here["name"]]))   # what they typed + Nominatim's name ("Special Capital Region of Jakarta")
        city = artworks_about(names)                          # API 2: art made there, named in the title, or about it
        wider = None
        if here["country"] and here["country"] not in names:
            shown = {art["link"] for art in city[1]}
            wider = artworks_about([here["country"]], skip=shown)   # API 2 again, with API 1's country as input
    except requests.RequestException:
        return search_page(stateCode=typed, error="Something's down. Please try again in a few minutes.")
    return search_page(stateCode=typed, country=here["country"], city=city, wider=wider)


@app.route("/save", methods=["POST"])
def save():
    art = {key: request.form.get(key, "") for key in ["title", "artist", "made_in", "date", "image", "link"]}
    if art["link"]:
        add_to_lesson(art)
    return redirect("/lesson")                                # redirect, so a reload doesn't save twice


@app.route("/remove", methods=["POST"])
def remove():
    remove_from_lesson(request.form.get("link", ""))
    return redirect("/lesson")


@app.route("/lesson")
def lesson():
    return render_template("lesson.html", artworks=load_lesson())


if __name__ == "__main__":
    app.run(debug=True)
