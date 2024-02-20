from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return redirect(url_for("search"))

@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        d_search = request.form["search-bar"]
        return redirect(url_for("user", usr = d_search))
    if request.method == "GET":
        return render_template("search.html")

#@app.route("/<usr>")
#def user(usr):
#    return f"salut {usr}"


if __name__ == '__main__':
    app.run(debug=True)