@client.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def editembed(ctx, message : discord.Message , *, msg: str = None):
    if msg:
        if embed_perms(ctx.message):
            ptext = title = description = image = thumbnail = colour = footer = author = None
            timestamp = discord.Embed.Empty
            embed_values = msg.split('|')
            for i in embed_values:
                if i.strip().lower().startswith('ptext='):
                    ptext = i.strip()[6:].strip()
                elif i.strip().lower().startswith('title='):
                    title = i.strip()[6:].strip()
                elif i.strip().lower().startswith('description='):
                    description = i.strip()[12:].strip()
                elif i.strip().lower().startswith('desc='):
                    description = i.strip()[5:].strip()
                elif i.strip().lower().startswith('image='):
                    image = i.strip()[6:].strip()
                elif i.strip().lower().startswith('thumbnail='):
                    thumbnail = i.strip()[10:].strip()
                elif i.strip().lower().startswith('colour='):
                    colour = i.strip()[7:].strip()
                elif i.strip().lower().startswith('colour='):
                    colour = i.strip()[6:].strip()
                elif i.strip().lower().startswith('footer='):
                    footer = i.strip()[7:].strip()
                elif i.strip().lower().startswith('author='):
                    author = i.strip()[7:].strip()
                elif i.strip().lower().startswith('timestamp'):
                    timestamp = ctx.message.created_at
                else:
                    if description is None and not i.strip().lower().startswith('field='):
                        description = i.strip()

            if colour:
                if colour.startswith('#'):
                    colour = colour[1:]
                if not colour.startswith('0x'):
                    colour = '0x' + colour

            if ptext is title is description is image is thumbnail is colour is footer is author is None and 'field=' not in msg:
                await ctx.message.delete()
                return await ctx.send(content=None,
                                                   embed=discord.Embed(description=msg))

            if colour:
                em = discord.Embed(timestamp=timestamp, title=title, description=description, colour=int(colour, 16))
            else:
                em = discord.Embed(timestamp=timestamp, title=title, description=description)
            for i in embed_values:
                if i.strip().lower().startswith('field='):
                    field_inline = True
                    field = i.strip().lstrip('field=')
                    field_name, field_value = field.split('value=')
                    if 'inline=' in field_value:
                        field_value, field_inline = field_value.split('inline=')
                        if 'false' in field_inline.lower() or 'no' in field_inline.lower():
                            field_inline = False
                    field_name = field_name.strip().lstrip('name=')
                    em.add_field(name=field_name, value=field_value.strip(), inline=field_inline)
            if author:
                if 'icon=' in author:
                    text, icon = author.split('icon=')
                    if 'url=' in icon:
                        em.set_author(name=text.strip()[5:], icon_url=icon.split('url=')[0].strip(), url=icon.split('url=')[1].strip())
                    else:
                        em.set_author(name=text.strip()[5:], icon_url=icon)
                else:
                    if 'url=' in author:
                        em.set_author(name=author.split('url=')[0].strip()[5:], url=author.split('url=')[1].strip())
                    else:
                        em.set_author(name=author)

            if image:
                em.set_image(url=image)
            if thumbnail:
                em.set_thumbnail(url=thumbnail)
            if footer:
                if 'icon=' in footer:
                    text, icon = footer.split('icon=')
                    em.set_footer(text=text.strip()[5:], icon_url=icon)
                else:
                    em.set_footer(text=footer)
            await message.edit(content=ptext, embed=em)
        else:
            await ctx.send('No embed permissions in this channel.')
    else:
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
