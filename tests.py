import unittest

import gol

class TestWorldCreation(unittest.TestCase):
  def testBuildWorldFailsOnBadLengthLines(self):
    badLengthFile = open("faulty_worlds/bad_length", "r")
    self.assertRaises(ValueError, gol.buildWorld, badLengthFile)
    badLengthFile.close()

  def testBuildWorldSucceedsOnOkayInput(self):
    okInputFile = open("worlds/blink", "r")
    result = gol.buildWorld(okInputFile)
    okInputFile.close()

    self.assertTrue(result[4, 1].isAlive())

if __name__ == "__main__":
  unittest.main()
