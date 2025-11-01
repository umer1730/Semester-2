class FileHandler:
    def __init__(self,filename):
        self.file = open(filename,"w")
        print(f"File {filename} opened")
    def __del__(self):
        self.file.close()
        print("File closed")
fh = FileHandler("test.txt")
del fh
class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def get_grade(self):
        if self.marks >= 80:
            return 'A'
        elif self.marks >= 60:
            return 'B'
        else:
            return 'C'
s1 = Student('Ayesha', 7, 85)
print(s1.get_grade())   # Expected Output: A


# return A, B, or C based on marks pass
s1 = Student('Ayesha', 7, 85) 
print(s1.get_grade())	# should print 'A'
s2 = Student('Ali', 5, 70)
s3 = Student('Sara', 9, 50)
print(s2.get_grade())   # B
print(s3.get_grade())


print()
class Playlist:
  def __init__(self, name):
    self.name = name
    self.songs = []

  def add_song(self, song):
    self.songs.append(song)
    print(f"Added: {song}")

  def remove_song(self, song):
    if song in self.songs:
      self.songs.remove(song)
      print(f"Removed: {song}")

  def show_songs(self):
    print(f"Playlist '{self.name}':")
    for song in self.songs:
      print(f"- {song}")

my_playlist = Playlist("Favorites")
my_playlist.add_song("Bohemian Rhapsody")
my_playlist.add_song("Stairway to Heaven")
my_playlist.show_songs()