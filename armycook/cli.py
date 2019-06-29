import click
import glob
import os
import datetime
import json

@click.command()
def cli():
    """Tweet"""
    # files = [f for f in glob.glob(path + "**/*.txt", recursive=True)]
    og_date_parts = os.environ['ORIGIN_DATE'].split(',')
    og_date_parts = list(map(lambda x: int(x), og_date_parts)) # string --> int
    og_date = datetime.datetime(og_date_parts[0], og_date_parts[1], og_date_parts[2])
    # click.echo(json.dumps(og_date.year))
    click.echo(json.dumps(getTweets()))

def getTweets():
    # load master.txt
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

