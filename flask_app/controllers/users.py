from flask_app import app
from flask import Flask, session, redirect, render_template, request
from flask_app.models.user import Users

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
    show_user = Users.save(data)
    return redirect(f"/user/show/{show_user}")

@app.route("/user/show/<int:id>")
def display_one(id):
    data = {"id":id}
    return render_template("readone.html", user= Users.get_one(data))

@app.route("/display_users")
def display_all():
    return render_template("read.html", all_users = Users.get_all())

@app.route("/user/edit_page/<int:id>" )
def edituser(id):
    data = {"id":id}
    return render_template("edit.html", user = Users.get_one(data))

@app.route("/user/edit", methods=['POST'])
def edit_page():
    updated_user = request.form["id"]
    Users.update(request.form)
    return redirect(f"/user/show/{updated_user}")

@app.route("/user/delete/<int:id>")
def goodbye(id):
    Users.delete(id)
    return redirect("/display_users")

