#!/usr/bin/python3
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
        
    def test_Rec_constructor3(self):
        """test_Rec_constructor3"""
        rec = Rectangle(1, 10,8,7)
        rec.create(**{"id":12,"width":18})
        self.assertEqual(rec.width, 1)
        self.assertEqual(rec.height, 10)
        
    def test_Rec_constructor4(self):
        """test_Rec_constructor4"""
        rec = Rectangle(1, 10,8,7)
        rec.create(**{"id":12,"width":18})
        self.assertEqual(rec.x, 8)
        self.assertEqual(rec.y, 7)

if __name__ == '__main__':
    unittest.main()
