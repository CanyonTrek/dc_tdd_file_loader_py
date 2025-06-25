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

        # Act
        bytes_read = cut.load_file_with_func(lambda fname: pretend_file_content)

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
        expected_bytes_read = 10

        # act
        bytes_read = cut.load_file_with_func(lambda fname: ["Hello", "world"])

        # assert
        self.assertEqual(expected_bytes_read, bytes_read)


if __name__ == '__main__':
    unittest.main()

