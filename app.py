from flask import Flask, render_template, request, redirect, abort
import json
import string
import random
import os

app = Flask(__name__)

URLS_FILE = "urls.json"

def load_urls():
    if not os.path.exists(URLS_FILE):
        return {}
    with open(URLS_FILE, "r") as file:
        return json.load(file)
        

def save_urls(urls):
    with open(URLS_FILE, "w") as file:
        json.dump(urls, file, indent=4)
        

def generate_short_code(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))
    

@app.route("/", methods=["GET", "POST"])
def index():
    urls = load_urls()

    if request.method == "POST":
        long_url = request.form.get("long_url")

        # Generate unique short code
        short_code = generate_short_code()
        while short_code in urls:
            short_code = generate_short_code()

        urls[short_code] = long_url
        save_urls(urls)

        return render_template("index.html", short_url=short_code, urls=urls)

    return render_template("index.html", urls=urls)
    

@app.route("/<short_code>")
def redirect_url(short_code):
    urls = load_urls()
    long_url = urls.get(short_code)

    if long_url:
        return redirect(long_url)
    else:
        abort(404)
        

@app.route("/delete/<short_code>")
def delete_url(short_code):
    urls = load_urls()
    if short_code in urls:
        del urls[short_code]
        save_urls(urls)
    return redirect("/")



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
