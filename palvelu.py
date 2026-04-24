from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_wolrd():
    return "<p> Hello, cruel World! </p>"

@app.route("/tulos")
def nayta_tulos():
    luku1 = request.args.get("luku1")
    luku2 = request.args.get("luku2")
    return "Näiden lukujen summa on %s" % (float(luku1) + float(luku2))

@app.route("/seikkailu")
def nayta_laatikko_sivu():
    return """

    <p>Laita tähän kaksi lukua:
    <form action="/tulos" enctype="application/x-www-urlencoded">
    Eka luku: <input name=luku1 type=text <br>
    Toka luku: <input name=luku2 type=text <br>
    <input type=submit value="Tee jotain">
    </form>    
        

"""

if __name__ == "__main__":
    app.run(debug=True)