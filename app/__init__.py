from flask import Flask, render_template, request, redirect, session
from flask_socketio import SocketIO, send, emit
import tweet_generator
import db

app = Flask(__name__)

## Setup secret key for session
secret_key_file = open("keys/app_secret_key.txt", "r")
secret_key = secret_key_file.read()
app.secret_key = secret_key
secret_key_file.close()

## Setup Socket
socketio = SocketIO(app)

# Consulted Primary Documentation --> https://flask-socketio.readthedocs.io/en/latest/

# @socketio.on('disconnect')
# def handle_disconnect():
#     print('Client disconnected')

@socketio.on('join')
def handle_join(data):
    # username = data['username']
    join_message = f'{session["name"]} has joined the chat'
    emit('new_message', {'username': 'ChatBot', 'message': join_message}, broadcast=True)

@socketio.on('send_message')
def handle_message(data):
    username = session['username']
    message = data['message']
    emit('new_message', {'username': username, 'message': message}, broadcast=True)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/signin', methods=["GET", "POST"])
def signin():
    if(db.check_credentials(request.form['username'], request.form['password'])):
        session['username'] = request.form['username']
        session['name'] = db.get_name(request.form['username'])
        session['pfp'] = tweet_generator.generate_pfp()
        return redirect("/explore")
    else:
        return render_template('login.html', error = 'login')

@app.route('/explore')
def explore():
    if("referrer" in session):
        referrer = session['referrer']
        del session['referrer']
        if (referrer == 'create_tweet'):
            tweets = tweet_generator.return_tweets()
            return render_template('index.html', data=tweets)
        
    tweet_generator.generate_tweet("Ericsohel", "Eric Sohel")
    tweets = tweet_generator.return_tweets()
    
    return render_template('index.html', data=tweets)

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/newaccount', methods=["POST"])
def newaccount():

    # store the username and password
    username = request.form["username"]
    password = request.form["password"]
    name = request.form["name"]

    db.db_user_init()
    if(not (db.check_user_not_exists(username)) ):
        #if username exists, block
        return render_template('signup.html', error = 'signup')
    else:
        db.create_new_user(username, password, name)
        return redirect("/")

@app.route('/logout', methods=["POST"])
def logout():
    session.pop('username')
    return redirect("/")

@app.route("/create_tweet", methods=['POST'])
def create_tweet():

    #the following will be used in order to ensure that the user generated tweet is 
    #at the top of the sequence of tweets
    session["referrer"] = "create_tweet"
    
    
    username = session['username']
    name = session['name']
    content = request.form['content']    
    pfp = session['pfp']

    tweet_generator.generate_user_tweet(pfp, username, name, content)

    return redirect("/explore")

@app.route("/chat")
def chat():
    return render_template("chat.html")


if __name__ == '__main__':
    app.debug = True
    # app.run()
    socketio.run(app)
