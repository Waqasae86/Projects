# choosing from a range of movie
movies = {
    "Rush": [18,5],
    "The Bad Guys": [3,5],
    "Ready Player One": [13,5],
    "Glory Road": [12,5]
    }

# pick a movie, then user will be asked of age
while True:
    choice = input("What movie would you like to see?: ").strip().title()
    if choice in movies:
        age = int(input ("How old are you?: ").strip())

# if they are old enough to watch and enough seats are available
        if age >= movies[choice][0]:
            if movies[choice][1] > 0:
                
# then the seat will be booked
                print("Enjoy the movie!")
                movies[choice][1] = movies[choice][1] - 1

# else error of either age is too little or not enough seats available
            else:
                print("Sorry, this movie is sold out.")               
        else:
            print("You are too young for this movie.")       
    else:
        print("We do not have that film")




