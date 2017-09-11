# game-of-life.py - An implementation of Conway's Game of Life in Python.
# Joe Graham - 9/11/17

import argparse

parser = argparse.ArgumentParser(description="Conway's Game of Life in Python.")
parser.add_argument("config", help="Configuration file " +
    "describing grid size and initial board config.")
parser.add_argument("gens", metavar="generations",
    help="Number of generations for the simulation to run.")
parser.add_argument("--continuous", "-c", action="store_true",
    help="Run the simulation continuously without stopping for each generation.")

args = parser.parse_args()
print args
