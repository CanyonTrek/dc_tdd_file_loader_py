import unittest
from app.file_loader import FileLoader

class TestFileLoader(unittest.TestCase):

    def test_load_all_of_file_using_inbuilt_files_type_as_lambda(self):
        # Arrange
        file_to_load = "sample.txt"
        cut = FileLoader(file_to_load)
        expected_bytes_read = 10

        # Prepare fake file contents
        pretend_file_content = ["Hello", "world"]

        # Define the mock loading function (acts like the lambda in Java)
        def mock_loader_func(fname):
            return pretend_file_content

        # Act
        bytes_read = cut.load_file_with_func(mock_loader_func)

        # Assert
        self.assertEqual(expected_bytes_read, bytes_read)

if __name__ == '__main__':
    unittest.main()

