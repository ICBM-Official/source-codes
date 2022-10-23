@client.command(pass_context=True, aliases=["calculate"])
async def calc(ctx, *, msg):
    equation = msg.strip().replace('^', '**').replace('x', '*')
    try:
        if '=' in equation:
            left = eval(equation.split('=')[0], {"__builtins__": None}, {"sqrt": sqrt})
            right = eval(equation.split('=')[1], {"__builtins__": None}, {"sqrt": sqrt})
            answer = str(left == right)
        else:
            answer = str(eval(equation, {"__builtins__": None}, {"sqrt": sqrt}))
    except TypeError:
        return await ctx.send("Invalid calculation query.")

    em = discord.Embed(color=clienthex, title='Calculator')
    em.add_field(name='Input:', value=msg.replace('**', '^').replace('x', '*'), inline=False)
    em.add_field(name='Output:', value=answer, inline=False)
    await ctx.send(content=None, embed=em)
    await ctx.message.delete()
