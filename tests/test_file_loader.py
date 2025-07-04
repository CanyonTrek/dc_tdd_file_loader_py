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


    def test_load_all_of_file_via_stub(self):
        """ Use a hardcoded stub to simulate reading two lines of text
            Benefit - no dependencyon actual files or filesystem
                    - portable test
                    - FileLoader is more flexible and decoupled allowing
                      file loading mechanism to be injected
        """
        # arrange
        file_to_load = ""
        cut = FileLoader(file_to_load)
        expected_bytes_read = 12

        # act
        bytes_read = cut.load_file_with_func(lambda fname: ["Hello", "world"])

        # assert
        self.assertEqual(expected_bytes_read, bytes_read)


    def test_load_all_of_file_using_mock(self):
        # Arrange
        file_to_load = "sample.txt"
        cut = FileLoader(file_to_load)

        # Simulate file content
        pretend_file_content = ["Hello", "world"]
        expected_bytes_read = 10

        # Create a mock callable for reading files
        mock_file_reader = Mock()
        mock_file_reader.return_value = pretend_file_content

        # Act
        # bytes_read = cut.load_file_with_func(lambda fname: mock_file_reader(fname))
        bytes_read = cut.load_file_with_func(lambda fname: mock_file_reader("XYZ"))

        # Assert
        self.assertEqual(expected_bytes_read, bytes_read)



if __name__ == '__main__':
    unittest.main()

