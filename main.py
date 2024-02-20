from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return redirect(url_for("search"))

@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        d_search = request.form["search-bar"]
        return redirect(url_for("search_result", search_result=d_search))
    if request.method == "GET":
        return render_template("search.html")

@app.route("/<search_result>", methods=["GET", "POST"])
def search_result(search_result):
    if request.method == "POST":
        d_search = request.form["search-bar"]
        return redirect(url_for("search_result", search_result=d_search))
    if request.method == "GET":
        return render_template("search_result.html", search_result=search_result)
    

if __name__ == '__main__':
    app.run(debug=True)