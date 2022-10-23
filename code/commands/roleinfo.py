@client.command()
@commands.has_permissions(manage_messages=True)
async def roleinfo(ctx, guild=None, *, msg):
    if guild:
        guild, found = find_server(guild)
        if not found:
            return await ctx.send(guild)
        guild_roles = guild.roles
    else:
        guild = ctx.message.guild
        guild_roles = ctx.message.guild.roles
    for role in guild_roles:
        if msg.lower() == role.name.lower() or msg == role.id:
            all_users = [str(x) for x in role.members]
            all_users.sort()
            all_users = ', '.join(all_users)
            em = discord.Embed(title='Role Info', color=role.color)
            em.add_field(name='Name', value=role.name)
            em.add_field(name='ID', value=role.id, inline=False)
            em.add_field(name='Users in this role', value=str(len(role.members)))
            em.add_field(name='Role color hex value', value=str(role.color))
            em.add_field(name='Role color RGB value', value=role.color.to_rgb())
            em.add_field(name='Mentionable', value=role.mentionable)
            if len(role.members) > 10:
                em.add_field(name='All users', value=(len(role.members)), inline=False)
            elif len(role.members) >= 1:
                em.add_field(name='All users', value=all_users, inline=False)
            else:
                em.add_field(name='All users', value='There are no users in this role!', inline=False)
            em.add_field(name='Created at', value=role.created_at.__format__('%x at %X'))
            em.set_thumbnail(url='http://www.colorhexa.com/{}.png'.format(str(role.color).strip("#")))
            return await ctx.send(content=None, embed=em)
    await ctx.send('Could not find role ``{}``'.format(msg))
    await ctx.message.delete()
