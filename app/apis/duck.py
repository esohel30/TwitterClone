
import requests
import time

def get_duck():
    # Append a unique timestamp to the URL to prevent caching
    timestamp = int(time.time())
    link = f'https://picsum.photos/500?{timestamp}'
    return link
