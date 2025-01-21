import click
from config import config


class AliasedGroup(click.Group):
    """This subclass of a group supports looking up aliases in a config
    file and with a bit of magic. Adapted from Click's `aliases` example.
    See https://github.com/pallets/click/tree/main/examples/aliases.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.aliases = dict()

    def add_alias(self, alias, cmd_name):
        """
        Adds aliases to class-defined aliases variable.
        """
        self.aliases[cmd_name] = alias

    def set_aliases(self, aliases):
        """
        Sets aliases dictionary holistically.
        """
        try:
            if not isinstance(aliases, dict):
                raise TypeError(
                    "Expecting dict object as input, got {} instead.".format(
                        type(aliases).__name__
                    )
                )
            self.aliases = aliases
        except TypeError as e:
            pass

    def get_command(self, ctx, cmd_name):
        """
        Reads from `aliases.ini` file and loads aliases and their associated
        actual commands.
        """
        # Step one: builtin commands as normal
        rv = click.Group.get_command(self, ctx, cmd_name)
        if rv is not None:
            return rv

        # Step two: look up an explicit command alias in the config
        if cmd_name in self.aliases:
            actual_cmd = aliases[cmd_name]
            return click.Group.get_command(self, ctx, actual_cmd)

    def resolve_command(self, ctx, args):
        # always return the command's name, not the alias
        _, cmd, args = super().resolve_command(ctx, args)
        return cmd.name, cmd, args
