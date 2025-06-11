import unittest
import helpers

class TestHelpers(unittest.TestCase):
    def test(self):
        aux = "# Hello\n"
        title = helpers.extract_title(aux)

        self.assertEqual("Hello", title)

    def test_raise(self):
        aux = "test"
        with self.assertRaises(Exception):
            helpers.extract_title(aux)

if __name__ == '__main__':
    unittest.main()