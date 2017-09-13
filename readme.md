# Conway's Game of Life
## Development environment
Simply install [Python](https://www.python.org).
## Compilation instructions
No compilation is necessary, Python code is compiled when it is ran by the user
## How to run the software
Using a command line interface on whatever OS you're using, run
`python ./game-of-life.py [--continuous] config generations` where config
is the location of a config file (more on that in the next section),
generations is the number of generations you want the simulation to run for,
and --continuous is an optional flag that tells the simulation not to wait for
user input before continuing to the next generation. -c can also be used.
Running the program without any command-line options or with the -h option will display help text.
## Config file
Sample config files can be found in this repo. The default one, called config,
is the same as the glider config. The comments at the top of each config file
describe the syntax of these config files: any line starting with a # is
assumed to be a comment and ignored. The first non-comment line must have two
values: the number of rows, and the number of columns that the game grid will
be made up of. Every other line in the file is read in as the initial
simulation state. A 0 represents a dead cell, any other character represents
an alive cell. In the example configs, a 1 is used for this character.
