import sqlite3

DB_file = "data.db"
db = None

def db_connect():
    global db
    db = sqlite3.connect(DB_file)
    return db.cursor()

def db_close():
    db.commit()
    db.close()

def tweet_table_init():
    '''
    Tweet Components:
    1) Profile Picture
    2) Username
    3) Name
    4) Tweet content
    4) Likes
    '''
    c =  db_connect()
    c.execute("CREATE TABLE IF NOT EXISTS tweets (pfp text, username text, name text, content text, likes int)")
    db_close()

def create_tweet(pfp, username, name, content, likes):
    tweet_table_init() # make sure table exists
    c = db_connect()
    c.execute('INSERT INTO tweets VALUES (?, ?, ?, ?, ?)', (pfp, username , name , content , likes))
    db_close()

def return_tweets():
    c = db_connect()
    c.execute("SELECT * FROM tweets")
    retVal = c.fetchall()
    db_close()
    return retVal

def db_user_init():
    c = db_connect()
    c.execute("CREATE TABLE IF NOT EXISTS users (username text, password text, name text)")
    db_close()

## Refactored from project p00 by Rice Explosion (Nakib Abedin, Donald Bi, Wilson Mach)

def check_user_not_exists(username): #checks if user doesn't exist, returns True if they don't exist
    db_user_init() # make sure table exists
    c = db_connect()
    c.execute('SELECT username FROM users WHERE username=?',(username,))
    user = c.fetchone()
    db_close()
    if user:
        return False
    return True

#for signing up
def create_new_user(username, password, name): #creates new user
    c = db_connect()
    c.execute('INSERT INTO users VALUES (?,?,?)',(username, password, name))
    c.execute("SELECT * from users")
    db_close()

#for logging in
def check_credentials(username, password): #checks if there exists username and password in db, returns True if there is
    c = db_connect()
    c.execute('SELECT username,password FROM users WHERE username=? AND password=?',(username, password))
    user = c.fetchone()
    db_close()
    if user:
        return True
    return False

#given username, returns name
def get_name(username):
    c = db_connect()
    c.execute('SELECT name FROM users WHERE username=?', (username,))
    user = c.fetchone()
    db_close()
    return user[0]






