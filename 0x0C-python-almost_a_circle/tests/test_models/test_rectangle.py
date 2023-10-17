#!/usr/bin/python3
"""modules"""
import sys
import os
import inspect

# Get the directory of the currently executing script
current_file = inspect.getfile(inspect.currentframe())
current_dir = os.path.dirname(os.path.abspath(current_file))

# Get the parent directory (your project's root)
project_dir = os.path.dirname(current_dir)

# Add the project's root directory to sys.path
sys.path.append(project_dir)

""" Module for test rectangle class """
import unittest
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base

"""testRectangle"""
class testRectangle(unittest.TestCase):
    
    def test_Rec_constructor(self):
        """test_Rec_constructor"""
        rec = Rectangle(1, 10)
        self.assertEqual(rec.width, 1)
        self.assertEqual(rec.height, 10)
        
    def test_Rec_constructor2(self):
        """test_Rec_constructor2"""

        rec = Rectangle(1, 10,8,7)
        self.assertEqual(rec.x, 8)
        self.assertEqual(rec.y, 7)

if __name__ == '__main__':
    unittest.main()
