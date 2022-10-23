@formexe.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def embed_format(ctx):
    msg = ("""Example: [prefix]embed title=test this | description=some words | colour=3AB35E | field=name=test value=test
You do NOT need to specify every property, only the ones you want.
**All properties and the syntax:**
- title=<words>
- description=<words>
- colour=<hex_value>
- image=<url_to_image> (must be https)
- thumbnail=<url_to_image>
- author=<words> **OR** author=name=<words> icon=<url_to_image>
- footer=<words> **OR** footer=name=<words> icon=<url_to_image>
- field=name=<words> value=<words> (you can add as many fields as you want)
- ptext=<words>
Force a field to go to the next line with the added parameter inline=False""")
    await ctx.send(msg)
