@client.command()
async def itunesartist(ctx, *, artist):

    art = itunespy.search_artist(artist)
    albums = art[0].get_albums()
    tracks = []
    for album in albums:
        tracks.append(f"\n {album.collection_name}")


    final_string = ','.join(tracks)

    embed = discord.Embed(
        colour = (0xFFFFFF),
        timestamp=ctx.message.created_at,
        title = (f'{artist}'),
        description = (final_string),
    )
    embed.set_author(name='Albums', icon_url='https://cdn.discordapp.com/attachments/933743205810327572/967438209233584148/ITunes_12.2_logo.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/933743205810327572/967438209233584148/ITunes_12.2_logo.png')
    message = await ctx.send(embed=embed)

@client.command()
async def itunesalbum(ctx, *, album):
    al = itunespy.search_album(album)
    tracks = al[0].get_tracks()

    songs = []
    for track in tracks:
        songs.append(f"\n {track.artist_name} : {track.track_name}")

    length = ('Total playing time: ' + str(al[0].get_album_time()))

    final_string = ','.join(songs)

    embed = discord.Embed(
        colour = (0xFFFFFF),
        timestamp=ctx.message.created_at,
        title = (f'{album}'),
        description = (final_string),
    )
    embed.set_author(name='Songs', icon_url='https://cdn.discordapp.com/attachments/933743205810327572/967438209233584148/ITunes_12.2_logo.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/933743205810327572/967438209233584148/ITunes_12.2_logo.png')
    embed.set_footer(text=length)
    message = await ctx.send(embed=embed)


@client.command()
async def itunessong(ctx, *, song):
    track = itunespy.search_track(song)
    final_string = (track[0].artist_name + ': ' + track[0].track_name + ' | Length: ' + str(track[0].get_track_time_minutes()))

    embed = discord.Embed(
        colour = (0xFFFFFF),
        timestamp=ctx.message.created_at,
        title = (f'{song}'),
        description = (final_string),
    )
    embed.set_author(name='Song info', icon_url='https://cdn.discordapp.com/attachments/933743205810327572/967438209233584148/ITunes_12.2_logo.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/933743205810327572/967438209233584148/ITunes_12.2_logo.png')
    message = await ctx.send(embed=embed)
