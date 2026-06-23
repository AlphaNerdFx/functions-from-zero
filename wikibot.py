import click
from mylib.bot import scrape


@click.command()
@click.option("--name", help="Web page you want to scrape")
@click.option("--length", help="The length of the output from wikipedia")
def cli(name, length):
    result = scrape(name, length)
    click.echo(click.style(f"{result}"))


if __name__ == "__main__":
    cli()
