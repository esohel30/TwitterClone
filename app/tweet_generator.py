from apis import duck, uselessfacts
import db
import random

def generate_pfp():
    pfp = duck.get_duck()
    return pfp

def generate_content():
    return uselessfacts.get_fact()

def generate_tweet(username, name):
    # generates an random tweet that is meant to simulate tweets from the outside world
    db.tweet_table_init()
    db.create_tweet(generate_pfp(), username, name, generate_content(), random.randint(1,1000))

def generate_user_tweet(pfp, username, name, content):
    # used to generate a new tweet where the user decides what the content is
    db.tweet_table_init()
    db.create_tweet(pfp, username, name, content, 0)

def return_tweets():
    return db.return_tweets()





    




