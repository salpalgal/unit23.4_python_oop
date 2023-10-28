"""Word Finder: finds random words from a dictionary."""
import random


class WordFinder:
    ...
    def __init__(self, path):
        self.path =path
        self.fileArr = []

    def readFile(self):
        
        file=open(self.path)
        for line in file:
            self.fileArr.append(line[:-1])
        file.close()
        return self.fileArr

    def random(self):
        return random.choices(self.fileArr)

class SpecialWordFinder(WordFinder):
    def __init__(self,path):
        super().__init__(path)
        self.specialFileArr=[]

    def specialReadFile(self):
        file=open(self.path)
        for word in file:
            if word[0] == "#" and word.isspace():
                pass
            else:
                self.specialFileArr.append(word[:-1])
        file.close()
        return self.specialFileArr
    def specialRandom(self):
        return random.choices(self.specialFileArr)
        





    

