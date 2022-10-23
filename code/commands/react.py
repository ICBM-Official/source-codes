@client.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def react(ctx, message : discord.Message, *, arg):
    await message.add_reaction(arg)
    await ctx.message.delete()
