import unittest

import gol

class TestWorldCreation(unittest.TestCase):
  def test_build_world(self):
    faulty_length_file = open("faulty_worlds/bad_length", "r")
    self.assertRaises(ValueError, gol.build_world, faulty_length_file)
    faulty_length_file.close()

if __name__ == "__main__":
  unittest.main()
