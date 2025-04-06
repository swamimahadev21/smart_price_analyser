
from flask import Flask, render_template, request
from app.main import analyze_price

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    results = None
    if request.method == "POST":
        product = request.form.get("product")
        results = analyze_price(product)
    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)
