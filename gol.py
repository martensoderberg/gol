import sys

usageText = "usage: gol.py <input file> [iteration count]"

# Parses the program arguments and either exits with an error if something went
# wrong, or returns a (file, count) tuple, where:
#  - file    is the input file describing the world
#  - count   is the number of iterations to advance the world
#
# Note that if no iteration count arguemnt is given, it is assumed to be 1
def parseArgs():
  # sys.argv[0] will always be "gol.py"
  argv = sys.argv
  argc = len(argv)
  if argc < 2:
    # TODO: error class?
    raise ValueError("Too few arguments!")
  elif argc == 2:
    iterationCount = 1
  else:
    try:
      iterationCount = int(argv[2])
    except ValueError:
      # TODO: error class?
      raise ValueError("Could not parse iteration count: " + argv[2])

  filePath = argv[1]

  try:
    inputFile = open(filePath, "r")
  except FileNotFoundError:
    raise FileNotFoundError("Could not open filepath: " + filePath)

  return (inputFile, iterationCount)

# buildWorld takes a file as its input and outputs its world representation
def buildWorld(inputFile):
  lines = 0
  lineLen = 0
  for line in inputFile:
    if lineLen is 0:
      lineLen = len(line)
    elif len(line) is not lineLen:
      # TODO: error class??
      raise ValueError("Varying-length lines in input file!")
    lines += 1

  return None


######################
# MAIN PROGRAM START #
######################
if __name__ == "__main__":
  try:
    (inputFile, iterationCount) = parseArgs()
  except Exception as error:
    print(error)
    print(usageText)
    exit(1)

  try:
    world = buildWorld(inputFile)
  except Exception as error:
    print(error)
    print(usageText)
    inputFile.close()
    exit(2)

  inputFile.close()






