#
#
#   Python: 3.10.5
#
#   Author: Gary Killen
#
#   Purpose: Making our first game in python
#


def start(nice =0,jerk=0,name=""):
    #get user's name
    name = describe_game(name)
    nice,jerk,name = nice_jerk(nice,jerk,name)
    


def describe_game(name):
    """
        check if this is a new game or not.
        if it is new, get the user's name
        if it is not a new game, thank the player for
        playing again and continue with the new game
    """
    #meaning, if we do not already have this user's name
    #then they are a new player and we need to get their name
    if name != "":
        print("\nThank you forplaying again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>>").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be greeted \nby several woman. \nYou can choose to be a nice guy or Jerk")
                    print("but at the end of the game your dating life \nwill be decided by your composer")
                    stop = False
    return name


def nice_jerk(nice,jerk,name):
    stop = True
    while stop:
        show_score(nice,jerk,name)
        pick = input("\nA beautiful approaches you for a \nconversation. Will you be nice \nor a jerk? (N/J) \n>>>: ").lower()
        if pick == "n":
            print("\nThe woman struts away ...")
            nice = (nice + 1)
            stop = False
        if pick == "j":
            print ("\nShe is appalled \nbut glances back at you...")
            jerk = (jerk + 1)
            stop = False
    score(nice,jerk,name) # pass the 3 variables to the score()        


def show_score(nice,jerk,name):
    print("\n{}, your current total: \n({}, Nice) and ({}, Jerk)".format(name,nice,jerk))

def score(nice,jerk,name):
    #score function is being passed the values stores within the 3 variables
    if nice > 2:  #if condition is valid, call win function passing in the variables so it can use them
        win(nice,jerk,name)
    if jerk > 2:  #if condition is valid, call lose function passing in the variables so it can use them
        lose(nice,jerk,name)
    else:         #else, call nice_mean fucntion passing in the variable so it can use them
        nice_jerk(nice,jerk,name)

def win(nice,jerk,name):
    # Substitute the {} wildcard with our variable values
    print("\nNice Job {}, winner winner chicken dinner! \nShe wont date you but I hear there is an opening in the friendzone \n".format(name))
    # call again function and pass in our variables
    again(nice,jerk,name)


def lose(nice,jerk,name):
    # Substitute the {} wildcard with our variable values
    print("\nAhhh good for you ! \n{}, being a jerk got you a date \nshe proably wont love you in the end but hey it is what it is!".format(name))
    # call again function and pass in our variables
    again(nice,jerk,name)   


def again(nice,jerk,name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n):\n>>> ").lower()
        if choice == "y":
            stop = False
            reset(nice,jerk,name)
        if choice == "n":
            print("\noh, so sad, sorry to see you go!")
            stop = False
            quit()
        else:
            print("\nEnter ( Y ) for 'Yes', ( N ) for 'NO':\n>>> ")

def reset(nice,jerk,name):
    nice = 0
    jerk = 0
    #Notice, I do not reset the name variables as that same user has elected to play again
    start(nice,jerk,name)

if __name__ == "__main__":
    start()
