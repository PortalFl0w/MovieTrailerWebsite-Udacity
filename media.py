#Imports
import webbrowser

#Useful functions
def valid_rating(given_rating, valid_ratings):
        #Check if the rating is valid
        for rating in valid_ratings:
            if given_rating == rating:
                return rating
        return null


#Create class Movie
class Movie():
    """ PROVIDES A WAY OF STORING INFO ABOUT A MOVIE """

    #constant variable storing valid ratings for our movies
    VALID_RATINGS = ["G" "PG", "PG+13", "R"]
    
    def __init__(self, title, storyline, image, trailer, rating):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = image
        self.trailer_youtube_url = trailer
        self.rating = valid_rating(rating, self.VALID_RATINGS)

    def show_trailer(self):
        #Opens the trailer in user default web browser
        webbrowser.open(self.trailer_youtube_url)
