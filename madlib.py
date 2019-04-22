def madlib_game():
#starts the game
    print "Let's play Mad Libs!"
    first_madlib()
    user_option()


#function for first round
def first_madlib():
    #collects users input
        name = raw_input("Choose a name: ")
        place = raw_input("Choose a place: ")
        food = raw_input("Choose a food: ")
        pronoun = raw_input("Choose a pronoun: ")
        friend = raw_input("Choose another name: ")
        second_food = raw_input("Choose another food: ")
        second_place = raw_input("Choose another place: ")
        adjective = raw_input("Choose an adjective: ")
        thing = raw_input("Choose an object: ")
    #prints the madlib
        print "{} was really hungry and decided to go to {} to grab some {}. On the way there, {} ran into {} and they decided to eat together. {} said they really wanted to eat {}. {} agreed that sounded great and offered to share the {} if {} shared the {}. They had a great lunch together and then went to {} because it had their favorite {} {}. The end.".format(name, place, food, pronoun, friend, friend, second_food, name, food, pronoun, second_food, second_place, adjective, thing)

#option to continue or exist
def user_option():
    restart = raw_input("Would you like to do another madlib?(Yes/No)")
    if restart == "Yes":
        second_madlib()
    elif restart == "No":
        print "Thanks for playing Mad Libs! Goodbye!"
        return
    else:
        print "That's not a valid option."
        user_option()

#function for second round
def second_madlib():
    #collects users input again
        new_name = raw_input("Choose a name: ")
        company = raw_input("Choose a company: ")
        number = raw_input("Choose a number: ")
        new_pronoun = raw_input("Choose a pronoun: ")
        city = raw_input("Choose a city: ")
        new_adjective = raw_input("Choose an adjective: ")
        animal = raw_input("Choose an animal: ")
        new_city = raw_input("Choose another city: ")
    #prints new madlib
        print "{} worked at {} for {} years and wanted to retire. {} decided to move to {} and live happily ever after. But when {} got to {}, there were too many {} {}s! So {} moved back home to {} and {} actually was happy where {} came from.".format(new_name, company, number, new_pronoun, city, new_pronoun, city, new_adjective, animal, new_name, new_city, new_pronoun, new_pronoun)
        print "Thanks for playing Mad Libs! Goodbye!"
        return

#runs Mad Lib program
madlib_game()
