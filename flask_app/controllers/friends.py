from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.friends import Friend


@app.route('/')
def home():
    friends_list= Friend.get_all_friends()
    return render_template('index.html', friends=friends_list)

@app.route('/about')
def about():
    return render_template('about.html')

# added for the form
@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')

@app.route('/project')
def project():
    return render_template('project.html')

@app.route('/login')
def login():
    return render_template('login.html')

# attach to register
@app.route('/create_friend', methods = ["POST"])
def create_friend():
    # create a dict with the data collected from the form
    data = {
        "first_name": request.form['fname'],
        "last_name": request.form['lname'],
        "occupation": request.form['occ'] 
    }

    Friend.save(data)
    return redirect('/')



# actions, show friend, edit friend
@app.route('/friend/details/<int:friend_id>')
def show_details(friend_id):
    data = {
        "id": friend_id
    }
    friend_details = Friend.get_one(data)
    return render_template('actions/details.html', details=friend_details)
# edit details
@app.route('/friend/edit/<int:friend_id>')
def edit_details(friend_id):
    data = {
        "id": friend_id
    }
    friend_details = Friend.get_one(data)
    return render_template('actions/edit.html', details=friend_details)

# update details
@app.route('/friend/update/', methods =['POST'])
def update_details():
    data = {
        "id": request.form["id"],
        "first_name": request.form["fname"],
        "last_name": request.form["lname"],
        "occupation": request.form["occ"]
    
    }
    Friend.update(data)
    return redirect('/')

@app.route('/friend/remove/<int:friend_id>')
def delete_friend(friend_id):
    data = {
        'id': friend_id
    }
    Friend.remove(data)
    return redirect('/')