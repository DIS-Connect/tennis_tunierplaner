from flask import Flask, render_template, request, redirect, session
import logic

app = Flask(__name__)
app.secret_key = "hallo"


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":

        if request.form["spieler"] == "":
            return redirect("/")



        mode = request.form.get('mode')
        session["mode"] = mode

        session["spieler"] = request.form.get("spieler")

        if not mode == "3":
            if request.form["runden"] == "":
                return redirect("/")
            session["runden"] = request.form.get("runden")
            print(session["runden"])

        elif mode == "4":
            session["fields"] = request.form.get("fields")


        if mode == "1":
            return redirect("/names_doppel")
        elif mode == "2":
            return redirect("/names_einzel")
        elif mode == "3":
            return redirect("/names_einzel")
        elif mode == "4":
            return redirect("/names_einzel")


    # value 1 : zufälliges Doppel


@app.route('/names_doppel', methods=["GET", "POST"])
def names_doppel():
    if request.method == "GET":
        print(session["spieler"])
        if int(session["spieler"]) % 2 == 0:
            player_a = player_b = int(int(session["spieler"]) / 2)
        else:
            player_a = int(int(session["spieler"]) / 2) + 1
            player_b = int(int(session["spieler"]) / 2)

        session["player_a"] = player_a
        session["player_b"] = player_b
        return render_template("names_doppel.html", player_a=player_a, player_b=player_b)
    elif request.method == "POST":

        gruppe_a = []
        gruppe_b = []
        for player in request.form:
            if player.startswith('player_a'):
                gruppe_a.append(request.form[player])
            else:
                gruppe_b.append(request.form[player])

        session["gruppe_a"] = gruppe_a
        session["gruppe_b"] = gruppe_b
        return redirect("/spielplan_erstellen")


@app.route('/names_einzel', methods=["GET", "POST"])
def names_einzel():
    if request.method == "GET":
        return render_template("names_einzel.html", spieler=int(session["spieler"]))
    elif request.method == "POST":
        player_list = []
        for player in request.form:
            player_list.append(request.form[player])

        session["player_list"] = player_list
        return redirect("/spielplan_erstellen")


@app.route('/spielplan_erstellen')
def spielplan_erstellen():
    print("spielplan erstellen")
    runden = int(session["runden"])
    spieler = int(session["spieler"])
    mode = session["mode"]

    if mode == "1":
        session["plan"] = logic.spielplan_doppel(runden, session["gruppe_a"], session["gruppe_b"])
    elif mode == "2":
        print(session["player_list"])
        session["plan"] = logic.runden_einzel(session["player_list"], session["runden"])
    elif mode == "3":
        print(session["player_list"])
        session["plan"] = logic.jeder_gegen_jeden(session["player_list"])
    elif mode == "4":
        print(session["runden"])
        session["plan"] = logic.limited_fields(session["player_list"], session["runden"], session["fields"])
        print(session["plan"])

    return redirect("/spielplan")


@app.route('/spielplan')
def spielplan():
    print("spielplan wird ausgedruckt")
    return render_template("spielplan.html", plan=session["plan"])


if __name__ == '__main__':
    app.run(debug=True)
