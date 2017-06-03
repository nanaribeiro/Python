import media
import fresh_tomatoes

avatar = media.Movie("Avatar",
                     "A story of a handicap man that gets a second chance in the body of an avatar",
                     "http://www.impawards.com/2009/posters/avatar.jpg",
                     "https://youtu.be/5PSNL1qE6VY")
#print(avatar.storyline)
#avatar.show_trailer()
pride_and_prejudice = media.Movie("Pride and Prejudice",
                                  "In a time where marrying a rich man was what every single woman could hope for",
                                  "http://img.moviepostershop.com/pride-and-prejudice-movie-poster-2005-1020451320.jpg",
                                  "https://youtu.be/fJA27Jujzq4")
hunger_games = media.Movie("Hunger Games",
                           "In a distant future, there is a game of life and death between districts",
                           "https://images-na.ssl-images-amazon.com/images/I/51OGv-AnD6L.jpg",
                           "https://youtu.be/4S9a5V9ODuY")
kimi_na_no_wa = media.Movie("Your Name",
                            "They were waiting for a 1000 years commet to pass",
                            "http://i.ebayimg.com/images/g/5EgAAOSw4shX6KSD/s-l300.jpg",
                            "https://youtu.be/hRfHcp2GjVI")
movies = [avatar, pride_and_prejudice, hunger_games, kimi_na_no_wa]
#print(media.Movie.__module__) - prints the name of the class
#print(media.Movie.__name__) -  prints name of the module in which the class was defined
fresh_tomatoes.open_movies_page(movies)
#pride_and_prejudice.show_trailer()
