import tweepy
from time import sleep
from credentials import *


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)



file = open('verne.txt', 'r')            # fichier texte
status = file.readlines()
file.close()

def tweet_line():                           # fonction
    for line in status:
        try:
            print(line)
            sleep(5)
            api.update_status(line)
            if line != '\n':               # passer les lignes blanches
                api.update_status(line)
            else:
                pass
        except tweepy.TweepError as e:
            if e.api_code == 187:
                print('Duplicate')
                sleep(5)
            elif e.api_code == 170:
                print('Blank')
                sleep(2)
            else:
                pass


tweet_line()











