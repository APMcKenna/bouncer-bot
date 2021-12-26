def validate_ping(ctx):
    """ Everyone is allowed to ping the bot except for the guest role. """
    if ctx.author.top_role.name == "Guest":
        return False
    return True
