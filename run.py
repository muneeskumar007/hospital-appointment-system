from flask import Flask, render_template, request, redirect, session
from app.routes.auth_routes import auth_bp

app = Flask(__name__, template_folder="app/templates", static_folder="app/static")
app.secret_key = "secret123"

# register blueprint
app.register_blueprint(auth_bp)

# temporary doctors data
doctors = [
{"id":1,"name":"Sarah Jenkins","specialty":"Cardiology","experience":12},
{"id":2,"name":"James Wilson","specialty":"Pediatrics","experience":8},
{"id":3,"name":"Elena Rodriguez","specialty":"Dermatology","experience":15},
{"id":4,"name":"Michael Chang","specialty":"Neurology","experience":20}
]

appointments = []


@app.route("/")
def home():

    specialty = request.args.get("specialty")

    if specialty:
        filtered = [d for d in doctors if d["specialty"] == specialty]
    else:
        filtered = doctors

    return render_template("index.html", doctors=filtered)


@app.route("/doctor/<int:id>")
def doctor_page(id):

    doctor = next(d for d in doctors if d["id"] == id)

    return render_template("doctor.html", doctor=doctor)


@app.route("/book/<int:id>")
def book(id):

    if "user" not in session:
        return redirect("/login")

    doctor = next(d for d in doctors if d["id"] == id)

    token = len(appointments) + 1

    appointments.append({
        "token": token,
        "doctor": doctor["name"],
        "user": session["user"]
    })

    return render_template("token.html", token=token, doctor=doctor)


if __name__ == "__main__":
    app.run(debug=True)