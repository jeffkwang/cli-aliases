import click
import cmd_aliases

AliasedGroup = cmd_aliases.AliasedGroup()
AliasedGroup.add_alias("welcome", "Hello World!")


@click.command(cls=AliasedGroup)
def cli():
    pass


@cli.command()
def HelloWorld():
    click.echo("Hello World!")


if __name__ == "__main__":
    cli()
