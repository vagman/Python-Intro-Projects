class ReadingTxtFile:

    def read_txt(self, filename: str):
        f = open(filename + ".txt", "r")
        data = f.read()

        return data