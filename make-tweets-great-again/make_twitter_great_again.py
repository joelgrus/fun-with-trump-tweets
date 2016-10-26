from twython import Twython
from twython.exceptions import TwythonError
import json, os, re

with open('credentials.json') as f:
    creds = json.loads(f.read())

client = Twython(
    creds['consumer_key'],
    creds['consumer_secret'],
    creds['access_token_key'],
    creds['access_token_secret']
)

query = 'make "great again" -america -filter:retweets'
rgx = r"make (.*) great again"

results = client.search(q=query)
for tweet in results["statuses"]:
  text = tweet["text"]
  if re.search(rgx, text, re.I):
    # twitter.retweet will raise an error if we try to retweet a tweet
    # that we've already retweeted.
    print(json.dumps(tweet, indent=4))
    try:
      #client.retweet(id=tweet["id"])
      break
    except TwythonError as e:
      print(e)
