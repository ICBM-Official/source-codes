@client.command()
async def youtube(ctx, *, search):
    def search_yt(item):
        with YoutubeDL(YDL_OPTIONS) as ydl:
            print(item)
            try:
                info = ydl.extract_info((f"ytsearch:{item}"), download=False)[
                    "entries"
                ][0]

            except Exception:
                return False
        return {
            "video": info["webpage_url"],
            "thumbnail": info["thumbnail"],
            "channel": info["channel"],
            "title": info["title"],
            "desc": info["description"],
            "song_length": info["duration"],
            "date": info["upload_date"],
        }
    song = search_yt(search)
    def convert(seconds):
        seconds = seconds % (24 * 3600)
        hour = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60

        return "%d:%02d:%02d" % (hour, minutes, seconds)
    title = (f"""{song['title']}""")
    channel = (f"""{song['channel']}""")
    url = (f"""{song['video']}""")
    img = (f"""{song['thumbnail']}""")
    date = (f"""{song['date']}""")
    year = date[:4]
    month = date[4:6]
    day = date[6:8]
    length = (convert(song['song_length']))
    embed = discord.Embed(colour=0xFF0000, timestamp=ctx.message.created_at, title=channel, description=f'**__[{title}]({url})__**')
    embed.set_author(name=f"Youtube Search", icon_url="https://cdn.discordapp.com/attachments/730456139111858336/910899014726221844/youtube-logo-hd-8.png")
    embed.set_thumbnail(url=img)
    embed.set_image(url=img)
    embed.set_footer(text=f"{ctx.message.author}")
    embed.add_field(name="Video length", value=length, inline=True)
    embed.add_field(name="Date", value=f'{day}/{month}/{year}', inline=True)
    message = await ctx.send(embed=embed)
