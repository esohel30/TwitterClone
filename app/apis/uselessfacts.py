import requests

def fact_jsonify():
    link = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"
    return requests.get(link).json()

def get_fact():
    json = fact_jsonify()
    return json['text']


# print(get_fact())