@client.group(pass_context=True)
@commands.has_permissions(ban_members=True)
async def find(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send_help(str(ctx.command))

@find.command(name="playing")
async def find_playing(ctx, *, search: str):
    result = [
        f"{i} | {i.activity.name}\r\n"
        for i in ctx.guild.members
        if (i.activity is not None)
        and (search.lower() in i.activity.name.lower())
        and (not i.bot)
    ]
    if result is None:
        return await ctx.send("Your search result was empty...")
    data = BytesIO("".join(result).encode("utf-8"))
    await ctx.send(
        content=f"Found **{len(result)}** on your search for **{search}**",
    )

@find.command(name="username", aliases=["name"])
async def find_name(ctx, *, search: str):
    result = [
        f"{i}\r\n" for i in ctx.guild.members if (search.lower() in i.name.lower())
    ]
    if result is None:
        return await ctx.send("Your search result was empty...")
    data = BytesIO("".join(result).encode("utf-8"))
    await ctx.send(
        content=f"Found **{len(result)}** on your search for **{search}**",
    )

@find.command(name="discriminator", aliases=["discrim"])
async def find_discriminator(ctx, *, search: str):
    result = [f"{i}\r\n" for i in ctx.guild.members if (search in i.discriminator)]
    if result is None:
        return await ctx.send("Your search result was empty...")
    data = BytesIO("".join(result).encode("utf-8"))
    await ctx.send(
        content=f"Found **{len(result)}** on your search for **{search}**",
    )
