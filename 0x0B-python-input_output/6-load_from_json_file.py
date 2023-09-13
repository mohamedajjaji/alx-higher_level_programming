#!/usr/bin/python3
""" Defines function """
import json


def load_from_json_file(filename):
    """ Creates an Object from a “JSON file” """
    with open(filename) as fl:
        return json.load(fl)
