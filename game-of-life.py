# game-of-life.py - An implementation of Conway's Game of Life in Python.
# Joe Graham - 9/11/17

import argparse, io, sys, os, platform, time

# function processCell: Takes in the cell value as an argument. Using the curRow
# and curCol global variables, it determines how many neighbors that cell has
# returns true if that should be alive in the next generation, or false if it
# shouldn't be.

def processCell(cell):
    # Define a few variables for the previous and next rows and columns.
    prevRow = curRow - 1
    nextRow = curRow + 1
    prevCol = curCol - 1
    nextCol = curCol + 1

    # All cells outside of the board are dead. If prevRow is invalid or nextRow
    # are invalid, we should start or end with the current row, respectively.
    # Same thing goes for the column variables.

    if prevRow < 0:
        prevRow = curRow
    if nextRow >= numRows:
        nextRow = curRow
    if prevCol < 0:
        prevCol = curCol
    if nextCol >= numCols:
        nextCol = curCol

    # Initialize the neighbors counter.
    neighbors = 0

    # Iterate over the neighbors of this cell. If they're alive and valid,
    # increment the neighbors counter.

    for neighborRow in range(prevRow, nextRow+1):
        for neighborCol in range(prevCol, nextCol+1):
            if gameBoard[neighborRow][neighborCol] == 1 and \
            validateSpace(neighborRow,neighborCol):
                neighbors += 1

    # Evaluate conditions based on number of neighbors.
    # Under population.
    if neighbors < 2:
        return False
    # Continued life and reproduction.
    if (neighbors == 2 and cell == 1) or neighbors == 3:
        return True
    # Over population.
    if neighbors > 4:
        return False

# function: validateSpace, takes in the row and column of the space to validate
# as arguments. Validates that that row and column is a valid neighbor. This is
# evaluated by determining if the row and column numbers are within the range
# of possible values, and that this space is not the same as the currently
# evaluated space, since a cell is not its own neighbor. Returns true if the
# space is valid, returns false if it isn't.

def validateSpace(validRow, validCol):
    if validRow < 0 or validRow == numRows:
        return False
    elif validCol < 0 or validCol == numCols:
        return False
    elif validRow == curRow and validCol == curCol:
        return False
    else:
        return True

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
try:
    numGens = int(args.gens)
except ValueError:
    sys.exit("Error: number of generations must be a number.")
continuousFlag = args.continuous

# Read in the config file.

config = io.open(configFilename, mode='r')
firstLine = True
for line in config:
    # Ignore comments.
    if not line.startswith("#"):
        # Initialize the board if this is the first line of the file.
        if firstLine:
            splitLine = line.split()
            try:
                numRows = int(splitLine[0])
            except ValueError:
                sys.exit("Error: number of rows must be a number.")
            try:
                numCols = int(splitLine[1])
            except ValueError:
                sys.exit("Error: number of columns must be a number.")
            except IndexError:
                sys.exit("Error: number of columns is missing in the config file.")
            if numRows < 3 or numCols < 3:
                sys.exit("Grid must be at least 3x3 in size.")
            firstLine = False
            gameBoard = [[0]*numCols for _ in range(numRows)]
            curRow = 0
            curCol = 0
        # Read in the current row if this isn't the first line. Any char that
        # isn't 0 represents a live cell, zeroes are ignored since the whole
        # board is initialized dead.
        else:
            for char in line.rstrip():
                if curCol == numCols:
                    sys.exit("Line " + str(curRow+1) + " is too long.")
                if curRow == numRows:
                    sys.exit("Too many rows in the config file.")
                if str(char) != "0":
                    gameBoard[curRow][curCol] = 1
                curCol += 1
            if curCol < numCols:
                sys.exit("Line " + str(curRow+1) + " is too short.")
            curRow += 1
            curCol = 0
curGen = 0
# Run the simulation only for the number of generations specified.
while curGen < numGens:
    # Clear out the previous generation's screen. Different OSes have different
    # clear commands.
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')
    # Print out this generation's board.
    for row in gameBoard:
        for cell in row:
            sys.stdout.write(str(cell))
            sys.stdout.flush()
        sys.stdout.write("\n")
        sys.stdout.flush()
    if continuousFlag is False:
        raw_input()
    # Copy this generation's board into a temporary new board.
    nextGenBoard = [[0]*numCols for _ in range(numRows)]
    curRow = 0
    curCol = 0
    for row in gameBoard:
        for cell in row:
            nextGenBoard[curRow][curCol] = cell
            curCol += 1
        curRow += 1
        curCol = 0
    # Iterate over the game board, evaluating each cell to see if it should live
    # on or not using the processCell function. If the processCell function
    # returns true, that cell is alive next generation and should be marked
    # as such on the next gen board. If it returns false, that cell is dead and
    # should be marked dead.
    curRow = 0
    curCol = 0
    for row in gameBoard:
        for cell in row:
            result = processCell(cell)
            if result is True:
                nextGenBoard[curRow][curCol] = 1
            else:
                nextGenBoard[curRow][curCol] = 0
            curCol += 1
        curRow +=1
        curCol = 0
    # Make the nextGenBoard the current gameBoard.
    gameBoard = nextGenBoard
    curGen += 1
    # Sleep for a second in between generations, so it's possible to see what's
    # going on, only if the continuous flag is set.
    if continuousFlag:
        time.sleep(0.5)
