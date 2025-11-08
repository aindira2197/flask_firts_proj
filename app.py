from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    habar = "Bosh sahifa"
    return render_template("index.html", habar = habar)

@app.route("/about")
def about():
    mess = "Lorem ipsum bir narsala hullas"
    return render_template("about.html", mess = mess)

@app.route("/contact")
def contact():
    con = "+998 97 777 77 77 "
    return render_template("contact.html", con = con)

@app.route("/blog")
def blog():
    mess = "Bizni blogimz : "
    return render_template("blog.html", mess = mess)

if __name__ == "__main__":
    app.run(debug = True)
