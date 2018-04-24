#Imports
import media, fresh_tomatoes

#Establish all the movie variables
interstellar = media.Movie("Interstellar",
                           "Space Stuff And Black Holes",
                           "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                           "https://www.youtube.com/watch?v=3WzHXI5HizQ",
                           "R")

inception = media.Movie("Inception",
                        "Dreams",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                        "https://www.youtube.com/watch?v=1g4PLj0PlOM",
                        "R")

dark_knight = media.Movie("The Dark Knight",
                          "Batman fights evil",
                          "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                          "https://www.youtube.com/watch?v=EXeTwQWrcwY",
                          "R")

dark_knight_rises = media.Movie("The Dark Knight Rises",
                                "Batman fights evil once again!",
                                "https://upload.wikimedia.org/wikipedia/en/8/83/Dark_knight_rises_poster.jpg",
                                "https://www.youtube.com/watch?v=z5Humz3ONgk",
                                "R")

dunkirk = media.Movie("Dunkirk",
                      "Dunkirk Evacuation",
                      "https://upload.wikimedia.org/wikipedia/en/1/15/Dunkirk_Film_poster.jpg",
                      "https://www.youtube.com/watch?v=rJePvN_4T_E",
                      "R")

the_prestige = media.Movie("The Prestige",
                           "Competing Magicians and a Dark Secret",
                           "https://upload.wikimedia.org/wikipedia/en/d/d2/Prestige_poster.jpg",
                           "https://www.youtube.com/watch?v=a1AqrIkD7vU",
                           "PG+13")

                      

#Put movies into array
movies = [interstellar, inception, dunkirk, dark_knight, dark_knight_rises, the_prestige]

#Run web page using the array and fresh_tomatoes module
fresh_tomatoes.open_movies_page(movies)
