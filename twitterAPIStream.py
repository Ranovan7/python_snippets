import json
import time
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

'''API key and token is stored in separate file as to keep it private'''
access_info = json.load(open("RanovanTwitterAPI.json"))

'''You guys use your own key and token ok'''
auth = OAuthHandler(access_info['consumer_key'], access_info['consumer_secret'])
auth.set_access_token(access_info['access_token'], access_info['access_token_secret'])

# api = tweepy.API(auth)

class Listener(StreamListener):
    """
    A listener handles tweets that are received from the stream.
    """

    def on_data(self, data):
        try:
            # convert the tweet data into json
            tweet = json.loads(data)

            # lets try printing it
            print(f"user : {tweet['user']['name']}")
            print(f"text : {tweet['text']}")
            print(f"language : {tweet['lang']}")
            print()
            return True
        except BaseException:
            # exception if the codes above got errors so it wont interrupt the stream
            print("Failed on Data\n")
            time.sleep(5)
            # iirc if you rerun the script in quick succession, twitter will
            # ban or stop you from streaming the tweets for some minutes
            # so the time.sleep above is needed

    def on_error(self, status):
        print("An Error Occurred")
        print(f"Status Code : {status}")
        return False


'''
Below is the code that runs the Stream
- First, initiate the Stream (object) using auth and the listener code as params
- Then set keywords to filter the tweets
'''
if __name__ == '__main__':
    l = Listener()

    stream = Stream(auth, l)
    stream.filter(track=['rocket', 'nasa', 'spacex'])
    
