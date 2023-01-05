# exercise 9.3.1 from unit 9
'''
Write a function called my_mp3_playlist defined as follows:

def my_mp3_playlist(file_path):
The function accepts as a parameter a path to the file (string).
The file represents a playlist of songs and has a fixed format consisting of the name of the song, the name of the performer (singer/band) and the length of the song, separated by a semicolon (;) without spaces.

An example of an input file called songs.txt:

Tudo Bom; Static and Ben El Tavori; 5:13;
I Gotta Feeling; The Black Eyed Peas; 4:05;
Instrumental; Unknown; 4:15;
Paradise; Coldplay; 4:23;
Where is the love?; The Black Eyed Peas; 4:13;
The function returns a tuple in which:

The first member is a string representing the name of the longest song in the file 
(it means the longest song, assume all lengths are different).
The second member is a number representing the number of songs the file contains.
The third member is a string representing the name of the operation that appears in
the file the largest number of times (assume there is only one).
An example of running the my_mp3_playlist function on the songs.txt file
>>> print(my_mp3_playlist(r"c:\my_files\songs.txt"))
("Tudo Bom", 5, "The black Eyed Peas")
'''
def my_mp3_playlist(file_path):
    longest_song = ""
    longest_song_length = 0
    song_count = 0
    most_common_artist = ""
    artist_counts = {}

    with open(file_path, 'r') as f:
        for line in f:
            song, artist, length = line.strip().split(';')
            length_parts = length.split(':')
            length_minutes = int(length_parts[0])
            length_seconds = int(length_parts[1])
            total_length = length_minutes * 60 + length_seconds

            if total_length > longest_song_length:
                longest_song = song
                longest_song_length = total_length

            if artist in artist_counts:
                artist_counts[artist] += 1
            else:
                artist_counts[artist] = 1

            song_count += 1

    most_common_artist = max(artist_counts, key=artist_counts.get)

    return (longest_song, song_count, most_common_artist)

def main():
    result = my_mp3_playlist(r"c:\my_files\songs.txt")
    print(result)

if __name__ == "__main__":
    main()
