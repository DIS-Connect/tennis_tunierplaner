from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "hallo"

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        mode = request.form.get('mode')
        session["mode"] = mode

        if mode == "1":
            return redirect("/zufaelliges_doppel")
        else:
            return redirect("/")

    #value 1 : zufälliges Doppel


@app.route('/zufaelliges_doppel', methods=["GET", "POST"])
def hello_zufaelliges_doppel():
    if request.method == "GET":
        return render_template("zufaelliges_doppel.html")
    elif request.method == "POST":
        spieler = request.form.get("spieler")
        session["spieler"] = spieler
        runden = request.form.get("runden")
        session["runden"] = runden

        return redirect("/spielplan")

@app.route('/spielplan', methods=["GET", "POST"])
def spielplan():
    return render_template("spielplan.html", mode=session["mode"], spieler=session["spieler"], runden=session["runden"])





if __name__ == '__main__':
    app.run(Debug=True)
