from flask import Flask, render_template, request, redirect, session, jsonify
from models.user_model import check_user
from models.post_model import *

app = Flask(__name__)
app.secret_key = "dev_secret_key"


# ---------------- LOGIN ----------------
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user_id = request.form["id"]
        pw = request.form["pw"]

        user = check_user(user_id, pw)

        if user:
            session["user"] = user_id
            return redirect("/board")

        return "Login Failed"

    return render_template("index.html")


# ---------------- BOARD PAGE ----------------
@app.route("/board")
def board():
    if "user" not in session:
        return redirect("/")

    posts = get_posts()
    return render_template("board.html", posts=posts, user=session["user"])


# ---------------- AJAX CREATE POST ----------------
@app.route("/api/post", methods=["POST"])
def api_post():
    if "user" not in session:
        return jsonify({"status": "fail"})

    data = request.json
    insert_post(data["title"], data["content"], session["user"])

    return jsonify({"status": "success"})


# ---------------- DELETE ----------------
@app.route("/delete/<int:idx>")
def delete(idx):
    delete_post(idx)
    return redirect("/board")


# ---------------- EDIT ----------------
@app.route("/edit/<int:idx>", methods=["GET", "POST"])
def edit(idx):
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        update_post(idx, title, content)
        return redirect("/board")

    post = get_post(idx)
    return render_template("edit.html", post=post)


# ---------------- LOGOUT ----------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)