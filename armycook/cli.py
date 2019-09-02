import click
import glob
import os
import datetime
import json
import random
import tweepy


@click.command()
def cli():
    """Tweet"""
    new_tweet = get_new_tweet()
    latest_tweet = get_latest_tweet()
    if (new_tweet[:50] == latest_tweet[:50]):
        click.echo('Trying to tweet same as latest tweet... Nope')
    else:
        click.echo('Sending new tweet: {}'.format(new_tweet))
        send_tweet(new_tweet)

def get_latest_tweet():
    api = get_twitter_api()
    tweets = api.home_timeline()
    return (tweets[0].text if len(tweets) > 0 else "")

def get_twitter_api():
    auth = tweepy.OAuthHandler(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'])
    auth.set_access_token(os.environ['ACCESS_TOKEN'], os.environ['ACCESS_TOKEN_SECRET'])
    return tweepy.API(auth)

def send_tweet(txt):
    api = get_twitter_api()
    api.update_status(txt)

def get_new_tweet():
    og_date_parts = os.environ['ORIGIN_DATE'].split(',')
    og_date_parts = list(map(lambda x: int(x), og_date_parts)) # string --> int
    og_date = datetime.datetime(og_date_parts[0], og_date_parts[1], og_date_parts[2])
    now = datetime.datetime.now()
    delta = now - og_date
    click.echo('Delta Days:' + str(delta.days))
    return get_tweets(delta.days)[delta.days]

def get_tweets(sd):
    master_txt = load_master_txt()
    sayings = load_sayings()
    random.seed(sd)
    get_random_saying = lambda: random.choice(sayings)
    return list(map(lambda x: get_tweet(x, get_random_saying), master_txt))

def get_tweet(txt, sayingFn):
    tweet = sayingFn()
    tweet = tweet.replace("$body", txt['body'])
    tweet = tweet.replace("$title", txt['title'])
    tweet = tweet + "\n\nsource: https://archive.org/details/1942TM10-405/"

    if(len(tweet) > 280):
        return get_tweet(txt, sayingFn)
    return tweet


def load_master_txt():
    """Load file containing text parts to be used in tweet"""
    if(os.environ.get('DEV_ENV', '') is "1"):
        txt_file = open("../master.txt", "r")
    else:
        txt_file  = open("/txts/master/master.txt", "r")
    txt = txt_file.read()
    txt_parts = txt.split('--')
    split_on_newline = lambda l: l.split("\n")
    non_empty = lambda s: len(s) > 0
    filter_nonempty = lambda ls: list(filter(non_empty, ls))
    break_apart_row = lambda row: {
        'title': filter_nonempty(split_on_newline(row))[0],
        'body': filter_nonempty(split_on_newline(row))[1]
    }

    txt_parts = list(map(break_apart_row, txt_parts))

    return txt_parts

def load_sayings():
    """Load txt file containing sayings part of the tweet"""
    if(os.environ.get('DEV_ENV', '') is "1"):
        txt_file  = open("../sayings.txt", "r")
    else:
        txt_file  = open("/txts/sayings/sayings.txt", "r")
    txt = txt_file.read()
    txt_parts = txt.split("\n")
    txt_parts = list(filter(lambda x: len(x) > 0, txt_parts))

    return txt_parts
