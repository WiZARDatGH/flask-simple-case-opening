from flask import Flask, render_template, request, redirect, session, url_for
from dotenv import load_dotenv
import json
import os
import db
import functions

app = Flask(__name__)
load_dotenv()
app.secret_key= os.environ['SECRET_KEY']

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("username", "<empty>")
        password = request.form.get("password", "<empty>")

        if db.login(username, password):
            session["username"] = username
            return redirect(url_for("index"))
        else:
            return redirect(url_for("login"))

    elif request.method == 'GET':
        return render_template("login.html")

@app.route('/logout', methods=['GET'])
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))

@app.route('/open_case', methods=['POST'])
def open_case():
    try:
        data = request.get_json()
        caseId = data["case_id"]
        item= functions.openCase(caseId)
        return {"success": True, "case_id": caseId, "item": item['drop_item'], "ticket": item['ticket']}

    except Exception as e:
        return {"success": False, "case_id": caseId, "error": str(e)}, 400

    finally:
        print("kasa acma denemesi")


if __name__ == "__main__":
    app.run(debug=True)
