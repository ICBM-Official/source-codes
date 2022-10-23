@client.command(pass_context=True, aliases=['rc'])
@commands.has_permissions(manage_roles=True)
async def rolecolour(ctx, role: discord.Role):
    embed = discord.Embed(colour = (clienthex),description = (f'Please enter a hex colour:'), timestamp = (ctx.message.created_at))
    qul = await ctx.send(embed=embed)
    rel = await client.wait_for('message' ,check=(lambda message: message.author == ctx.message.author))
    if '#' in rel.content:
        colour = rel.content.split('#')
        nc = (colour[1])
        nnc = discord.Colour(int(f"0x{nc}", 16))
        await role.edit(color=discord.Colour(int(f"0x{nc}", 16)))
        embed = discord.Embed(colour = (clienthex), title = ('Role edit'), description = (f'Role {role} colour changed to {rel.content}'), timestamp = (ctx.message.created_at))
        await ctx.send(embed=embed)
        await ctx.message.delete()
