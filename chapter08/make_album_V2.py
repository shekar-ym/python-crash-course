def make_album(artist_name, album_title):

    album = {
        'Artist Name': artist_name,
        'Album Name': album_title
    }
    print(album)

while True:
    print("Enter q to quit at any time. Now press Enter")

    artist_name = input("Enter artist name: ")
    if artist_name == 'q':
        break

    album_title = input("Enter album title: ")
    if album_title == 'q':
        break
    make_album(artist_name,album_title)
