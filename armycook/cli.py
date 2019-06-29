import click
import glob
import os
import datetime
import json
import random

@click.command()
def cli():
    """Tweet"""
    # files = [f for f in glob.glob(path + "**/*.txt", recursive=True)]
    og_date_parts = os.environ['ORIGIN_DATE'].split(',')
    og_date_parts = list(map(lambda x: int(x), og_date_parts)) # string --> int
    og_date = datetime.datetime(og_date_parts[0], og_date_parts[1], og_date_parts[2])
    # click.echo(json.dumps(og_date.year))
    click.echo(json.dumps(get_tweets()))

def get_tweets():
    master_txt = load_master_txt()
    sayings = load_sayings()
    get_random_saying = lambda: random.choice(sayings)
    return list(map(lambda x: get_tweet(x, get_random_saying), master_txt))

def get_tweet(txt, sayingFn):
    tweet = sayingFn()
    tweet = tweet.replace("$body", txt['body'])
    tweet = tweet.replace("$title", txt['title'])
    if(len(tweet) > 280):
        return get_tweet(txt, sayingFn)
    return tweet


def load_master_txt():
    """Load file containing text parts to be used in tweet"""
    txt_file  = open("/army/master.txt", "r")
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
    txt_file  = open("/army/sayings.txt", "r")
    txt = txt_file.read()
    txt_parts = txt.split("\n")
    txt_parts = list(filter(lambda x: len(x) > 0, txt_parts))

    return txt_parts
