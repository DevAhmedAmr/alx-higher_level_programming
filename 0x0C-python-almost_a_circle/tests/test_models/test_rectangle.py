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
        """test_Rec_constructor7"""
        rec = Rectangle(1, 10,8,7)
        rec.update(**{"id": 1,"width":2,"height":3,"x":4,"y":5})
        self.assertEqual(rec.id, 1)
        self.assertEqual(rec.width, 2)
        self.assertEqual(rec.height, 3)
        self.assertEqual(rec.x, 4)
        self.assertEqual(rec.y, 5)
        
    def test_Rec_constructor8(self):
        """test_Rec_constructor8"""
        rec = Rectangle(1, 10,8,7)
        rec.update(10,20,30,40,50,**{"id": 1,"width":2,"height":3,"x":4,"y":5})
        self.assertEqual(rec.id, 1)
        self.assertEqual(rec.width, 2)
        self.assertEqual(rec.height, 3)
        self.assertEqual(rec.x, 4)
        self.assertEqual(rec.y, 5)
        
    def test_area(self):
        """test_area"""
        rec =Rectangle(1,1)
        self.assertEqual(rec.area(), 1)
        
    def test_area2(self):
        """test_area2"""
        rec =Rectangle(10,90)
        self.assertEqual(rec.area(), 900)

    def test_2(self):
        """test 2"""
        r0 = Rectangle(1, 2, 3)
        self.assertEqual(r0.width, 1)
        self.assertEqual(r0.height, 2)
        self.assertEqual(r0.x, 3)
        self.assertEqual(r0.y, 0)
        self.assertEqual(r0.__str__(), "[Rectangle] (4) 3/0 - 1/2")
        self.assertEqual(r0.area(), 2)
        output = {'x': 3, 'y': 0, 'id': 4, 'height': 2, 'width': 1}
        self.assertEqual(r0.to_dictionary(), output)

    def test_3(self):
        """test 3"""
        r0 = Rectangle(1, 2, 3, 4,5)
        self.assertEqual(r0.id, 5)
        self.assertEqual(r0.width, 1)
        self.assertEqual(r0.height, 2)
        self.assertEqual(r0.x, 3)
        self.assertEqual(r0.y, 4)
        self.assertEqual(r0.__str__(), "[Rectangle] (5) 3/4 - 1/2")
        self.assertEqual(r0.area(), 2)
        output = {'x': 3, 'y': 4, 'id': 5, 'height': 2, 'width': 1}
        self.assertEqual(r0.to_dictionary(), output)

    def test_4(self):
        """test 4"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("1", 2)

    def test_5(self):
        """test 5"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "2")

    def test_6(self):
        """test 6"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "3")

    def test_7(self):
        """test 7"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, "4")

    def test_8(self):
        """test 8"""
        r0 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r0.id, 5)
        self.assertEqual(r0.width, 1)
        self.assertEqual(r0.height, 2)
        self.assertEqual(r0.x, 3)
        self.assertEqual(r0.y, 4)
        self.assertEqual(r0.__str__(), "[Rectangle] (5) 3/4 - 1/2")
        self.assertEqual(r0.area(), 2)
        output = {'x': 3, 'y': 4, 'id': 5, 'height': 2, 'width': 1}
        self.assertEqual(r0.to_dictionary(), output)

    def test_9(self):
        """test 9"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)

    def test_10(self):
        """test 10"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -2)

    def test_11(self):
        """test 11"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_12(self):
        """test 12"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)
            
if __name__ == '__main__':
    unittest.main()
