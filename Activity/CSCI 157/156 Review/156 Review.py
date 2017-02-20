__author__ = 'Fossum'


class Song:
    def __init__(self, filepointer=None):
        if filepointer is not None:
            with open(filepointer+".csv", "a+", encoding="utf-8") as text:
                text.seek(0)
                song_data = text.readlines()
                number = len(song_data)
                song_data2 = [song_data[x:x+3] for x in range(0, number, 3)]
                for number_of_songs in range(len(song_data2)):
                    self.band_members = dict()
                    number2 = len(song_data2[number_of_songs])
                    song_data3 = song_data2[number_of_songs][1].strip().strip("{}")
                    tuple1 = song_data3.replace("'", "").split(",")
                    tuple2 = tuple1[0].replace(" ", "").split(":")
                    try:
                        tuple3 = tuple1[1].replace(" ", "").split(":")
                        self.band_members[tuple3[0]] = [tuple3[1]]
                        try:
                            tuple4 = tuple1[2].replace(" ", "").split(":")
                            self.band_members[tuple4[0]] = [tuple4[1]]
                            try:
                                tuple5 = tuple1[3].replace(" ", "").split(":")
                                self.band_members[tuple5[0]] = [tuple5[1]]
                                try:
                                    tuple6 = tuple1[4].replace(" ", "").split(":")
                                    self.band_members[tuple6[0]] = [tuple6[1]]
                                except:
                                    IndexError
                            except:
                                IndexError
                        except:
                            IndexError
                    except:
                        IndexError
                    self.band_members[tuple2[0]] = [tuple2[1]]
                    self.song_title = song_data2[number_of_songs][0].strip()
                    self.chart_rank = song_data2[number_of_songs][number2-1].strip().strip("'")
                    print(song_data)
                    print(song_data2)
                    print(song_data3)
                    print(self.song_title)
                    print(self.band_members)
                    print(self.chart_rank)

    def __str__(self):
        body = "The song called " + self.song_title + " played by " +\
               (str(self.band_members).strip("{}").replace("'", "").replace("[", "").replace("]", "")) +\
               "; has reached a chart rank of " + str(self.chart_rank)
        return body

list = ""
list += str(Song(filepointer="songlist")) + "\n"
print(list)
