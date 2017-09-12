# game-of-life.py - An implementation of Conway's Game of Life in Python.
# Joe Graham - 9/11/17

import argparse, io

# Parse in config filename, number of generations, and whether or not to pause
# between generations from the command line. argparse will auto stop if not
# enough mandatory parameters are passed as arguments.

parser = argparse.ArgumentParser(description="Conway's Game of Life in Python.")
parser.add_argument("config", help="Configuration file " +
    "describing grid size and initial board config.")
parser.add_argument("gens", metavar="generations",
    help="Number of generations for the simulation to run.")
parser.add_argument("--continuous", "-c", action="store_true",
    help="Run the simulation continuously without stopping for each generation.")

# Parse arguments and assign them to variables.

args = parser.parse_args()
configFilename = args.config
numGens = args.gens
continuousFlag = args.continuous

# Read in the config file.

config = io.open(configFilename, mode='r')
firstLine = True
for line in config:
    # Ignore comments.
    if not line.startswith("#"):
        # Initialize the board if this is the first line of the file.
        if firstLine:
            numRows = int(line[0])
            numCols = int(line[2])
            firstLine = False
            gameBoard = [[0]*numCols for _ in range(numRows)]
            curRow = 0
            curCol = 0
        # Read in the current row if this isn't the first line.
        else:
            for char in line.rstrip():
                if str(char) != "0":
                    gameBoard[curRow][curCol] = 1
                curCol += 1
            curRow += 1
            curCol = 0
print gameBoard
