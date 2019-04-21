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
