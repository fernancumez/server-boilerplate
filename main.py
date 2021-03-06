
from flask import Flask, render_template, request, url_for, redirect
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/contact", methods=["POST"])
def contact():
    payload = {
      "name": request.form["name"],
      "email": request.form["email"],
      "description": request.form["description"],
    }

    file = open('data.txt', 'w')
    file.write(payload.__str__())
    file.close()

    return redirect(url_for('index'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host = '0.0.0.0', port = port)