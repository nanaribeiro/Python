import webbrowser
class Movie():
    #This is for documentaion, stored in __doc__ variable
    """ This class provides a way to store movie related information"""
    #Create an instance of the class
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        #Initialize attributes
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
    
