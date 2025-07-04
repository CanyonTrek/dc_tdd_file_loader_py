import unittest
from app.file_loader import FileLoader

class TestFileLoader(unittest.TestCase):

    def test_load_all_of_file_using_inbuilt_files_type_as_lambda(self):
        # Arrange
        file_to_load = "sample.txt"
        cut = FileLoader(file_to_load)
        expected_bytes_read = 12

        # Calculate expected number of characters
        with open(file_to_load, encoding="utf-8") as f:
            expected_bytes_read = sum(len(line) for line in f.readlines())

        # Act
        bytes_read = cut.load_file_with_func(lambda fname: open(fname,
                                             encoding="utf-8").readlines())

        # Assert
        self.assertEqual(expected_bytes_read, bytes_read)



if __name__ == '__main__':
    unittest.main()

