import sys

usage_text = "usage: gol.py <input file> [iteration count]"

# Parses the program arguments and either exits with an error if something went
# wrong, or returns a (file, count) tuple, where:
#  - file    is the input file describing the world
#  - count   is the number of iterations to advance the world
#
# Note that if no iteration count arguemnt is given, it is assumed to be 1
def parse_args():
  # sys.argv[0] will always be "gol.py"
  argv = sys.argv
  argc = len(argv)
  if argc < 2:
    # TODO: error class?
    raise ValueError("Too few arguments!")
  elif argc == 2:
    iteration_count = 1
  else:
    try:
      iteration_count = int(argv[2])
    except ValueError:
      # TODO: error class?
      raise ValueError("Could not parse iteration count: " + argv[2])

  filepath = argv[1]

  try:
    input_file = open(filepath, "r")
  except FileNotFoundError:
    raise FileNotFoundError("Could not open filepath: " + filepath)

  return (input_file, iteration_count)

# build_world takes a file as its input and outputs its world representation
def build_world(input_file):
  lines = 0
  line_len = 0
  for line in input_file:
    if line_len is 0:
      line_len = len(line)
    elif len(line) is not line_len:
      # TODO: error class??
      raise ValueError("Varying-length lines in input file!")
    print(line.strip())
    lines += 1

  return None


######################
# MAIN PROGRAM START #
######################
if __name__ == "__main__":
  try:
    (input_file, iteration_count) = parse_args()
  except Exception as error:
    print(error)
    print(usage_text)
    exit(1)

  try:
    world = build_world(input_file)
  except Exception as error:
    print(error)
    print(usage_text)
    input_file.close()
    exit(2)

  input_file.close()






