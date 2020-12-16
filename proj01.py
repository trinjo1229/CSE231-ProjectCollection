####################################################################
# Computer Project #1
# Program prompts user for a number representing a distance in rods
# Will print conversions for rods in meters, feet, miles \
# furlongs, and minutes to walk
# The conversions will then be printed
####################################################################

METERS_PER_ROD = 5.0292
METERS_PER_FOOT = .3048
METERS_PER_MILE = 1609.34
RODS_PER_FURLONG = 40
WALK_MILES_PER_HOUR = 3.1
MINUTES_IN_HOUR = 60
 
num_of_rods_str = input("Input rods: ")
num_of_rods_flt = float(num_of_rods_str)

# Produce Number of Meters

num_of_m_flt = num_of_rods_flt * METERS_PER_ROD

# Produce Number of Feet

num_of_ft_flt = num_of_m_flt / METERS_PER_FOOT

# Produce Number of Miles

num_of_mi_flt = num_of_m_flt / METERS_PER_MILE

# Produce Number of Furlongs

num_of_fur_flt = num_of_rods_flt / RODS_PER_FURLONG

# Produce the Minutes to Walk
# Change hours to minutes
 
num_of_min_flt = (MINUTES_IN_HOUR * num_of_mi_flt) / WALK_MILES_PER_HOUR 

print("You input",round(num_of_rods_flt, 3), "rods.")
print()
print("Conversions")
print("Meters:",round(num_of_m_flt, 3))
print("Feet:",round(num_of_ft_flt, 3))
print("Miles:",round(num_of_mi_flt, 3))
print("Furlongs:",round(num_of_fur_flt, 3))
print("Minutes to walk",round(num_of_rods_flt, 3), "rods:", \
      round(num_of_min_flt, 3))
      #This is pretty darn cool if I do say so myself