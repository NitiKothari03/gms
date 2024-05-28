from flask import Flask, render_template, request, redirect, url_for
from datetime import date

app = Flask(__name__)

# Define a list of members
members = [
    {
        'id': 1,
        'name': 'John Smith',
        'membership_type': 'Basic',
        'expiration_date': date(2022, 6, 30)
    },
    {
        'id': 2,
        'name': 'Jane Doe',
        'membership_type': 'Premium',
        'expiration_date': date(2023, 3, 31)
    },
    {
        'id': 3,
        'name': 'Bob Johnson',
        'membership_type': 'Basic',
        'expiration_date': date(2022, 12, 31)
    }
]

# Homepage
@app.route('/')
def index():
    return render_template('index1.html', members=members)

# View Members Page
@app.route('/view_members')
def view_members():
    return render_template('view_members.html', members=members)

# Add Member Page
@app.route('/add_member', methods=['GET', 'POST'])
def add_member():
    if request.method == 'POST':
        name = request.form['name']
        membership_type = request.form['membership-type']
        expiration_date = request.form['expiration-date']
        expiration_date = date.fromisoformat(expiration_date)
        new_member = {
            'id': len(members) + 1,
            'name': name,
            'membership_type': membership_type,
            'expiration_date': expiration_date
        }
        members.append(new_member)
        return redirect(url_for('view_members'))
    else:
        return render_template('add_member.html')

# Remove Member Page
@app.route('/remove_member', methods=['GET', 'POST'])
def remove_member():
    if request.method == 'POST':
        member_id = int(request.form['member-id'])
        for member in members:
            if member['id'] == member_id:
                members.remove(member)
                break
        return redirect(url_for('view_members'))
    else:
        return render_template('remove_member.html')

# Renew Membership Page
@app.route('/renew_membership', methods=['GET', 'POST'])
def renew_membership():
    if request.method == 'POST':
        member_id = int(request.form['member-id'])
        new_expiration_date = request.form['expiration-date']
        new_expiration_date = date.fromisoformat(new_expiration_date)
        for member in members:
            if member['id'] == member_id:
                member['expiration_date'] = new_expiration_date
                break
        return redirect(url_for('view_members'))
    else:
        return render_template('renew_membership.html')

if __name__ == '__main__':
    app.run(debug=True)
