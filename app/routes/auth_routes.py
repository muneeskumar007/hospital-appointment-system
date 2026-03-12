from flask import Blueprint, render_template, request, redirect, session
from app.services.auth_service import register_user, login_user

auth_bp = Blueprint("auth",__name__)


@auth_bp.route("/register",methods=["GET","POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        role = request.form["role"]

        register_user(name,email,password,role)

        return redirect("/login")

    return render_template("register.html")



@auth_bp.route("/login",methods=["GET","POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        user = login_user(email,password)

        if user:
            session["user_id"] = user["id"]
            session["role"] = user["role"]

            return redirect("/")

        return "Invalid email or password"

    return render_template("login.html")



@auth_bp.route("/logout")
def logout():

    session.clear()

    return redirect("/login")