# usage: python load_display_json.py --json <PATH_TO_JSON>

# import necessary packages
import json
import argparse
import pprint

# construct argument parser and parse arguments
ap = argparse.ArgumentParser()
ap.add_argument("-j", "--json", required=True, help="Path to JSON file")
args = vars(ap.parse_args())

# create PrettyPrinter object
pp = pprint.PrettyPrinter()

# read and display json
def load_display_json(json_file):
	with open(json_file) as f:
		dictionary = json.load(f)
		pp.pprint(dictionary)


load_display_json(args["json"])
