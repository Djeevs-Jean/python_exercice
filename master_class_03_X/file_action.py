from pathlib import Path

class FileAction:
    """Class File Action."""

    def __init__(self, path_file:Path) -> None:
        self.__path_file = Path(path_file)

    def reader_file(self):
        """ Read in a file."""
        if self.__path_file.exists() and self.__path_file.is_file():
            with open(self.__path_file, 'r+') as reader:
                to_read = reader.read()
                reader.close()
                return to_read

    def delete_content_file(self):
        """ Delete content file."""
        if self.__path_file.exists() and self.__path_file.is_file():
            with open(self.__path_file, 'w') as del_items:
                del_items.write('')
                del_items.close()

    def delete_file(self):
        """Delele file in fs."""
        if self.__path_file.exists() and self.__path_file.is_file():
            self.__path_file.unlink()

    def writer_file(self, word:str):
        """ Write to file."""
        # if self.__file_path.exists() and self.__file_path.is_file():
        with open(self.__path_file, 'a+') as writter:
            writter.write(word + '\n') 
            writter.close()          

# test
chemin_fichier = Path(__file__).parent.parent.joinpath("test/text1.txt")
obj_fichier = FileAction(chemin_fichier)

print(obj_fichier.reader_file())
obj_fichier.delete_content_file()

print(obj_fichier.reader_file())
obj_fichier.writer_file("JESUS CHRIST")

print(obj_fichier.reader_file())