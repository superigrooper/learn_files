# albums
def make_albums(artist, album, tracks=None):
    info = {'artist' : artist, 'album' : album}
    if tracks:
        info['tracks'] = tracks
    return info

while True:
    print("\nМузыкальные альбомы.")
    print("(для завершения нажмите 'q')")

    artist = input("Введи исполнителя: ")
    if artist == 'q':
        break

    album = input("Введи название альбома: ")
    if album == 'q':
        break

    tracks = input("Кол-во песен: (необязательно)")
    if tracks == 'q':
        break

    print(make_albums(artist, album, tracks))