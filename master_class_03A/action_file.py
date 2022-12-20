from pathlib import Path

class ActionFile:
    """Class Action File."""

    def __init__(self, file_path:Path) -> None:
        self.__file_path = Path(file_path)

    def read_file(self):
        """ Read in a file."""
        if self.__file_path.exists() and self.__file_path.is_file():
            with open(self.__file_path, 'r+') as reader:
                r = reader.read()
                reader.close()
                return r

    def del_item_into_file(self):
        """ Del items in a file."""
        if self.__file_path.exists() and self.__file_path.is_file():
            with open(self.__file_path, 'w') as del_it:
                del_it.write('')
                del_it.close()

    def delete_file(self):
        if self.__file_path.exists() and self.__file_path.is_file():
            self.__file_path.unlink()

    def write_file(self, word:str):
        """ Write in a file."""
        # if self.__file_path.exists() and self.__file_path.is_file():
        with open(self.__file_path, 'a+') as writter:
            writter.write(word + '\n') 
            writter.close()          
    
path_file = Path(__file__).parent.parent.joinpath("test/text1.txt")
obj_action = ActionFile(path_file)

print(obj_action.read_file())
obj_action.del_item_into_file()

print(obj_action.read_file())
obj_action.write_file("JESUS CHRIST")

print(obj_action.read_file())