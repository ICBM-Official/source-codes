@client.command(pass_context=True)
async def userinfo(ctx, member : discord.Member = None):
    member = ctx.message.author if not member else member
    roles=[role for role in member.roles]
    perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in member.guild_permissions if p[1]])
    voice_state = None if not member.voice else member.voice.channel

    roles = []
    for role in member.roles:
        roles.append(role)

    embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)
    embed.set_author(name=f"User Info - {member}", icon_url=member.avatar.url)
    embed.set_thumbnail(url=member.avatar.url)
    embed.set_footer(text=f"Requested by {ctx.message.author}")
    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="User name:", value=member.display_name)
    embed.add_field(name='Nickname', value=member.nick)
    embed.add_field(name='Status', value=member.status)
    embed.add_field(name='In Voice', value=voice_state)
    embed.add_field(name='Game', value=member.activity)
    embed.add_field(name="Created at:", value=member.created_at.strftime("%a, %d %B %Y, %I:%M %p GMT"))
    embed.add_field(name="Joined at:", value=member.joined_at.strftime("%a, %d %B %Y, %I:%M %p GMT"))
    members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
    embed.add_field(name="Join position", value=str(members.index(member)+1))
    embed.add_field(name="Top role:", value=member.top_role.mention)
    embed.add_field(name="Bot?", value=member.bot)
    embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]), inline=False)
    embed.add_field(name="Guild permissions", value=perm_string, inline=False)

    await ctx.send(embed=embed)
    await ctx.message.delete()
