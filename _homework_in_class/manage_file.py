from pathlib import Path

class ManageFile:
    """Class Manage File."""

    def __init__(self, path_file) -> None:
        self.path_file = path_file

    def read_file(self):
        with open(self.path_file, "r") as file:
            return file.read()

    def _write_file(self, msg, mode):
        with open(self.path_file, mode) as writting:
            writting.write(msg)

    def append(self, text):
        self._write_file(text + "\n", "a")

    def prepend(self, text):
        text1 = self.read_file()
        self._write_file(text + "\n", "w")
        self._write_file(text1, "a+")

    def add(self, text):
        self._write_file(text + "\n", "w")

    def clean(self):
        self._write_file("", "w")
    
# test
chemin_fichier = Path(__file__).parent.parent.joinpath("test/programiz.txt")
obj = ManageFile(chemin_fichier)

# obj.clean()
obj.read_file()

# obj.append("append")
obj.prepend("0preppend")


# print(obj_fichier.read_file())
obj.read_file()
