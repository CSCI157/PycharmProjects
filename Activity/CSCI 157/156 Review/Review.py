from ast import literal_eval

__author__ = 'Fossum'

eof = False


class Song:
    def __init__(self, filepointer=None):
        self.band_members = {}
        if filepointer is not None:
            self.song_title = filepointer.readline()
            song_members = filepointer.readline()
            self.chart_rank = filepointer.readline()
            self.band_members.update(literal_eval(song_members))
        else:
            self.song_title = input("Please enter the title of the song: ")
            number = input("Please enter how many band members there are: ")
            band = 0
            while band in range(int(number)):
                name = input("Please enter the name of the band member: ")
                instrument = input("Please enter the instrument that the previous band member plays: ")
                self.band_members[name] = instrument
                band += 1
            self.chart_rank = input("Please enter the chart rank: ")

    def __str__(self):
        body = "    The song called " + self.song_title.strip() + "\n      played by " + \
               (str(self.band_members).strip("{}").replace("'", "").replace("[", "").replace("]", "")) + \
               ";\n        has reached a chart rank of " + str(self.chart_rank)
        return body

    def save(self, filepointer):
        filepointer.write(self.song_title.strip() + "\n" + str(self.band_members) + "\n" + self.chart_rank + "\n")


class Album:
    def __init__(self, filepointer=None):
        if filepointer is not None:
            self.album_title = filepointer.readline().replace("**", "")
            if self.album_title == "":
                global eof
                eof = True
            else:
                self.album_year = filepointer.readline().replace("**", "")
                self.album_producer = filepointer.readline().replace("**", "")
                self.songs = []
                self.song_count = filepointer.readline().replace("**", "")
                for j in range(int(self.song_count)):
                    self.songs.append(Song(filepointer))
        else:
            self.album_title = "**" + input("Please enter the album title: ") + "**"
            self.album_year = "**" + input("Please enter the year the album was released: ") + "**"
            self.album_producer = "**" + input("Please enter the albums producer: ") + "**"
            self.song_count = input("How many songs are in the album? ")
            self.songs = []
            for i in range(0, int(self.song_count)):
                self.songs.append(Song())

    def __str__(self):
        header = self.album_title.strip().replace("**", "") + " produced by " +\
                 self.album_producer.strip().replace("**", "") + " in the year " +\
                 self.album_year.strip().replace("**", "") + " has " + self.song_count.strip() + " song(s). \n"
        for song in self.songs:
            header += str(song)
        return header

    def save(self, filepointer):
        filepointer.write(self.album_title.strip() + "\n" + self.album_year.strip() + "\n" +
                          self.album_producer.strip() + "\n" + self.song_count.strip() + "\n")
        for song in self.songs:
            song.save(filepointer)


def options():
    menu = ("1. Input a new album.", "2. Print albums.", "3. Quit.")
    end = len(menu)
    inputcommand = "\nYou must input a number from 1 to " + str(end) + ": "
    while True:
        for j in menu:
            print(j)
        choice = input("\nPlease make a choice 1 - " + str(end) + ": ")
        try:
            num = int(choice)
            if 1 <= num <= end:
                return num
            else:
                print(inputcommand)
                print("\n")
                return options()
        except ValueError:
            print(inputcommand)
            print("\n")
            return options()


album_list = []
with open("songlist.csv", "r+", encoding="utf-8") as text:
    new_album = Album(text)
    while not eof:
        album_list.append(new_album)
        new_album = Album(text)

selection = 0
while selection != 3:
    selection = options()
    if selection == 1:
        new_album = Album()
        album_list.append(new_album)
    elif selection == 2:
        for album in album_list:
            print(album)

with open("songlist.csv", "w+", encoding="utf-8") as text:
    for album in album_list:
        album.save(text)
