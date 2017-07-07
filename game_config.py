#!/usr/bin/python3
"""
Starting configuration for the game
"""
MALE_NAMES = []
with open("male_names.txt", "r") as mnames:
    content = mnames.readlines()
content = [x.strip() for x in content]

for item in content:
    temp = item.split(",")
    for it in temp:
        MALE_NAMES.append(it)

FEMALE_NAMES = []
with open("female_names.txt", "r") as fnames:
    content = fnames.readlines()
content = [x.strip() for x in content]

for item in content:
    temp = item.split(",")
    for it in temp:
        FEMALE_NAMES.append(it)

MAX_HUMAN_AGE = 80
STARTING_COUNT_OF_PEOPLE = 25
BASIC_PROFESIIONS = ["Agriculture", "Handworking"]
LIFE_PART = MAX_HUMAN_AGE / 10
#  Chance to die in a specific age, based on life part. Please keep the number of elements accordingly to life parts
NATURAL_DEATH_CHANCES = [0, 100, 200, 300, 400, 500, 600, 700, 900, 1000] #  10 life parts, 10 chances elements
FERTILITY_AGE = 15
FERTILITY_CHANCES = [900, 900, 700, 700, 400, 300, 100, 0, 0, 0] #  10 life parts, 10 chances elements
