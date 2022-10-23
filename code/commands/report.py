@client.command(pass_context = True)
async def report(ctx):
    await ctx.message.delete()
    tauth = ctx.message.author
    msg = await ctx.send('Creating Report Ticket...')
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
    ulist = []
    for channel in category.channels:
        if channel.type is discord.ChannelType.voice:
            pass
        elif (channel.topic) == None:
            await channel.edit(topic=client.user.id)
            ulist.append(int(channel.topic))
        else:
            try:
                if int(channel.topic) == (tauth.id):
                    current = client.get_channel(channel.id)
                    ulist.append(int(channel.topic))
            except:
                pass
    i = (tauth.id)
    if i not in ulist:
        channel = await ctx.message.guild.create_text_channel(name=f'{tauth.name} report', topic=(tauth.id), category=category)
        msg = await channel.send(f'{tauth.mention} Someone will be with you shortly')
        msg = await channel.send('If you can send the users name or id and the evidence that would help us out. Thanks')
        ibc = await channel.set_permissions(tauth, read_messages=True, send_messages=True)
    else:
        await current.send(f'{tauth.mention} You already have a ticket')
