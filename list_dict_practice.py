# list stores the order
fav_movies = ["The Matrix", "Inception", "Interstellar", "The Dark Knight", "Avengers: Endgame"]

# dict stores the details, keyed by title
movie_info = {
    "The Matrix":           {"year": 1999, "rating": 8.7},
    "Inception":            {"year": 2010, "rating": 8.8},
    "Interstellar":         {"year": 2014, "rating": 8.6},
    "The Dark Knight":      {"year": 2008, "rating": 9.0},
    "Avengers: Endgame":    {"year": 2019, "rating": 8.4}
}

def ask_for_number():
    while True:

        ask_input = input("Type a number between 1 and 5 to see your favorite movies: ")
        if ask_input.isdigit():
            num = int(ask_input)
            if 1 <= num <= 5:
                return num
            else:
                print("Please enter a number between 1 and 5.")
        else:
            print("Invalid input. Please enter a number.")

num_of_movie = ask_for_number()

def get_details(num_of_movie):
    title = fav_movies[num_of_movie - 1]
    details = movie_info[title]
    return title, details

title, details = get_details(num_of_movie)

print(f"{title} ({details['year']}) — Rating: {details['rating']}")