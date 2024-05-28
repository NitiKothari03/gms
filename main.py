from flask import Flask, render_template, request

app = Flask(__name__)

members = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/view_members")
def view_members():
  return render_template("view_members.html", members=members)

@app.route("/add_member", methods=["GET", "POST"])
def add_member():
    if request.method == "POST":
        name = request.form["name"]
        membership_type = request.form["membership_type"]
        expiration_date = request.form["expiration_date"]
        members.append({"name": name, "membership_type": membership_type, "expiration_date": expiration_date})
        return render_template("add_member_success.html")
    else:
        return render_template("add_member.html")

@app.route("/remove_member", methods=["GET", "POST"])
def remove_member():
    if request.method == "POST":
        id = request.form["id"]
        for member in members:
            if str(member["id"]) == id:
                members.remove(member)
                return render_template("remove_member_success.html")
        return render_template("remove_member_fail.html")
    else:
        return render_template("remove_member.html")

@app.route("/renew_membership", methods=["GET", "POST"])
def renew_membership():
    if request.method == "POST":
        id = request.form["id"]
        new_expiration_date = request.form["expiration_date"]
        for member in members:
            if str(member["id"]) == id:
                member["expiration_date"] = new_expiration_date
                return render_template("renew_membership_success.html")
        return render_template("renew_membership_fail.html")
    else:
        return render_template("renew_membership.html")

if __name__ == "main":
    app.run(debug=True)
