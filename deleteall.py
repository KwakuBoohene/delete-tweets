import io
import tweepy
import json


#Input the different keys from your twitter app over here
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

twitterid = []

def read_all(file):
# This function reads all twitter ids into a list
     rows = []
     with io.open(file, mode="r", encoding = 'utf-8') as jsfile:
          reader = json.loads(jsfile.read()[2:])
          for row in reader:
               rows.append(row["tweet"]['id'])
     return(rows)

read_all("tweet.js")

def readbyYear(file,year):
# This function reads all tweet ids from a particular year into a list
     rows = []
     with io.open(file,mode="r",encoding='utf-8') as jsfile:
          reader = json.loads(jsfile.read()[25:])
          for row in reader:
               if(str(year) in row["tweet"]["created_at"]):
                    rows.append(row["tweet"]["created_at"])
                    print(row["tweet"]["created_at"])
     return rows




def auth(consumer_key,consumer_secret):
# This function Authenticates with twitter using OAuth
     auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
     auth_url = auth.get_authorization_url()
     verify_code = input("Authenticate at %s and then enter you verification code here > " % auth_url)
     auth.get_access_token(verify_code)
     return tweepy.API(auth)

def main(consumer_k,consumer_s,access_k,access_s):
     # Aunthenticate user
     auth = tweepy.OAuthHandler(consumer_k, consumer_s)
     auth.set_access_token(access_k, access_s)
     api = tweepy.API(auth)
     print("Authenticated as: %s" % api.me().screen_name)

     # read all of the tweet ids into a variable:
     tweets = read_all("tweet.js")
     print('The tweets have been read from'+ ' tweet.js')
     print("Tweets Loaded")

     # Delete the tweets and print the results as tweets keep getting deleted
     delete_count = 0
     for tweet in tweets:
          try:
               api.destroy_status(tweet)
               print(tweet, 'deleted!')
               delete_count += 1
          except:
               print(tweet, 'could not be deleted.')
     print(delete_count, 'tweets deleted.')


#call to the code which runs the script in order

main(consumer_key,consumer_secret,access_key,access_secret)