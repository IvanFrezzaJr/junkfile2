#!/usr/bin/env python3

import argparse
from junkfile.app import app


""" Usage:
    python .\junkfile -i D:\\Users\\Ivan\\Documents\\dev\\old\\test2\\ --copy

"""


parser = argparse.ArgumentParser(description="=== junk files organizer ===")
parser.add_argument(
    "-i",
    "--dir-in",
    help="path to organize. E.g.: /Home/Jhon/docs",
    required=True,
    type=str,
)
parser.add_argument(
    "-o",
    "--dir-out",
    help="path to copy. E.g.: /Home/Jhon/docs",
    type=str,
)

parser.add_argument(
    "-c", "--copy", help="True if would like make a directory copy", action="store_true"
)

# default function
parser.set_defaults(func=app.run)

# parse arguments
args = parser.parse_args()

# calls function
try:
    args.func(args.dir_in, args.dir_in, args.copy)


except Exception as e:
    print(f"[Junkfile] - ERROR: {e}")
