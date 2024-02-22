class Walker:
    def __init__(self):
        self.xcord = 0
        self.ycord = 0

    def walk(self, path):
        for p in path:
            match p:
                case "n": self.ycord += 1
                case "s": self.ycord -= 1
                case "e": self.xcord += 1
                case "w": self.xcord -= 1

    def coords(self):
        return (self.xcord, self.ycord)
