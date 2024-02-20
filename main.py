from flask import Flask, redirect, url_for, render_template, request, supabase

#Supabase Connect
url = "https://tgwcszwdpjqtjpfpwici.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRnd2NzendkcGpxdGpwZnB3aWNpIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDg0NTMwNTUsImV4cCI6MjAyNDAyOTA1NX0.cjLfWVaFISUk2-DKdfFV1R7Evv-zlqQDBbdVpl29QWo"
supabase = supabase.create_client(url, key)
response = supabase.table("furnizori").select("*").execute()

#MAIN FLASK APP
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