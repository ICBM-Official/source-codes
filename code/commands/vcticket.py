@client.command(pass_context = True)
async def vcticket(ctx):
    await ctx.message.delete()
    tauth = ctx.message.author
    msg = await ctx.send('Creating Vc Ticket...')
    await asyncio.sleep(3)
    await msg.delete()
    guild = client.get_guild(tauth.guild.id)
    logs = discord.utils.get(guild.channels, name='ticket-logs')
    if logs == None:
        cat = await guild.create_category(name='Tickets')
        c = await cat.create_text_channel(name=f'ticket-logs', topic=('DO NOT EDIT THE NAME OF THIS CHANNEL'))
        await c.send('DO NOT EDIT THE NAME OF THIS CHANNEL, if you want it changed contact support')
        logs = discord.utils.get(guild.channels, name='ticket-logs')
    category = logs.category
    channel = await guild.create_voice_channel(name=f'{tauth.name} ticket', category=category)
    ibc = await channel.set_permissions(tauth, connect=True, speak=True)
    msg = await ctx.send(f'{tauth.mention} Someone will be with you shortly')
    msg2 = await ctx.send('The channel will delete when you leave')
    await asyncio.sleep(10)
    await msg.delete()
    await msg2.delete()

@client.event
async def on_voice_state_update(member, before, after):
    if member.guild.id == (1234567890):
        pass
    else:
        if before.channel is None:
            pass
        elif before.channel.name == (f'{member.name} ticket') and after.channel is None:
                channel = client.get_channel(before.channel.id)
                logs = discord.utils.get(member.guild.channels, name='ticket-logs')
                embed = discord.Embed(
                    colour = discord.Colour(clienthex),
                    title = (f'{channel.name} was closed by {member}'),
                )
                await logs.send(embed=embed)
                await channel.delete()
