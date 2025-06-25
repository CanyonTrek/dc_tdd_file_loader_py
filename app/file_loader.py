from pathlib import Path

class FileLoader:
    def __init__(self, file_to_load):
        self.file_to_load = file_to_load
        self.lines = []

    def load_file(self, fname):
        try:
            self.lines = Path(fname).read_text(encoding='utf-8').splitlines()
        except Exception:
            self.lines = []

        return self._calculate_file_size()

    def _calculate_file_size(self):
        total_length = sum(len(line) for line in self.lines)
        return total_length

