class Key:
    def __init__(self, color, teeth):
        self.color = color
        self.teeth = teeth

    def __eq__(self, other):
        if not isinstance(other, Key):
            return NotImplemented
        return self.color == other.color and self.teeth == other.teeth

    def __str__(self):
        outStr = "A " + self.color + " " + str(self.teeth) + "-toothed key"
        return outStr
