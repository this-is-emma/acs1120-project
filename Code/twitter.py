import dotenv
import os
dotenv.load_dotenv('.env')
from requests_oauthlib import OAuth1Session

consumer_key = os.environ.get('TWITTER_CONSUMER_KEY')
consumer_secret = os.environ.get('TWITTER_CONSUMER_SECRET')
access_token = os.environ.get('TWITTER_ACCESS_TOKEN')
access_token_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')


session = OAuth1Session(consumer_key,
                      client_secret=consumer_secret,
                      resource_owner_key=access_token,
                      resource_owner_secret=access_token_secret)

# The URL endpoint to update a status (i.e. tweet)
url = 'https://api.twitter.com/2/tweets'

# The contents of status (i.e. tweet text)
status = 'If you are reading this on Twitter, the API request worked!'

# Send a POST request to the url with a 'status' parameter
resp = session.post(url, json={ 'text': status })

# Show the text from the response
print(resp.text)

def tweet(status):
    resp = session.post(url, json={ 'text': status })
    return resp.text
