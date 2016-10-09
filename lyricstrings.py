class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def write_me_a_sing(self):
        for line in self.lyrics:
            print line

happy_anniversary = Song(["Happy anniversary to all",
                          "You better buy a present",
                          "Or you're on the couch boy"])

sunny_day_today = Song(["What a beautiful day",
                        "Wish I could enjoy it"])

happy_anniversary.write_me_a_sing()

sunny_day_today.write_me_a_sing()
