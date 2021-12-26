def validate_stop(ctx):
    """
    Only the Landlord role is allowed to stop the bot running.

    :param ctx:
    :return:
    """
    if ctx.author.top_role.name == "Landlord":
        return True
    return False
