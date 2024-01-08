def make_album(artist_name, album_title,number_of_songs = None):
    album = {
        'Artist Name': artist_name,
        'Album Name': album_title
    }
    if number_of_songs:
        album['Number of Songs'] = number_of_songs
    return album

print(make_album('Michael Jackson', 'Thriller',9))
print(make_album('The Beatles', 'Lonely Hearts Club Band',1))
print(make_album('Pink Floyd', 'The Dark Side Of The Moon'))