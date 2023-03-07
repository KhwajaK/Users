from flask import Flask, session, redirect, render_template, request
from user import Users

app = Flask (__name__)

@app.route("/")
def index():
    return render_template("create.html")

@app.route('/input_user', methods=["POST"])
def input():
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email": request.form["email"]
    }
    Users.save(data)
    return redirect("/display_users")

@app.route("/display_users")
def display():
    all_users = Users.get_all()
    return render_template("/read.html", all_users=all_users)


if __name__=="__main__":
    app.run(port=8000,debug=True)
