import click
from cmd_aliases import AliasedGroup, AliasConfig

AliasConfig.add_alias("helloworld", "welcome")  # set a single alias entry


@click.command(cls=AliasedGroup)
def cli():
    pass


@cli.command()
def HelloWorld():
    click.echo("Hello World!")


if __name__ == "__main__":
    cli()
