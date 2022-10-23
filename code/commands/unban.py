@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            embed = discord.Embed(colour = (clienthex),title = ('Banned'),description = (f'Unbanned {user}'), timestamp = (ctx.message.created_at))
            embed.set_author(name=f"{user}", icon_url=user.avatar.url)
            embed.set_thumbnail(url=user.avatar.url)
            await ctx.send(embed=embed)
            await ctx.message.delete()
            return
