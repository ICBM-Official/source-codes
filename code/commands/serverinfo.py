@client.command(name="serverinfo", aliases=["guildinfo", "si", "gi"])
async def server_info(ctx):
    embed = discord.Embed(title="Server information",
    			  colour=ctx.guild.owner.colour,
                  timestamp = (ctx.message.created_at),
    )

    embed.set_thumbnail(url=ctx.guild.icon.url)

    statuses = [len(list(filter(lambda m: str(m.status) == "online", ctx.guild.members))),
    			len(list(filter(lambda m: str(m.status) == "idle", ctx.guild.members))),
    			len(list(filter(lambda m: str(m.status) == "dnd", ctx.guild.members))),
    			len(list(filter(lambda m: str(m.status) == "offline", ctx.guild.members)))]

    fields = [("ID", ctx.guild.id, True),
    		  ("Owner", ctx.guild.owner, True),
    		  ("Region", ctx.guild.region, True),
    		  ("Created at", ctx.guild.created_at.strftime("%d/%m/%Y %H:%M:%S"), True),
    		  ("Members", len(ctx.guild.members), True),
    		  ("Humans", len(list(filter(lambda m: not m.bot, ctx.guild.members))), True),
    		  ("Bots", len(list(filter(lambda m: m.bot, ctx.guild.members))), True),
    		  ("Banned members", len(await ctx.guild.bans()), True),
    		  ("Statuses", f"🟢 {statuses[0]} 🟠 {statuses[1]} 🔴 {statuses[2]} ⚪ {statuses[3]}", True),
    		  ("Text channels", len(ctx.guild.text_channels), True),
    		  ("Voice channels", len(ctx.guild.voice_channels), True),
    		  ("Categories", len(ctx.guild.categories), True),
    		  ("Roles", len(ctx.guild.roles), True),
    		  ("Invites", len(await ctx.guild.invites()), True),
    		  ("\u200b", "\u200b", True)]

    for name, value, inline in fields:
        embed.add_field(name=name, value=value, inline=inline)

    await ctx.send(embed=embed)
    await ctx.message.delete()
