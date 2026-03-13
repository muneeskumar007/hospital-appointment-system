

# from flask import Blueprint, render_template, request, redirect, session
# from app.services.db import mysql

# auth_bp = Blueprint("auth", __name__)

# @auth_bp.route("/login", methods=["GET","POST"])
# def login():

#     if request.method == "POST":

#         email = request.form["email"]
#         password = request.form["password"]

#         cur = mysql.connection.cursor()
#         cur.execute("SELECT * FROM users WHERE email=%s AND password=%s",(email,password))

#         user = cur.fetchone()

#         if user:
#             session["user_id"] = user[0]
#             session["role"] = user[4]

#             return redirect("/dashboard")

#     return render_template("login.html")

# @auth_bp.route("/register", methods=["GET","POST"])
# def register():

#     if request.method == "POST":

#         name = request.form["name"]
#         email = request.form["email"]
#         password = request.form["password"]

#         cur = mysql.connection.cursor()

#         cur.execute(
#         "INSERT INTO users(name,email,password,role) VALUES(%s,%s,%s,'patient')",
#         (name,email,password)
#         )

#         mysql.connection.commit()

#         return redirect("/login")

#     return render_template("register.html")


from flask import Blueprint, render_template, request, redirect, session
from app.services.db import mysql

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["GET","POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        cur = mysql.connection.cursor()
        cur.execute(
        "SELECT * FROM users WHERE email=%s AND password=%s",
        (email,password)
        )

        user = cur.fetchone()

        if user:
            session["user_id"] = user[0]
            return redirect("/dashboard")

    return render_template("login.html")


@auth_bp.route("/register", methods=["GET","POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        cur = mysql.connection.cursor()

        cur.execute(
        "INSERT INTO users(name,email,password,role) VALUES(%s,%s,%s,'patient')",
        (name,email,password)
        )

        mysql.connection.commit()

        return redirect("/login")

    return render_template("register.html")