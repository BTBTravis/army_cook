import click
import glob
import os
import datetime
import json

@click.command()
def cli():
    """Example script."""
    # files = [f for f in glob.glob(path + "**/*.txt", recursive=True)]
    og_date_parts = os.environ['ORIGIN_DATE'].split(',')
    og_date_parts = list(map(lambda x: int(x), og_date_parts)) # string --> int
    og_date = datetime.datetime(og_date_parts[0], og_date_parts[1], og_date_parts[2])
    click.echo(json.dumps(og_date.year))
    # click.echo(og_date.year)
    # click.echo(og_date_parts[0])
