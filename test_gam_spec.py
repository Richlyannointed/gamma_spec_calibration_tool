import unittest
import main

class GeneralTesting(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()
    
    def tearDown(self) -> None:
        return super().tearDown()
    
    def test_module(self):
        result = main.add(2, 3)
        self.assertAlmostEqual(result, 5.1, 0)

if __name__ == '__main__':
    unittest.main()