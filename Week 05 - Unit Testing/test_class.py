import unittest
from worker import NormalIncrease

class TestNormalIncrease(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Big test started \n")

    @classmethod
    def tearDownClass(cls):
        print("Big test end")

    def setUp(self):
        print("setUp")
        self.dorj = NormalIncrease("Dorj","Misha", 800000)
        self.myagmar = NormalIncrease("Myagmar","Bold", 760000)

    def tearDown(self):
        print("tearDown \n")

    def test_fullname(self):
        print("test_fullname")
        self.assertEqual(self.dorj.fullname(), 'Dorj Misha')
        self.assertEqual(self.myagmar.fullname(), 'Myagmar Bold')

        # We will change lastnames just to check the lastnames have been changed in the object
        self.dorj.lname = "Huyag"
        self.myagmar.lname = "Gan"

        self.assertEqual(self.dorj.fullname(), "Dorj Huyag")
        self.assertEqual(self.myagmar.fullname(), "Myagmar Gan")

    def test_apply_raise(self):
        print("test_apply_raise")
        # 800000*1.2 = 960000(Dorj's expected salary)
        # 760000*1.2 = 912000(Myagmar's expected salary)
        self.dorj.apply_raise()
        self.myagmar.apply_raise()

        self.assertEqual(self.dorj.salary, 960000)
        self.assertEqual(self.myagmar.salary, 912000)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)