# Use this handy logger to document your work automatically

# import setup_logger function from instructor-generated module
from util_logger import setup_logger

# setup the logger using the current file name (a built-in variable)
logger, logname = setup_logger(__file__)


# Import from Python Standard Library

import math

# Use the math module's constant for pi
pi = math.pi

# get the number of points scored in he first half of the basketball game
# Use \n to add a blank new line to the terminal before we ask for input
first_half_points = input("\nEnter the number of points scored in the first half: ")
second_half_points = input("\nEnter the number of points scored in the second half: ")
number_of_players = input("\nEnter the number of players who played in the game: ")

# convert the radius_string to a number
first = int(first_half_points)
second = int(second_half_points)
players = int(number_of_players)

# calculate the area using the numeric value (not the string)
total_points = first + second
average_points = (first+second)/players
max_points = max(first, second)

# log the results
logger.info(f"The sum of points scored in the game is {total_points}.")
logger.info(f"The maximum number of points scored in a half is {max_points}.")
logger.info(f"The average points scored per player is {average_points}.")


