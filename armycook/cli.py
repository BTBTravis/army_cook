import click
import glob

@click.command()
def cli():
    """Example script."""
    # files = [f for f in glob.glob(path + "**/*.txt", recursive=True)]
    click.echo('Test')

