from flask import Flask, render_template, request
import sqlite3
import os

app = Flask(__name__)


# --------------- DATABASE AUTO CREATE --------------- #
def init_db():
    if not os.path.exists("database.db"):
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        cur.execute("""
            CREATE TABLE contact (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                message TEXT NOT NULL
            )
        """)
        con.commit()
        con.close()
        print("Database created!")
    else:
        print("Database already exists.")

init_db()


# ---------------- ROUTES ---------------- #
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/insects")
def insects():
    return render_template("insects.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


# ---------- CONTACT FORM BACKEND ---------- #
@app.route("/submit_contact", methods=["POST"])
def submit_contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    if not name or not email or not message:
        return render_template("contact.html", msg="Please fill all fields!")

    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO contact (name, email, message) VALUES (?, ?, ?)",
                (name, email, message))
    con.commit()
    con.close()

    return render_template("contact.html", msg="Your message was sent successfully!")


# -------- INSECT DETAIL PAGES ---------- #
@app.route("/ant")
def ant_detail():
    return render_template("ant-detail.html")


@app.route("/bee")
def bee_detail():
    return render_template("bee-detail.html")


@app.route("/beetle")
def beetle_detail():
    return render_template("beetle-detail.html")


@app.route("/butterfly")
def butterfly_detail():
    return render_template("butterfly-detail.html")


# ---------------- RUN APP ---------------- #
if __name__ == "__main__":
    app.run(debug=True)
