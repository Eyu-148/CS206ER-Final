class FITNESS:
    def __init__(self, floating, distance):
        self.floating = floating
        self.distance = distance

    # overload operator
    def __gt__(self, other):
        # a greater fitness is not good
        if (self.floating > other.floating) and (self.distance > other.distance):
            return True
        if (self.floating == other.floating) and (self.distance > other.distance):
            return True
        if (self.floating > other.floating) and (self.distance == other.distance):
            return True
        else:
            return False

    def __lt__(self, other):
        if (self.floating < other.floating) and (self.distance < other.distance):
            return True
        if (self.floating == other.floating) and (self.distance < other.distance):
            return True
        if (self.floating < other.floating) and (self.distance == other.distance):
            return True
        else:
            return False

    def __eq__(self, other):
        if (self.floating == other.floating) and (self.distance == other.distance):
            return True
        else:
            return False

    def __ne__(self, other):
        if (self.floating != other.floating) and (self.distance != other.distance):
            return True
        else:
            return False