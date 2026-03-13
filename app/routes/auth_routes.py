from flask import Blueprint, render_template, request, redirect, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.user_model import create_user, get_user_by_email

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        user = get_user_by_email(email)

        if user and check_password_hash(user["password"], password):
            session["user_id"] = user["id"]
            session["user_name"] = user["name"]
            session["user_role"] = user["role"]
            flash("Login successful!", "success")
            return redirect("/")
        else:
            flash("Invalid email or password", "error")
            return redirect("/login")

    return render_template("login.html")


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        role = request.form.get("role", "patient")

        # Hash password
        hashed_password = generate_password_hash(password)

        try:
            create_user(name, email, hashed_password, role)
            flash("Registration successful! Please login.", "success")
            return redirect("/login")
        except Exception as e:
            flash("Registration failed. Email might already exist.", "error")
            return redirect("/register")

    return render_template("register.html")