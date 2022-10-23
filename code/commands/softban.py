@client.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def softban(ctx, user : discord.Member, *, reason=None):
    if ctx.author.top_role > user.top_role or ctx.author == ctx.guild.owner:
        if user == ctx.author:
            return await ctx.send("***You can't softban yourself...***")
        await user.ban(reason=reason)
        await user.unban(reason=reason)
        embed = discord.Embed(colour = (clienthex),title = ('Softban'),description = (f'{user} was softbanned'), timestamp = (ctx.message.created_at))
        embed.set_author(name=f"{user}", icon_url=user.avatar.url)
        embed.set_thumbnail(url=user.avatar.url)
        embed.add_field(name='Reason', value=(f"""{reason}"""), inline=False)
        await ctx.send(embed=embed)
        await ctx.message.delete()
