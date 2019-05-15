# Codecademy Python 2 Practice

# PYTHON SYNTAX
    skill_completed = "Python Syntax"

    exercises_completed = 13

    #The amount of points for each exercise may change, because points don't exist yet
    points_per_exercise = 5

    point_total = 100

    point_total += (exercises_completed * points_per_exercise)

    point_string = "I got " + str(point_total) + " points!"

    print point_string

# STRINGS & CONSOLE OUTPUT

    my_string = "Hello, world!"

    print len(my_string)

    print my_string.upper()

# DATE AND TIME

    from datetime import datetime
    now = datetime.now()

    print '%02d/%02d/%04d %02d:%02d:%02d' % (now.month, now.day, now.year, now.hour, now.minute, now.second)

# CONDITIONALS & CONTROL FLOW

    # Complete the if and elif statements!
    def grade_converter(grade):
        if grade >= 90:
            return "A"
        elif grade >= 80 and grade <= 89:
            return "B"
        elif grade >= 70 and grade <= 79:
            return "C"
        elif grade >= 65 and grade <= 69:
            return "D"
        else:
            return "F"
          
    # This should print an "A"      
    print grade_converter(92)

    # This should print a "C"
    print grade_converter(70)

    # This should print an "F"
    print grade_converter(61)

# FUNCTIONS
    
    # Function Review
    def shut_down(s):
      if s == "yes":
        return "Shutting down"
      elif s == "no":
        return "Shutdown aborted"
      else:
        return "Sorry"

    # Modules Review
    import math
    print math.sqrt(13689)

    from math import sqrt
    print sqrt(13689)

    # Built-In Functions Review 
    def distance_from_zero(num):
      if type(num) == int or type(num) == float:
        return abs(num)
      else:
        return "Nope"