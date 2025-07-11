from cow import Cow

class FileCow(Cow):

    def __init__(self, name, filename):
        super().__init__(name)
        self.image = None
        im = open(filename, "r") # Opens the file
        try:
            self.image = im.read() # Reads the file contents
            if self.image == None:
                raise RuntimeError # Raises runtime error if self.image is failed to change
        except RuntimeError:
            print("MOOOOO!!!!!!")

    def set_image(self, image):
        try:
            raise RuntimeError # Always raise runtime error due to specs in the lab
        except RuntimeError:
            print("Cannot reset FileCow Image")

