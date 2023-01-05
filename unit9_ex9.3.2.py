# exercise 9.3.2 from unit 9 
'''
def my_mp4_playlist(file_path, new_song):
The function accepts as parameters:

Path to the file (string).
Just like in the previous exercise, the file represents a playlist of songs and has a fixed format built from the name of the song, the name of the performer (singer/band) and the length of the song, separated by a semicolon (;) without spaces.

An example of an input file called songs.txt:
Tudo Bom; Static and Ben El Tavori; 5:13;
I Gotta Feeling; The Black Eyed Peas; 4:05;
Instrumental; Unknown; 4:15;
Paradise; Coldplay; 4:23;
Where is the love?; The Black Eyed Peas; 4:13;
A string representing the name of a new song.
The operation of the function my_mp4_playlist:

The function writes to the file the string representing the name of a new song (new_song) instead of the name of the song that appears in the third line of the file (if the file contains less than three lines, write empty lines to the file so that the name of the song is written in the third line).
The function prints the contents of the file after the change has been made.
An example of running the my_mp4_playlist function on the songs.txt file
>>> my_mp4_playlist(r"c:\my_files\songs.txt", "Python Love Story")
Tudo Bom; Static and Ben El Tavori; 5:13;
I Gotta Feeling; The Black Eyed Peas; 4:05;
Python Love Story;Unknown;4:15;
Paradise; Coldplay; 4:23;
Where is the love?; The Black Eyed Peas; 4:13;
The contents of the songs.txt file after

Tudo Bom;Static and Ben El Tavori;5:13;
I Gotta Feeling;The Black Eyed Peas;4:05;
Python Love Story;Unknown;4:15;
Paradise;Coldplay;4:23;
Where is the love?;The Black Eyed Peas;4:13;

'''
def my_mp4_playlist(file_path, new_song):
    with open(file_path, 'r') as f:
        lines = f.readlines()
        
    while len(lines) < 3:
        lines.append(";;\n")

    song_parts = new_song.split(';')
    song_name = song_parts[0]
    artist = "Unknown"
    if len(song_parts) > 1:
        artist = song_parts[1]

    lines[2] = f"{song_name};{artist};\n"

    with open(file_path, 'w') as f:
        f.writelines(lines)

    with open(file_path, 'r') as f:
        print(f.read())

def main():
    my_mp4_playlist(r"c:\my_files\songs.txt", "Python Love Story")

if __name__ == "__main__":
    main()

    
