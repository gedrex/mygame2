#!/usr/bin/python3
import game_config as config
"""
Industry etc., industry evolution tree
BASICS:
-----------
Name:       | Produces:    |   Needs_to_evolve:
---------------------------------------------------
Agriculture | Basic food   |        - 
----------------------------------------------------
Handworking | Basic Tools  |        -
---------------------------------------------------------
"""

class Industry(object):
    def __init__(self):
        self.branches = {}
        for item in config.BASIC_PROFESIIONS:
            self.branches["Name"] = item[0]
            self.branches["Efectivity"] = 0
            self.branches["Product"] = item[1]
            self.branches["Stock"] = 0
            self.branches["Prerequisity"] = None

