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
        rec = Rectangle(1, 10,8,7,12)
        rec.create(**{"id":12,"width":18})
        self.assertEqual(rec.x, 8)
        self.assertEqual(rec.y, 7)
        self.assertEqual(rec.id, 12)

        
    def test_Rec_constructor5(self):
        """test_Rec_constructor5"""
        rec = Rectangle(1, 10,8,7)
        rec.update(1,2,3,4,5)
        self.assertEqual(rec.x, 4)
        self.assertEqual(rec.y, 5)
        self.assertEqual(rec.id, 1)
        self.assertEqual(rec.y, 5)
        
    def test_Rec_constructor6(self):
        """test_Rec_constructor6"""

        rec = Rectangle(1, 1,1,1,8)
        self.assertEqual(rec.id, 8)
        rec.update(1,2,3,4,5)
        self.assertEqual(rec.id, 1)
        self.assertEqual(rec.width, 2)
        self.assertEqual(rec.height, 3)
        self.assertEqual(rec.x, 4)
        self.assertEqual(rec.y, 5)
        
    def test_Rec_constructor7(self):
        """test_Rec_constructor6"""
        rec = Rectangle(1, 10,8,7)
        rec.update(**{"id": 1,"width":2,"height":3,"x":4,"y":5})
        self.assertEqual(rec.id, 1)
        self.assertEqual(rec.width, 2)
        self.assertEqual(rec.height, 3)
        self.assertEqual(rec.x, 4)
        self.assertEqual(rec.y, 5)
        
    def test_Rec_constructor8(self):
        """test_Rec_constructor6"""
        rec = Rectangle(1, 10,8,7)
        rec.update(10,20,30,40,50,**{"id": 1,"width":2,"height":3,"x":4,"y":5})
        self.assertEqual(rec.id, 1)
        self.assertEqual(rec.width, 2)
        self.assertEqual(rec.height, 3)
        self.assertEqual(rec.x, 4)
        self.assertEqual(rec.y, 5)
        
    def test_area(self):
        """test_Rec_constructor6"""
        rec =Rectangle(1,1)
        self.assertEqual(rec.area(), 1)
    def test_area2(self):
        """test_Rec_constructor6"""
        rec =Rectangle(10,90)
        self.assertEqual(rec.area(), 900)

        
if __name__ == '__main__':
    unittest.main()
