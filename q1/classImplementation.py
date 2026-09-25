class Music:
    def __init__(self, title, artist, genre, publication_year):
        self.song_title = title
        self.artist = artist
        self.genre = genre
        self.publication_year = publication_year 
        self.__current_time = 0
        self.__is_playing = False

    def playBack(self, seconds):
        self.__current_time = max(0, self.__current_time - seconds) 
        print(f"Current time: {self.__current_time} seconds")  

    def skip(self):
        self.__is_playing = False
        print("Skipping track.")

    def pause(self):
        self.__is_playing = False
        print("Pausing track.") 

    def get_publication_year(self):
        return self.publication_year  

    def set_publication_year(self, year):
        if isinstance(year, int) and year > 0:
            self.publication_year = year
        else:
            print("Invalid publication year. Please provide a positive integer.")   


    def display_info(self):
        print(f"Title: {self.song_title}")
        print(f"Artist: {self.artist}")
        print(f"Genre: {self.genre}")
        print(f"Publication Year: {self.publication_year}")
        print(f"Current Time: {self.__current_time} seconds")
        print(f"Is Playing: {self.__is_playing}")

music_1 = Music("Sa'yo", "Silent Sanctuary", "OPM", 2013)
music_2 = Music("Dahan", "Over October", "OPM", 2025)

print("--- BEFORE ---")
music_1.display_info()
print()
music_2.display_info()

print("\n--- UPDATING ---")
music_1.playBack(30)
music_1.pause()
music_2.skip()

print("\n--- AFTER ---")
music_1.display_info()
print()
music_2.display_info()
